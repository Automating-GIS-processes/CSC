Installing Python + GIS
=======================

**How to start doing GIS with Python on your own computer?**

First step is to install Python and necessary Python modules that are needed to perform various GIS-tasks.
The purpose of this page is to help you out installing Python and various useful GIS modules into your own computer.
Even though it is possible to install Python from their `homepage <https://www.python.org/>`_,
**we highly recommend using** `Anaconda <https://www.continuum.io/anaconda-overview>`_ which is an open source
distribution of the Python and R programming languages for large-scale data processing, predictive analytics,
and scientific computing, that aims to simplify package management and deployment. In short,
it makes life much easier when installing new tools on your Python to play with.

Install Python + GIS on Windows
-------------------------------

Following steps have been tested to work on Windows 7 and 10 with Anaconda3 64 bit, using conda v4.3.29 (30th October 2017).

`Download Anaconda installer (64 bit) <https://www.continuum.io/downloads>`_ for Windows.

Install Anaconda to your computer by double clicking the installer and install it into a directory you want (needs admin rights).
Install it to **all users** and use default settings.

.. note::

    Note for University of Helsinki workers: you need to set the installation location as ``C:\HYapp`` so that it can be used easily by anyone without the need to
    pass admin credentials all the time. If you don't have ``C:\HYapp`` -folder, create one with admin rights.


Test that the Anaconda´s package manage called ``conda`` works by `opening a command prompt as a admin user <http://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/>`_
and running command ``conda --version``.

Install GIS related packages with conda (and pip) by running in command prompt following commands.
Many of the GIS packages are bundled with geopandas, but there are a few that requires separate installation.
As you can see below, many of the GIS packages are available from specific ``channel`` from conda called ``conda-forge``.

.. code:: bash

    # Install Geopandas
    conda install -c conda-forge geopandas

    # Install geoplot
    conda install -c conda-forge geoplot

    # Install osmnx
    conda install -c conda-forge osmnx

    # Install pysal
    conda install -c conda-forge pysal

    # Install contextily
    conda install -c conda-forge contextily

    # Install rasterio
    conda install -c conda-forge rasterio

    # Install rasterstats
    conda install -c conda-forge rasterstats

    # Install pycrs
    pip install git+https://github.com/mullenkamp/PyCRS

    # Install Dash using Pip
    pip install dash==0.19.0  # The core dash backend
    pip install dash-renderer==0.11.1  # The dash front-end
    pip install dash-html-components==0.8.0  # HTML components
    pip install dash-core-components==0.14.0  # Supercharged components
    pip install plotly --upgrade  # Plotly graphing library

Test that everything works
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can test that the installations have worked by running following commands in your IPython console (comes with mini-conda).

.. code:: python

     import geopandas as gpd
     import pysal
     import cartopy
     import geoplot
     import osmnx
     import folium
     import dash
     import rasterio
     import osmnx
     import contextily


If you don't receive any errors, everything should be working!

.. hint::

    It is also possible to install all these packages at once by taking advantage of ``.yml`` environment file
    that is provided by us. Using them requires a few special tricks, :doc:`read more from here <install-using-yml>`.


Install Python + GIS on Linux / Mac
-----------------------------------

**Install Anaconda 3 and add it to system path**

.. code:: bash

    # Download and install Anaconda
    sudo wget https://repo.continuum.io/archive/Anaconda3-5.3.0-Linux-x86_64.sh
    sudo bash Anaconda3-5.3.0-Linux-x86_64.sh

    # Add Anaconda installation permanently to PATH variable
    nano ~/.bashrc

    # Add following line at the end of the file and save (EDIT ACCORDING YOUR INSTALLATION PATH)
    export PATH=$PATH:/PATH_TO_ANACONDA/anaconda3/bin:/PATH_TO_ANACONDA/anaconda3/lib/python3.7/site-packages

**Install Python packages**

Install GIS related packages with conda (and pip) by running in command prompt following commands (in the same order as they are listed):

.. code:: bash

    # Install Geopandas
    conda install -c conda-forge geopandas

    # Install geoplot
    conda install -c conda-forge geoplot

    # Install osmnx
    conda install -c conda-forge osmnx

    # Install pysal
    conda install -c conda-forge pysal

    # Install contextily
    conda install -c conda-forge contextily

    # Install rasterio
    conda install -c conda-forge rasterio

    # Install rasterstats
    conda install -c conda-forge rasterstats

    # Install pycrs
    pip install pycrs

    # Install Dash using Pip
    pip install dash==0.19.0  # The core dash backend
    pip install dash-renderer==0.11.1  # The dash front-end
    pip install dash-html-components==0.8.0  # HTML components
    pip install dash-core-components==0.14.0  # Supercharged components
    pip install plotly --upgrade  # Plotly graphing library

How to find out which conda -command to use when installing a package?
----------------------------------------------------------------------

The easiest way
~~~~~~~~~~~~~~~

The first thing to try when installing a new module ``X`` is to run in a command prompt (as admin) following command (here we try to install a hypothetical
module called X)

.. code::

    conda install X

In most cases this approach works but sometimes you get errors like (example when installing a module called shapely):

.. code::

    C:\WINDOWS\system32>conda install shapely
    Using Anaconda API: https://api.anaconda.org
    Fetching package metadata .........
    Solving package specifications: .
    Error: Package missing in current win-64 channels:
      - shapely

    You can search for packages on anaconda.org with

        anaconda search -t conda shapely

Okey, so conda couldn't find the shapely module from the typical channel it uses for downloading the module.


Alternative way to install if typical doesn't work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How to find a way to install a module if it cannot be installed on a typical way?
Well, the answer is the same is in many other cases nowadays, **Google it!**

Let's find our way to install the Shapely module by typing following query to Google:

.. image:: img/google_query_conda.PNG

Okey, we have different pages showing how to install Shapely using conda package manager.

**Which one of them is the correct one to use?**

We need to check the operating system banners and if you find a logo of the operating system of your computer,
that is the one to use! Thus, in our case the first page that Google gives does not work in Windows but the second one does, as it has Windows logo on it:

.. image:: img/conda_shapely_windows.PNG

From here we can get the correct installation command for conda and it works!

.. image:: img/install_shapely.PNG

You can follow these steps similarly for all of the other Python modules that you are interested to install.


