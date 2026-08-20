---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/JSTextFlyover.html
archived_at: '2026-07-15T08:14:39.686904Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# JSTextFlyover

## Component Description

The JSTextFlyover appears in the browser as a hyperlink containing
text that changes color when the mouse pointer hovers over it.

## Synopsis

JSTextFlyover { [action=_anAction_;
| pageName=_pageName_;] string=aString;
selectedColor=_selectedHexString_;
unselectedColor=_unselectedHexString_;
[targetWindow=_windowName_;]
};

## Bindings

**action**
: Action method invoked when the user clicks the hyperlink.

**pageName**
: Name of the WOComponent displayed when the user clicks
the hyperlink.

**selectedColor**
: The color of the text when the mouse pointer is hovering
over it.

**unselectedColor**
: The color of the text when the mouse pointer is not
hovering over it.

**targetWindow**
: The name of the window in which the page is displayed
when the user clicks on the hyperlink.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
