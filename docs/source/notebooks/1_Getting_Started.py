# ---
# jupyter:
#   jupytext:
#     cell_markers: '"""'
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
"""
# Welcome

This document provides a general overview of `OpenSees_Model_Generator (osmg)`.

Opensees_Model_Generator is a python module aimed to simplify the definition of 3D models in OpenSees by automating various "offline calculations", such as orienting line elements in 3D space,  subdividing line elements, distributing loads based on tributary area analysis, and other such operations. The module aims to promote the use of OpenSees for research applications and form a community of researchers who benefit from its capabilities and contribute to its development.

The source code of this module should be thought of as a higher-level interface to OpenSees.
Users of the module are expected to understand the source code and be willing to make changes to it to meet their goals.

## Workflow

The general workflow enabled by the module is the following:
1. Instantiate model objects and define their components
2. Perform preprocessing operations
3. Define load_case and analysis objects
4. Run the analyses
5. Post-process the analysis results

Actual interaction with OpenSees only happens at step #4.

## Install

It is recommended to use a virtual environment to manage the dependencies of this module. I use Anaconda.

Here is how to [install Aanaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).



### Install from PyPI

```
# create a conda environment
$ conda create --name your_env_name_here python=3.11
$ conda activate your_env_name_here
$ python -m pip install osmg
```

Optional:
In case you would like to run tributary area analyses for load distribution calculations, `scikit-geometry` needs to be installed.
```
$ conda install scikit-geometry -c conda-forge
```


### Development mode

Alternatively, if you plan to make changes to the code, installing osmg in development mode is recommended.
This is how it is done.
```
$ mkdir parent_directory_where_you_would_like_to_have_osmg
$ cd parent_directory_where_you_would_like_to_have_osmg
$ git clone https://github.com/ioannis-vm/OpenSees_Model_Generator
$ cd OpenSees_Model_Generator
$ conda create --name your_env_name_here python=3.9
$ conda activate your_env_name_here
$ python -m pip install -r requirements_dev.txt
$ conda install scikit-geometry -c conda-forge
$ python -m pip install -e .
```

### Units
At the moment, the following unit options are available:

Imperial (default)

| Quantity | Unit |
| --- | --- |
| Length | in |
| Force  | lb |
| Weight | lb/(in/s2) |

Metric

| Quantity | Unit |
| --- | --- |
| Length | m |
| Force  | kN |
| Weight | kg |

Well, metric might not work as expected for a while. Making sure it does is on my TODO list. Check your results.

### IDE or Jupyter Notebooks?
I prefer using Emacs as my IDE and working directly with `.py` files. Jupyter notebooks can be used instead, as in these example files.

The benefit of using an IDE and `.py` files is the added ability to set up an argument parser and coordinate analyses from the command line. `.py` files also work much better with version control. The benefit of jupyter notebooks is a somewhat more interactive experience, integrated plots, and markdown integration, but the lack of convenient version-control and Emacs key bindings is a deal-breaker for me.

An excellent IDE that I used in the past is [Spyder](https://www.spyder-ide.org/).

## Tips
How to make sense of all this code?


To figure out the required syntax, these example files and the documentation of the module will be helpful.
For a deep-dive into the execution steps, other than reading the source files and the docstrings, an effective way is to run the examples using [the python debugger](https://docs.python.org/3/library/pdb.html). Just add
```
import pdb
pdb.set_trace()
```
at any line where you would like to stop the execution, and then follow the execution step by step. This is another instance where an IDE can be more effective than jupyter notebooks. There is also pydoc for offline documentation. On the terminal, try:

```
pydoc osmg
pydoc osmg.model.Model
pydoc numpy.array
```

Taking notes in the process might also help.
"""
