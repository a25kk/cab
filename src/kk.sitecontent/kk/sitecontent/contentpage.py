from Acquisition import aq_inner
from AccessControl import Unauthorized

from five import grok
from plone import api

from z3c.form import group, field
from zope import schema
from zope.component import getMultiAdapter

from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from plone.keyring import django_random
from Products.CMFPlone.utils import safe_unicode

from kk.sitecontent import MessageFactory as _


class IContentPage(form.Schema, IImageScaleTraversable):
    """
    Folderish contentpage containing submodules
    """
    headline = schema.TextLine(
        title=_(u"Headline"),
        description=_(u"Override the actual title with a content headline in"
                      u"order to keep the dublin core metadata short and "
                      u"precise"),
        required=False
    )
    text = RichText(
        title=_(u"Body Text"),
        required=False
    )


class ContentPage(Container):
    grok.implements(IContentPage)
    pass


class View(grok.View):
    grok.context(IContentPage)
    grok.require('zope2.View')
    grok.name('view')

