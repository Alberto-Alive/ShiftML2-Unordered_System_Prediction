#!/usr/bin/env python
# coding: utf-8

# # Scripts
# 
# You can also create content with Jupyter Notebooks. This means that you can include
# code blocks and their outputs in your book.
# 
# ## Markdown + notebooks
# 
# As it is markdown, you can embed images, HTML, etc into your posts!
# 
# ![](https://myst-parser.readthedocs.io/en/latest/_static/logo-wide.svg)
# 
# You can also $add_{math}$ and
# 
# $$
# math^{blocks}
# $$
# 
# or
# 
# $$
# \begin{aligned}
# \mbox{mean} la_{tex} \\ \\
# math blocks
# \end{aligned}
# $$
# 
# But make sure you \$Escape \$your \$dollar signs \$you want to keep!
# 
# ## MyST markdown
# 
# MyST markdown works in Jupyter Notebooks as well. For more information about MyST markdown, check
# out [the MyST guide in Jupyter Book](https://jupyterbook.org/content/myst.html),
# or see [the MyST markdown documentation](https://myst-parser.readthedocs.io/en/latest/).
# 
# ## Code blocks and outputs
# 
# Jupyter Book will also embed your code blocks and output in your book.
# For example, here's some sample Matplotlib code:

# In[1]:


from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
plt.ion()


# In[2]:


# Name                    Version                   Build  Channel
alabaster                 0.7.13                   pypi_0    pypi
anyio                     3.6.2                    pypi_0    pypi
argon2-cffi               21.3.0                   pypi_0    pypi
argon2-cffi-bindings      21.2.0                   pypi_0    pypi
arrow                     1.2.3                    pypi_0    pypi
ase                       3.22.1             pyhd8ed1ab_1    conda-forge
asttokens                 2.1.0              pyhd8ed1ab_0    conda-forge
attrs                     21.4.0                   pypi_0    pypi
babel                     2.11.0                   pypi_0    pypi
backcall                  0.2.0              pyh9f0ad1d_0    conda-forge
backports                 1.0                        py_2    conda-forge
backports.functools_lru_cache 1.6.4              pyhd8ed1ab_0    conda-forge
beautifulsoup4            4.11.2                   pypi_0    pypi
bleach                    6.0.0                    pypi_0    pypi
brotli                    1.0.9                hcfcfb64_8    conda-forge
brotli-bin                1.0.9                hcfcfb64_8    conda-forge
bzip2                     1.0.8                h8ffe710_4    conda-forge
ca-certificates           2022.9.24            h5b45459_0    conda-forge
certifi                   2022.9.24          pyhd8ed1ab_0    conda-forge
cffi                      1.15.1                   pypi_0    pypi
charset-normalizer        3.0.1                    pypi_0    pypi
click                     8.1.3           win_pyhd8ed1ab_2    conda-forge
colorama                  0.4.6              pyhd8ed1ab_0    conda-forge
comm                      0.1.2                    pypi_0    pypi
contourpy                 1.0.6           py310h232114e_0    conda-forge
cycler                    0.11.0             pyhd8ed1ab_0    conda-forge
debugpy                   1.6.3           py310h00ffb61_1    conda-forge
decorator                 5.1.1              pyhd8ed1ab_0    conda-forge
defusedxml                0.7.1                    pypi_0    pypi
docutils                  0.17.1                   pypi_0    pypi
entrypoints               0.4                pyhd8ed1ab_0    conda-forge
executing                 1.2.0              pyhd8ed1ab_0    conda-forge
fastjsonschema            2.16.3                   pypi_0    pypi
flask                     2.2.2              pyhd8ed1ab_0    conda-forge
fonttools                 4.38.0          py310h8d17308_1    conda-forge
fqdn                      1.5.1                    pypi_0    pypi
freetype                  2.12.1               h546665d_0    conda-forge
ghp-import                2.1.0                    pypi_0    pypi
gitdb                     4.0.10                   pypi_0    pypi
gitpython                 3.1.31                   pypi_0    pypi
greenlet                  2.0.2                    pypi_0    pypi
idna                      3.4                      pypi_0    pypi
imagesize                 1.4.1                    pypi_0    pypi
importlib-metadata        5.0.0              pyha770c72_1    conda-forge
intel-openmp              2022.1.0          h57928b3_3787    conda-forge
ipykernel                 6.20.2                   pypi_0    pypi
ipython                   8.6.0              pyh08f2357_1    conda-forge
ipython-genutils          0.2.0                    pypi_0    pypi
ipywidgets                7.7.3                    pypi_0    pypi
isoduration               20.11.0                  pypi_0    pypi
itsdangerous              2.1.2              pyhd8ed1ab_0    conda-forge
jedi                      0.18.1             pyhd8ed1ab_2    conda-forge
jinja2                    3.1.2              pyhd8ed1ab_1    conda-forge
joblib                    1.2.0                    pypi_0    pypi
jpeg                      9e                   h8ffe710_2    conda-forge
jsonpointer               2.3                      pypi_0    pypi
jsonschema                4.17.3                   pypi_0    pypi
jupyter-book              0.13.2                   pypi_0    pypi
jupyter-cache             0.4.3                    pypi_0    pypi
jupyter-core              5.2.0                    pypi_0    pypi
jupyter-events            0.6.3                    pypi_0    pypi
jupyter-server            2.3.0                    pypi_0    pypi
jupyter-server-mathjax    0.2.6                    pypi_0    pypi
jupyter-server-terminals  0.4.4                    pypi_0    pypi
jupyter-sphinx            0.3.2                    pypi_0    pypi
jupyter_client            7.4.7              pyhd8ed1ab_0    conda-forge
jupyterlab-pygments       0.2.2                    pypi_0    pypi
jupyterlab-widgets        1.1.2                    pypi_0    pypi
kiwisolver                1.4.4           py310h232114e_1    conda-forge
latexcodec                2.0.1                    pypi_0    pypi
lcms2                     2.14                 h90d422f_0    conda-forge
lerc                      4.0.0                h63175ca_0    conda-forge
libblas                   3.9.0              16_win64_mkl    conda-forge
libbrotlicommon           1.0.9                hcfcfb64_8    conda-forge
libbrotlidec              1.0.9                hcfcfb64_8    conda-forge
libbrotlienc              1.0.9                hcfcfb64_8    conda-forge
libcblas                  3.9.0              16_win64_mkl    conda-forge
libdeflate                1.14                 hcfcfb64_0    conda-forge
libffi                    3.4.2                h8ffe710_5    conda-forge
liblapack                 3.9.0              16_win64_mkl    conda-forge
libpng                    1.6.38               h19919ed_0    conda-forge
libsodium                 1.0.18               h8d14728_1    conda-forge
libsqlite                 3.40.0               hcfcfb64_0    conda-forge
libtiff                   4.4.0                h8e97e67_4    conda-forge
libwebp-base              1.2.4                h8ffe710_0    conda-forge
libxcb                    1.13              hcd874cb_1004    conda-forge
libzlib                   1.2.13               hcfcfb64_4    conda-forge
linkify-it-py             2.0.0                    pypi_0    pypi
lxml                      4.9.2                    pypi_0    pypi
m2w64-gcc-libgfortran     5.3.0                         6    conda-forge
m2w64-gcc-libs            5.3.0                         7    conda-forge
m2w64-gcc-libs-core       5.3.0                         7    conda-forge
m2w64-gmp                 6.1.0                         2    conda-forge
m2w64-libwinpthread-git   5.0.0.4634.697f757               2    conda-forge
markdown-it-py            1.1.0                    pypi_0    pypi
markupsafe                2.1.1           py310h8d17308_2    conda-forge
matplotlib-base           3.6.2           py310h51140c5_0    conda-forge
matplotlib-inline         0.1.6              pyhd8ed1ab_0    conda-forge
mdit-py-plugins           0.2.8                    pypi_0    pypi
mistune                   0.8.4                    pypi_0    pypi
mkl                       2022.1.0           h6a75c08_874    conda-forge
msys2-conda-epoch         20160418                      1    conda-forge
munkres                   1.1.4              pyh9f0ad1d_0    conda-forge
myst-nb                   0.13.2                   pypi_0    pypi
myst-parser               0.15.2                   pypi_0    pypi
nbclassic                 0.5.2                    pypi_0    pypi
nbclient                  0.5.13                   pypi_0    pypi
nbconvert                 6.5.4                    pypi_0    pypi
nbdime                    3.1.1                    pypi_0    pypi
nbformat                  5.7.3                    pypi_0    pypi
nest-asyncio              1.5.6              pyhd8ed1ab_0    conda-forge
notebook                  6.5.2                    pypi_0    pypi
notebook-shim             0.2.2                    pypi_0    pypi
numpy                     1.23.5          py310h4a8f9c9_0    conda-forge
openjpeg                  2.5.0                hc9384bd_1    conda-forge
openssl                   3.0.7                hcfcfb64_0    conda-forge
packaging                 21.3               pyhd8ed1ab_0    conda-forge
pandas                    1.5.2                    pypi_0    pypi
pandocfilters             1.5.0                    pypi_0    pypi
parso                     0.8.3              pyhd8ed1ab_0    conda-forge
pickleshare               0.7.5                   py_1003    conda-forge
pillow                    9.2.0           py310hd4fb230_3    conda-forge
pip                       22.3.1             pyhd8ed1ab_0    conda-forge
platformdirs              2.5.2              pyhd8ed1ab_1    conda-forge
prometheus-client         0.16.0                   pypi_0    pypi
prompt-toolkit            3.0.32             pyha770c72_0    conda-forge
psutil                    5.9.4           py310h8d17308_0    conda-forge
pthread-stubs             0.4               hcd874cb_1001    conda-forge
pure_eval                 0.2.2              pyhd8ed1ab_0    conda-forge
pybtex                    0.24.0                   pypi_0    pypi
pybtex-docutils           1.0.2                    pypi_0    pypi
pycparser                 2.21                     pypi_0    pypi
pydata-sphinx-theme       0.8.1                    pypi_0    pypi
pygments                  2.13.0             pyhd8ed1ab_0    conda-forge
pyparsing                 3.0.9              pyhd8ed1ab_0    conda-forge
pyrsistent                0.19.3                   pypi_0    pypi
python                    3.10.6          hcf16a7b_0_cpython    conda-forge
python-dateutil           2.8.2              pyhd8ed1ab_0    conda-forge
python-json-logger        2.0.7                    pypi_0    pypi
python_abi                3.10                    2_cp310    conda-forge
pytz                      2022.7                   pypi_0    pypi
pyvirtualdisplay          3.0                      pypi_0    pypi
pywin32                   304             py310h00ffb61_2    conda-forge
pywinpty                  2.0.10                   pypi_0    pypi
pyyaml                    6.0                      pypi_0    pypi
pyzmq                     24.0.1          py310hcd737a0_1    conda-forge
requests                  2.28.2                   pypi_0    pypi
rfc3339-validator         0.1.4                    pypi_0    pypi
rfc3986-validator         0.1.1                    pypi_0    pypi
scikit-learn              1.2.1                    pypi_0    pypi
scipy                     1.9.3           py310h578b7cb_2    conda-forge
seaborn                   0.12.2                   pypi_0    pypi
send2trash                1.8.0                    pypi_0    pypi
setuptools                65.5.1             pyhd8ed1ab_0    conda-forge
shiftml2                  1.0.0                    pypi_0    pypi
six                       1.16.0             pyh6c4a22f_0    conda-forge
skcosmo                   0.1.2                    pypi_0    pypi
smmap                     5.0.0                    pypi_0    pypi
sniffio                   1.3.0                    pypi_0    pypi
snowballstemmer           2.2.0                    pypi_0    pypi
soprano                   0.8.13                   pypi_0    pypi
soupsieve                 2.4                      pypi_0    pypi
sphinx                    4.5.0                    pypi_0    pypi
sphinx-book-theme         0.3.3                    pypi_0    pypi
sphinx-comments           0.0.3                    pypi_0    pypi
sphinx-copybutton         0.5.1                    pypi_0    pypi
sphinx-design             0.1.0                    pypi_0    pypi
sphinx-external-toc       0.3.1                    pypi_0    pypi
sphinx-jupyterbook-latex  0.5.2                    pypi_0    pypi
sphinx-multitoc-numbering 0.1.3                    pypi_0    pypi
sphinx-thebe              0.2.1                    pypi_0    pypi
sphinx-togglebutton       0.3.2                    pypi_0    pypi
sphinxcontrib-applehelp   1.0.4                    pypi_0    pypi
sphinxcontrib-bibtex      2.5.0                    pypi_0    pypi
sphinxcontrib-devhelp     1.0.2                    pypi_0    pypi
sphinxcontrib-htmlhelp    2.0.1                    pypi_0    pypi
sphinxcontrib-jsmath      1.0.1                    pypi_0    pypi
sphinxcontrib-qthelp      1.0.3                    pypi_0    pypi
sphinxcontrib-serializinghtml 1.1.5                    pypi_0    pypi
sqlalchemy                1.4.46                   pypi_0    pypi
stack_data                0.6.1              pyhd8ed1ab_0    conda-forge
tbb                       2021.7.0             h91493d7_0    conda-forge
terminado                 0.17.1                   pypi_0    pypi
threadpoolctl             3.1.0                    pypi_0    pypi
tinycss2                  1.2.1                    pypi_0    pypi
tk                        8.6.12               h8ffe710_0    conda-forge
tornado                   6.2             py310h8d17308_1    conda-forge
traitlets                 5.9.0                    pypi_0    pypi
tzdata                    2022f                h191b570_0    conda-forge
uc-micro-py               1.0.1                    pypi_0    pypi
ucrt                      10.0.22621.0         h57928b3_0    conda-forge
unicodedata2              15.0.0          py310h8d17308_0    conda-forge
uri-template              1.2.0                    pypi_0    pypi
urllib3                   1.26.14                  pypi_0    pypi
vc                        14.3                 h3d8a991_9    conda-forge
vs2015_runtime            14.32.31332          h1d6e394_9    conda-forge
wcwidth                   0.2.5              pyh9f0ad1d_2    conda-forge
webcolors                 1.12                     pypi_0    pypi
webencodings              0.5.1                    pypi_0    pypi
websocket-client          1.5.1                    pypi_0    pypi
werkzeug                  2.2.2              pyhd8ed1ab_0    conda-forge
wheel                     0.38.4             pyhd8ed1ab_0    conda-forge
widgetsnbextension        3.6.2                    pypi_0    pypi
xorg-libxau               1.0.9                hcd874cb_0    conda-forge
xorg-libxdmcp             1.1.3                hcd874cb_0    conda-forge
xz                        5.2.6                h8d14728_0    conda-forge
zeromq                    4.3.4                h0e60522_1    conda-forge
zipp                      3.10.0             pyhd8ed1ab_0    conda-forge
zstd                      1.5.2                h7755175_4    conda-forge


# In[ ]:


# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot']);


# There is a lot more that you can do with outputs (such as including interactive outputs)
# with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)
