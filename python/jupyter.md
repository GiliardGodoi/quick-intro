# Jupyter Quick Tips

Jupyter, IPython and IPythonKernel are three differents things.

## Register a Kernel for a different enviroment

[Link](https://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments) for documentation.

    source activate myenv
    conda install pip
    conda install ipykernel

    python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
