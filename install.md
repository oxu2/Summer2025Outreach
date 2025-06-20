# Installation
:label:`chap_installation`

In order to get up and running,
we will need an environment for running Python,
the Jupyter Notebook, the relevant libraries,
and the code needed to run the book itself.

## Installing Anaconda

Your simplest option is to install
[Anaconda](https://www.anaconda.com/docs/getting-started/anaconda/install#mac-os-command-line-installer).
Note that the Python 3.x version is required.
You can skip the following steps
if your machine already has conda installed.

Follow the `Command Prompt` installation guide on that website.


Next, initialize the shell so we can run `conda` directly.

```bash
conda init
```


Then close and reopen your current shell.
You should be able to create
a new environment as follows:

```bash
conda create --name d2l python=3.9 -y
```


Now we can activate the `d2l` environment:

```bash
conda activate d2l
```


## Installing the Deep Learning Framework and the `d2l` Package

Before installing any deep learning framework,
please first check whether or not
you have proper GPUs on your machine
(the GPUs that power the display
on a standard laptop are not relevant for our purposes).
For example,
if your computer has NVIDIA GPUs and has installed [CUDA](https://developer.nvidia.com/cuda-downloads),
then you are all set.
If your machine does not house any GPU,
there is no need to worry just yet.
Your CPU provides more than enough horsepower
to get you through the first few chapters.
Just remember that you will want to access GPUs
before running larger models.


:begin_tab:`mxnet`

To install a GPU-enabled version of MXNet,
we need to find out what version of CUDA you have installed.
You can check this by running `nvcc --version`
or `cat /usr/local/cuda/version.txt`.
Assume that you have installed CUDA 11.2,
then execute the following command:

```bash
# For macOS and Linux users
pip install mxnet-cu112==1.9.1

# For Windows users
pip install mxnet-cu112==1.9.1 -f https://dist.mxnet.io/python
```


You may change the last digits according to your CUDA version, e.g., `cu101` for
CUDA 10.1 and `cu90` for CUDA 9.0.


If your machine has no NVIDIA GPUs
or CUDA,
you can install the CPU version
as follows:

```bash
pip install mxnet==1.9.1
```


:end_tab:


:begin_tab:`pytorch`

You can install PyTorch (the specified versions are tested at the time of writing) with either CPU or GPU support as follows:

```bash
pip install torch==2.0.0 torchvision==0.15.1
```


:end_tab:

:begin_tab:`tensorflow`
You can install TensorFlow with either CPU or GPU support as follows:

```bash
pip install tensorflow==2.12.0 tensorflow-probability==0.20.0
```


:end_tab:

:begin_tab:`jax`
You can install JAX and Flax with either CPU or GPU support as follows:

```bash
# GPU
pip install "jax[cuda11_pip]==0.4.13" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html flax==0.7.0
```


If your machine has no NVIDIA GPUs
or CUDA,
you can install the CPU version
as follows:

```bash
# CPU
pip install "jax[cpu]==0.4.13" flax==0.7.0
```


:end_tab:


Our next step is to install
the `d2l` package that we developed
in order to encapsulate
frequently used functions and classes
found throughout this book:

```bash
pip install d2l==1.0.3
```


## Downloading and Running the Code

Next, you will want to download the notebooks
so that you can run each of the book's code blocks.
Simply click on the "Notebooks" tab at the top
of any HTML page on [the D2L.ai website](https://d2l.ai/)
to download the code and then unzip it.
Alternatively, you can fetch the notebooks
from the command line as follows:

:begin_tab:`mxnet`

```bash
mkdir d2l-en && cd d2l-en
curl https://d2l.ai/d2l-en-1.0.3.zip -o d2l-en.zip
unzip d2l-en.zip && rm d2l-en.zip
cd mxnet
```


:end_tab:


:begin_tab:`pytorch`

```bash
mkdir d2l-en && cd d2l-en
curl https://d2l.ai/d2l-en-1.0.3.zip -o d2l-en.zip
unzip d2l-en.zip && rm d2l-en.zip
cd pytorch
```


:end_tab:

:begin_tab:`tensorflow`

```bash
mkdir d2l-en && cd d2l-en
curl https://d2l.ai/d2l-en-1.0.3.zip -o d2l-en.zip
unzip d2l-en.zip && rm d2l-en.zip
cd tensorflow
```


:end_tab:

:begin_tab:`jax`

```bash
mkdir d2l-en && cd d2l-en
curl https://d2l.ai/d2l-en-1.0.3.zip -o d2l-en.zip
unzip d2l-en.zip && rm d2l-en.zip
cd jax
```


:end_tab:

If you do not already have `unzip` installed, first run `sudo apt-get install unzip`.
Now we can start the Jupyter Notebook server by running:

```bash
jupyter notebook
```


At this point, you can open http://localhost:8888
(it may have already opened automatically) in your web browser.
Then we can run the code for each section of the book.
Whenever you open a new command line window,
you will need to execute `conda activate d2l`
to activate the runtime environment
before running the D2L notebooks,
or updating your packages
(either the deep learning framework
or the `d2l` package).
To exit the environment,
run `conda deactivate`.


:begin_tab:`mxnet`
[Discussions](https://discuss.d2l.ai/t/23)
:end_tab:

:begin_tab:`pytorch`
[Discussions](https://discuss.d2l.ai/t/24)
:end_tab:

:begin_tab:`tensorflow`
[Discussions](https://discuss.d2l.ai/t/436)
:end_tab:

:begin_tab:`jax`
[Discussions](https://discuss.d2l.ai/t/17964)
:end_tab:
