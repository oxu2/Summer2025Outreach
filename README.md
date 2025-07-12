# Summer 2025 Outreach

## About
Summer 2025 Outreach is a collection of materials, plans, and documentation for organizing and running a summer outreach program during the summer of 2025. This repository includes schedules, presentation slides, promotional content, and relevant communication templates aimed at engaging the community and expanding the program.

## Summer Plan

### Initial Stage
- Students will gain hands-on experience with Python installation and usage, as well as foundational skills in Git, GitHub, and cloud server environments.  
- Students will begin by going through the notebooks in my repository: [Summer2025Outreach Notebooks](https://github.com/oxu2/Summer2025Outreach).  
- The code, created by our labmate Ruiyu Mao, is a simplified version of the Dive into Deep Learning project ([d2l.ai](https://d2l.ai/)). It provides students with a low‐overhead way to become familiar with Python and standard deep learning models.

### Final Project

The final project will serve as a practical component where students apply what they have learned in the outreach program. Below is an overview:

- We may explore the paper **“SafeFix: Targeted Model Repair via Controlled Image Generation”**, which represents an active research direction in our lab and is a project I am primarily responsible for.
- To reduce overhead, we may shrink the dataset and/or use Google Colab so that models can be trained efficiently.
- The goal is to help students understand the **machine learning project pipeline**, and to explore **data-efficient methods** in practical scenarios.
- The project will involve components from:
  - **Computer vision models**
  - **Text-to-image generative models**
  - **Large vision-language models (VLMs)**

####

These topics align closely with current trends in AI research.

#### Related Paper for Reference

> **HiBug: On Human-Interpretable Model Debug**  
> NeurIPS 2023  
> [PDF link](https://proceedings.neurips.cc/paper_files/paper/2023/file/0f53ecc0d36a5d5d3d3e94d42c4b23ca-Paper-Conference.pdf)

## Setup

Follow these steps to create a reproducible Conda environment with Python 3.9 and all required packages.

---

### 1. Install Conda

1. Install Anaconda as we did last before on your own computer. Or download the Miniconda installer for your platform from  
   https://repo.anaconda.com/miniconda/  
2. Run the installer and follow the prompts.  
3. Open a new terminal and verify Conda is available:  
   ```bash
   conda --version
   ```

---

### 2. Create and Activate the Environment

```bash
conda create -n resnet-env python=3.9
conda activate resnet-env
```

---

### 3. Install PyTorch and TorchVision

Following https://pytorch.org/get-started/locally/,
#### CPU version

```bash
pip3 install torch torchvision torchaudio
```


---

### 4. Install Other Dependencies

```bash
conda install numpy matplotlib
```

> **Note:**  
> - `numpy` is required for data indexing and random seeds.  
> - `matplotlib` is optional if you plan to plot training curves.

---

### 5. Verify the Installation

Run this command to confirm versions:

```bash
python -c "import torch, torchvision, numpy; \
print('torch', torch.__version__, \
'torchvision', torchvision.__version__, \
'numpy', numpy.__version__)"
```

---

Once your environment is ready, you can run your training script:

```bash
python train.py
```

## Tentative Schedule

| No. | Date           | Day       | Topic(s)                                                                                                                                    |
|-----|----------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | June 10, 2025  | Tuesday   | introduction; preliminaries; install Python                                                                                                  |
| 2   | June 12, 2025  | Thursday  | use Git, GitHub; introduction to the Dive-into-Deep-Learning book and repository                                                             |
| 3   | June 17, 2025  | Tuesday   | linear-regression; linear-classification; multilayer-perceptrons                                                                             |
| –   | June 19, 2025  | Thursday  | **Juneteenth (no class)**                                                                                                                    |
| 4   | June 24, 2025  | Tuesday   | builders-guide; convolutional-neural-networks; convolutional-modern                                                                          |
| 5   | June 26, 2025  | Thursday  | recurrent-neural-networks; recurrent-modern                                                                                                   |
| 6   | July 1, 2025   | Tuesday   | attention-mechanisms-and-transformers                                                                                                        |
| 7   | July 3, 2025   | Thursday  | optimization; computational-performance; computer-vision                                                                                      |
| 8   | July 8, 2025   | Tuesday   | natural-language-processing-pretraining; natural-language-processing-applications; reinforcement-learning                                     |
| 9   | July 10, 2025  | Thursday  | [HiBug](https://proceedings.neurips.cc/paper_files/paper/2023/file/0f53ecc0d36a5d5d3d3e94d42c4b23ca-Paper-Conference.pdf)  explanation       |
| 10  | July 15, 2025  | Tuesday   | reading gaussian-processes; [HiBug code](https://github.com/cure-lab/HiBug); project part 1: working on Resnet Classification on ImageNet subset       |
| 11  | July 17, 2025  | Thursday  | reading hyperparameter-optimization                                        |
| 12  | July 22, 2025  | Tuesday   | reading generative-adversarial-networks                                                                                                      |
| 13  | July 24, 2025  | Thursday  | reading recommender-systems                                                                                                                  |
| 14  | July 29, 2025  | Tuesday   | Hands-on Project                                                                                                                             |
| 15  | July 31, 2025  | Thursday  | Project presentation                                                                                                                         |



