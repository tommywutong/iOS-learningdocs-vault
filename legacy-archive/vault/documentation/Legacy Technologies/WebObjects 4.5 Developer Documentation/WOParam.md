---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOParam.html
archived_at: '2026-07-15T08:09:53.395966Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

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

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
