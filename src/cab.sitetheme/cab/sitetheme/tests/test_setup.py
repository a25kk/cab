# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from cab.cab.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of cab.cab into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if cab.cab is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('cab.cab'))

    def test_uninstall(self):
        """Test if cab.cab is cleanly uninstalled."""
        self.installer.uninstallProducts(['cab.cab'])
        self.assertFalse(self.installer.isProductInstalled('cab.cab'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICabCabLayer is registered."""
        from cab.cab.interfaces import ICabCabLayer
        from plone.browserlayer import utils
        self.failUnless(ICabCabLayer in utils.registered_layers())
