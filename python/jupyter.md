# Jupyter commands

## Creating a kernel specification

Pretend we have a conda environment called `lab`

```
(base)$ conda activate lab
(lab)$ conda install ipykernel
(lab)$ ipython kernel install --user --name=<any_name_for_kernel>
(lab)$ conda deactivate
```

## Listing kernels

```
jupyter kernelspec list
```

## Removing a kernel

```
jupyter kernelspec remove <kernel-name>
```
