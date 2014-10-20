# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from ade25.cab.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of ade25.cab into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ade25.cab is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('ade25.cab'))

    def test_uninstall(self):
        """Test if ade25.cab is cleanly uninstalled."""
        self.installer.uninstallProducts(['ade25.cab'])
        self.assertFalse(self.installer.isProductInstalled('ade25.cab'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IAde25CabLayer is registered."""
        from ade25.cab.interfaces import IAde25CabLayer
        from plone.browserlayer import utils
        self.failUnless(IAde25CabLayer in utils.registered_layers())
