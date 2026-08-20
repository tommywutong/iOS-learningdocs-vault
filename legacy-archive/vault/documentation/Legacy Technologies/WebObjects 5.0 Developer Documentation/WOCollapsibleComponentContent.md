---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOCollapsibleCmpntCntnt.html
archived_at: '2026-07-15T08:14:40.628520Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOCollapsibleComponentContent

## Component Description

The WOCollapsibleComponentContent component allows the user
to display (expand) or hide (collapse) the content (that is, everything
between the `<WEBOBJECT...> and </WEBOBJECT...>` tags
in the template file). When the content is collapsed, it is replaced
with an image, which defaults to ![[image: Art/WOExtWOCCCClosedIcon.gif]](Art/WOExtWOCCCClosedIcon.gif)
. Clicking
the image expands the content. When the content is expanded, it
is displayed below an image, which defaults to ![[image: Art/WOExtWOCCCOpenedIcon.gif]](Art/WOExtWOCCCOpenedIcon.gif)
.
Clicking the image collapses the content.

![[image: Art/WOExtWOCCCClosed.gif]](Art/WOExtWOCCCClosed.gif)
![[image: Art/WOExtWOCCCOpened.gif]](Art/WOExtWOCCCOpened.gif)

This component can be embedded within a WOForm. When the WOCollapsibleComponentContent contains
form fields that are bound to an enterprise object's attributes,
the HTML element the user clicks to collapse the content must be
a submit button. This ensures that the values the user types into these
fields get stored in the enterprise object upon collapse. If the
HTML element the user clicks is a hyperlink, the enterprise object's
attributes are not updated when the user collapses the content and
the form field values will not reappear when the user expands the
content again. The `submitActionName` binding
determines the whether the HTML element that collapses the content
is a hyperlink or a submit button.

## Synopsis

WOCollapsibleComponentContent { [condition=_aBoolean_;]
[visibility=_aBoolean_;]
[openedImageFileName=_aPath_;]
[closedImageFileName=_aPath_;] [framework=_aString_;]
[openedLabel=_aString_;]
[closedLabel=_aString_;] [submitActionName=_anActionName_;]
};

## Bindings

**condition**
: A flag to indicate whether the component is initially
expanded (YES) or collapsed (NO).

**visibility**
: The current state of expansion. This attributed is updated
each time the component is expanded or collapsed.

**openedImageFileName**
: The file name for an active image displayed above the
expanded content. The user clicks this image to collapse the content.
WebObjects assumes the image resides in the WebServerResources directory
of the framework containing the image (see the `framework` attribute.)
If this attribute is not defined, WOCollapsibleComponentContent
displays ![[image: Art/WOExtWOCCCOpenedIcon.gif]](Art/WOExtWOCCCOpenedIcon.gif)
.

**closedImageFileName**
: The filename for an active image displayed when the
content is collapsed. The user clicks this image to expand the content.
WebObjects assumes the image resides in the WebServerResources directory
of the framework containing the image (see the `framework` attribute.)
If this attribute is not defined, WOCollapsibleComponentContent
displays ![[image: Art/WOExtWOCCCClosedIcon.gif]](Art/WOExtWOCCCClosedIcon.gif)
.

**framework**
: The framework `openedImageFileName` and `closedImageFileName` come
from. Defaults to the application.

**openedLabel**
: A label displayed above the expanded content.

**closedLabel**
: A label displayed next to the collapsed content.

**submitActionName**
: The name of an action that is called upon collapse.
This attribute functions only when the WOCollapsibleComponentContent
component is embedded within a WOForm. If `submitActionName` is
not defined or is set to `null`, the
HTML element that expands the content is a hyperlink. Otherwise
the it is a submit button. If you want to expand the content with
a submit button, but don't want it to invoke an action, set this
attribute to the empty string (`""`).

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
