---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOFrame.html
archived_at: '2026-07-15T08:14:38.985122Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOFrame

## Element Description

WOFrame represents itself as a dynamically generated Netscape
Frame element.

## Synopsis

WOFrame { value=_aMethod_;
| src=_aURL_; | pageName=_aString_;
| directActionName=_anActionName_; actionClass=_className_;...
};

## Bindings

**value**
: Method that will supply the content for this frame.

**src**
: External source that will supply the content for this
frame.

**pageName**
: Name of WebObjects page that will supply the content
for this frame.

**directActionName**
: The name of the direct action method (minus the "Action"
suffix) that will supply the content for the frame.

**actionClass**
: The name of the class in which the method designated
in __directActionName__ can be found. Defaults
to "`DirectAction`".

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
