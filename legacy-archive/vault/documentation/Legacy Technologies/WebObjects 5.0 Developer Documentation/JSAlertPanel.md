---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/JSAlertPanel.html
archived_at: '2026-07-15T08:14:39.625434Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# JSAlertPanel

## Component Description

This component appears as a hyperlink, which can contain an
image, text, and the JSAlertPanel's component content. When the
user clicks on it, a dialog box displaying an alert message appears.
When the user clicks OK, the hyperlink is executed.

## Synopsis

JSAlertPanel { action=_anAction_;
| javaScriptFunction=_javaScriptCodeString_;
| pageName=_aPageName_;
alertMessage=_message_; [altTag=_aTag_;]
[filename=_imageFileName_;]
[targetWindow=_windowName_;] [string=_aString_;]
};

## Bindings

**action**
: The action method performed when the user clicks OK.

**javaScriptFunction**
: Java Script code executed when the user clicks OK.

**pageName**
: The page displayed when the user clicks OK.

**alertMessage**
: The message to display when the user clicks on the hyperlink.

**altTag**
: The HTML alt attribute for the hyperlink's image if
an image is specified. Browsers can display this attribute in place
of the image.

**filename**
: The name of the image file. Binding this causes the
hyperlink to contain an image.

**targetWindow**
: The name of the window in which the page is displayed
when the user clicks OK.

**string**
: A string displayed in the hyperlink.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
