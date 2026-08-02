---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOAppleScript.html
archived_at: '2026-07-15T08:14:40.113124Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOAppleScript

## Component Description

The WOAppleScript component provides the ability to include
client-side AppleScript in web pages, allowing WebObjects to control
Macintosh computers that have the appropriate browser plug-in.

## Synopsis

WOAppleScript { scripttext=_aString;_ [controller=_aString_;]
[height=_aNumber_;]
[width=_aNumber_;] [scriptcomment=_aString_;]
[scripttitle=_aString_;] };

## Bindings

**scripttext**
: A string identifying the AppleScript to be executed
on the client. This attribute is required.

**controller**
: A string containing either "True" or "False"
that determines whether or not the controller panel should appear.

**height**
: The height of the AppleScript component in the client
browser.

**width**
: The width of the AppleScript component in the client
browser.

**scriptcomment**
: A comment for the AppleScript plug-in.

**scripttitle**
: A title for the AppleScript.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
