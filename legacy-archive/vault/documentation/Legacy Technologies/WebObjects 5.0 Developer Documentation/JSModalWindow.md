---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/JSModalWindow.html
archived_at: '2026-07-15T08:14:39.671138Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# JSModalWindow

## Component Description

This component appears as a hyperlink in the browser. When
the user clicks it, the result displays in a modal-like window.

## Synopsis

JSModalWindow { action=_anAction_;
| pageName=_pageName_; height=_height_;
width=_width_;
windowName=_aString_;
[isResizable="YES"|"NO";] [showLocation="YES"|"NO";]
[showMenuBar="YES"|"NO";] [showScrollbars="YES"|"NO";]
[showStatus="YES"|"NO";]
[showToolbar="YES"|"NO";] };

## Bindings

**action**
: Action method invoked when the user clicks the hyperlink
that supplies the content for the modal-like window.

**pageName**
: The WOComponent displayed when the user clicks the hyperlink
that appears in the modal-like window.

**height**
: Height, in pixels, of the window.

**width**
: Width, in pixels, of the window.

**windowName**
: Specifies the title for the window.

**isResizable**
: Controls whether the window can be resized.

**showLocation**
: Controls whether the window displays the URL.

**showMenubar**
: Controls whether the window has a menu bar.

**showScrollbars**
: Controls whether the window has scroll bars.

**showStatus**
: Controls whether the window has a status display.

**showToolbar**
: Controls whether the window has a tool bar.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
