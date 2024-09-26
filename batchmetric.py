import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import mean_squared_error as mse
import lpips

class ImageQualityAssessmentTool:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Quality Assessment Tool")
        self.master.geometry("400x300")

        self.reference_image_path = tk.StringVar()
        self.comparison_folder_path = tk.StringVar()

        self.create_widgets()

        # Initialize LPIPS
        try:
            self.lpips_model = lpips.LPIPS(net='alex')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize LPIPS model: {str(e)}")
            self.lpips_model = None

    def create_widgets(self):
        tk.Label(self.master, text="Reference Image:").pack(pady=5)
        tk.Entry(self.master, textvariable=self.reference_image_path, width=50).pack()
        tk.Button(self.master, text="Browse", command=self.browse_reference_image).pack(pady=5)

        tk.Label(self.master, text="Comparison Folder:").pack(pady=5)
        tk.Entry(self.master, textvariable=self.comparison_folder_path, width=50).pack()
        tk.Button(self.master, text="Browse", command=self.browse_comparison_folder).pack(pady=5)

        tk.Button(self.master, text="Evaluate", command=self.evaluate_images).pack(pady=20)

    def browse_reference_image(self):
        filename = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tif")])
        self.reference_image_path.set(filename)

    def browse_comparison_folder(self):
        folder_path = filedialog.askdirectory()
        self.comparison_folder_path.set(folder_path)

    def evaluate_images(self):
        reference_path = self.reference_image_path.get()
        comparison_folder = self.comparison_folder_path.get()

        if not reference_path or not comparison_folder:
            messagebox.showerror("Error", "Please select both reference image and comparison folder.")
            return

        try:
            reference_img = self.load_image(reference_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load reference image: {str(e)}")
            return

        results = []
        total_images = len([f for f in os.listdir(comparison_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif'))])
        processed_images = 0

        for filename in os.listdir(comparison_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif')):
                img_path = os.path.join(comparison_folder, filename)
                try:
                    comparison_img = self.load_image(img_path)
                    metrics = self.calculate_metrics(reference_img, comparison_img)
                    metrics['filename'] = filename
                    results.append(metrics)
                except Exception as e:
                    messagebox.showwarning("Warning", f"Failed to process {filename}: {str(e)}")
                
                processed_images += 1
                self.master.title(f"Processing... {processed_images}/{total_images}")
                self.master.update()

        self.save_results(results)
        messagebox.showinfo("Success", f"Evaluation complete. Processed {processed_images} images. Results saved as 'quality_assessment_results.csv'.")
        self.master.title("Image Quality Assessment Tool")

    def load_image(self, path):
        return cv2.imread(path)

    def calculate_metrics(self, ref_img, comp_img):
        metrics = {}
        
        # Ensure images have the same dimensions
        comp_img = cv2.resize(comp_img, (ref_img.shape[1], ref_img.shape[0]))

        # Convert images to grayscale for some metrics
        ref_gray = cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY)
        comp_gray = cv2.cvtColor(comp_img, cv2.COLOR_BGR2GRAY)

        # Calculate PSNR
        try:
            metrics['PSNR'] = psnr(ref_img, comp_img)
        except Exception as e:
            metrics['PSNR'] = f"Error: {str(e)}"

        # Calculate SSIM
        try:
            metrics['SSIM'] = ssim(ref_gray, comp_gray, data_range=ref_gray.max() - ref_gray.min())
        except Exception as e:
            metrics['SSIM'] = f"Error: {str(e)}"

        # Calculate MSE
        try:
            metrics['MSE'] = np.mean((ref_img.astype(float) - comp_img.astype(float)) ** 2)
        except Exception as e:
            metrics['MSE'] = f"Error: {str(e)}"

        # Calculate NRMSE
        try:
            mse_value = np.mean((ref_img.astype(float) - comp_img.astype(float)) ** 2)
            metrics['NRMSE'] = np.sqrt(mse_value) / (np.max(ref_img) - np.min(ref_img))
        except Exception as e:
            metrics['NRMSE'] = f"Error: {str(e)}"

        # Calculate LPIPS
        if self.lpips_model:
            try:
                ref_tensor = lpips.im2tensor(cv2.cvtColor(ref_img, cv2.COLOR_BGR2RGB))
                comp_tensor = lpips.im2tensor(cv2.cvtColor(comp_img, cv2.COLOR_BGR2RGB))
                metrics['LPIPS'] = float(self.lpips_model(ref_tensor, comp_tensor))
            except Exception as e:
                metrics['LPIPS'] = f"Error: {str(e)}"
        else:
            metrics['LPIPS'] = 'N/A'

        return metrics

    def save_results(self, results):
        with open('quality_assessment_results.csv', 'w', newline='') as csvfile:
            fieldnames = ['filename', 'PSNR', 'SSIM', 'MSE', 'NRMSE', 'LPIPS']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for result in results:
                writer.writerow(result)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageQualityAssessmentTool(root)
    root.mainloop()