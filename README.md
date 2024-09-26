
# Batch Image Quality Assessment Tool (BatchIQA)

A user-friendly application for assessing the quality of images by comparing them to a reference image using multiple metrics.

![Image Quality Assessment Tool Interface](path/to/screenshot.png)

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
3. Extract the ZIP file to your preferred location on your computer.

## Usage

1. Double-click on `ImageQualityAssessmentTool.exe` to launch the application.
2. In the application window:
   - Click "Browse" next to "Reference Image" to select your reference image.
   - Click "Browse" next to "Comparison Folder" to select the folder containing images to be compared.
   - Click "Evaluate" to start the assessment process.
3. Once complete, a CSV file named `quality_assessment_results.csv` will be saved in the same directory as the executable.

## Understanding the Metrics

- **PSNR**: Higher values indicate better quality. Typical values are between 20 and 40 dB.
- **SSIM**: Ranges from -1 to 1. Higher values indicate greater structural similarity.
- **MSE**: Lower values indicate less difference between images.
- **NRMSE**: Normalized version of RMSE. Lower values indicate better quality.
- **LPIPS**: Ranges from 0 to 1. Lower values indicate greater perceptual similarity.


