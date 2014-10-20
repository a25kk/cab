# ade25.sitetheme

## Buildout based Website

* `Source code @ GitHub <https://github.com/kreativkombinat/ade25.cab>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/ade25.cab>`_
* `Documentation @ ReadTheDocs <http://ade25cab.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/kreativkombinat/ade25.cab>`_

## How it works

This package provides a Diazo Plone theme as an installable Python egg package.
The generated Python package hold the necessary scaffold to kickstart theme
development.

In order to get productive you still need to generate a theme

```bash
$ cd ade25.cab/src/ade25/cab/resources
$ yo generator-diazotheme

```


## Installation

To install `ade25.cab` you simply add ``ade25.cab``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `ade25.cab` using the Add-ons control panel.


## Configuration

The configuration is done by the package generic setup profile but can be changed by accessing the plone theming control panel
