
# Batch Image Quality Assessment Tool (BatchIQA)

A user-friendly application for assessing the quality of images from one whole folder by comparing them to a reference image using multiple metrics.

这是一款用户友好型应用程序，可使用多种指标将一整个文件夹下的图像与参考图像进行比较，从而评估图像质量。


<div style="display: flex; justify-content: center; align-items: center; height: 200px;">
  <img src="[https://github.com/Mnster00/ImageBatchCropping/blob/main/2.png](https://github.com/Mnster00/BatchIQA/blob/main/figs/1.png)" style="max-width: 80%;">
</div>


## Features

- Easy-to-use graphical interface
- Batch processing of multiple images
- Calculates multiple image quality metrics:
  - PSNR (Peak Signal-to-Noise Ratio)
  - SSIM (Structural Similarity Index)
  - MSE (Mean Squared Error)
  - NRMSE (Normalized Root Mean Square Error)
  - LPIPS (Learned Perceptual Image Patch Similarity)
- Results saved in CSV format for easy analysis

## System Requirements

- Windows 

## Download and Installation

1. Go to the [Releases](https://github.com/yourusername/image-quality-assessment-tool/releases) page of this repository.
2. Download the latest `ImageQualityAssessmentTool.zip` file.

## Usage

1. Double-click on `ImageQualityAssessmentTool.exe` to launch the application.
2. In the application window:
   - Click "Browse" next to "Reference Image" to select your reference image.
   - Click "Browse" next to "Comparison Folder" to select the folder containing images to be compared.
   - Click "Evaluate" to start the assessment process.
3. Once complete, a CSV file named `quality_assessment_results.csv` will be saved in the same directory as the executable.

<div style="display: flex; justify-content: center; align-items: center; height: 200px;">
  <img src="[https://github.com/Mnster00/ImageBatchCropping/blob/main/2.png](https://github.com/Mnster00/BatchIQA/blob/main/figs/1.png)" style="max-width: 80%;">
</div>

<div style="display: flex; justify-content: center; align-items: center; height: 200px;">
  <img src="[https://github.com/Mnster00/ImageBatchCropping/blob/main/2.png](https://github.com/Mnster00/BatchIQA/blob/main/figs/2.png)" style="max-width: 80%;">
</div>

<div style="display: flex; justify-content: center; align-items: center; height: 200px;">
  <img src="[https://github.com/Mnster00/ImageBatchCropping/blob/main/2.png](https://github.com/Mnster00/BatchIQA/blob/main/figs/3.png)" style="max-width: 80%;">
</div>

<div style="display: flex; justify-content: center; align-items: center; height: 200px;">
  <img src="[https://github.com/Mnster00/ImageBatchCropping/blob/main/2.png](https://github.com/Mnster00/BatchIQA/blob/main/figs/5.png)" style="max-width: 80%;">
</div>

## Understanding the Metrics

- **PSNR**: Higher values indicate better quality. Typical values are between 20 and 40 dB.
- **SSIM**: Ranges from -1 to 1. Higher values indicate greater structural similarity.
- **MSE**: Lower values indicate less difference between images.
- **NRMSE**: Normalized version of RMSE. Lower values indicate better quality.
- **LPIPS**: Ranges from 0 to 1. Lower values indicate greater perceptual similarity.


