---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOParam.html
archived_at: '2026-07-15T08:14:39.121167Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOParam

## Element Description

WOParam elements are used for passing [WOApplet](WOApplet.md#apple-ineuqssgjfceg) parameters.

## Synopsis

WOParam { name=_aString_;
value=_aString_; | action=_aMethod_;
... };

## Bindings

**name**
: Symbolic name associated with this element's value.

**value**
: Value of this parameter.

**action**
: Method that sets the parameter's value. Use this attribute
instead of __value__ if you want the parameter
to be a WebObjects component.

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
