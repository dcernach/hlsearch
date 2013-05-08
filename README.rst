=========
hlsearch: Hero Lab file search
=========

About
-----

``hlsearch`` is a quick search utility for `Hero Lab <http://wolflair.com/index.php?context=hero_lab>`_
which will search through a directory of .por and .stock files and parse through them looking to match the creature
names inside them against supplied user data.

.. image:: http://tarsis.org/images/hlsearch.png


Installation
------------

The application is a simple binary that you can download and run.

`Windows binary <http://tarsis.org/builds/hlsearch.exe>`_

`Linux 32bit binary <http://tarsis.org/builds/hlsearch.i386>`_

`Linux 64bit binary <http://tarsis.org/builds/hlsearch.amd64>`_


Installation from Source
------------

Install both Python_ 2.7 and PyQt4_.

Download_ and unzip the app into a folder.

Running from Source
-------

On Windows just double click the hlsearch.py file. Under Linux run:

    python hlsearch.py

Usage
-----

Select the directory where you have your por or stock files stored. Then put in a name to search for and click
on Search Files. It may take awhile for it to search through all the files.

For the search field you can use Python compatible regex.

License
-------

``hlsearch`` is released under the GPLv3 license.


.. _python: http://www.python.org/
.. _download: http://hg.tarsis.org/hlsearch/archive/tip.zip
.. _pyqt4: http://www.riverbankcomputing.com/software/pyqt/download
