---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/JSImageFlyover.html
archived_at: '2026-07-15T08:14:39.655172Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# JSImageFlyover

## Component Description

The JSImageFlyover appears in the browser as an active image
which changes to another image when the mouse pointer hovers over
it.

## Synopsis

JSImageFlyover { action=_anAction_;
| javaScriptFunction=_aURL_; | pageName=_pageName_;
selectedImage=_selectedImageName_;
unselectedImage=_unselectedImageName_;
[framework=_frameworkName_;]
[targetWindow=_windowName_;] };

## Bindings

**action**
: The action method performed when the user clicks the
image.

**javaScriptFunction**
: Java Script code executed when the user clicks the image.

**pageName**
: The WOComponent displayed when the user clicks the image.

**selectedImage**
: The image displayed when the mouse pointer is hovering
over it.

**unselectedImage**
: The image displayed when the mouse pointer is not hovering
over it.

**framework**
: The framework containing the image. Defaults to the
application.

**targetWindow**
: The name of the window in which the new page is displayed
when the user clicks on the image.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
