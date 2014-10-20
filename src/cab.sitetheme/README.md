# cab.sitetheme

## Plone Website

* `Source code @ GitHub <https://github.com/kreativkombinat/cab.cab>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/cab.cab>`_
* `Documentation @ ReadTheDocs <http://cabcab.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/kreativkombinat/cab.cab>`_

## How it works

This package provides a Diazo Plone theme as an installable Python egg package.
The generated Python package hold the necessary scaffold to kickstart theme
development.

In order to get productive you still need to generate a theme

```bash
$ cd cab.cab/src/cab/cab/resources
$ yo generator-diazotheme

```


## Installation

To install `cab.cab` you simply add ``cab.cab``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `cab.cab` using the Add-ons control panel.


## Configuration

The configuration is done by the package generic setup profile but can be changed by accessing the plone theming control panel
