---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WORepetition.html
archived_at: '2026-07-15T08:14:39.210443Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WORepetition

## Element Description

A WORepetition is a container element that repeats its contents
(that is, everything between the `<WEBOBJECT...>
and </WEBOBJECT...>` tags in the template
file) a given number of times. You can use a WORepetition to create
dynamically generated ordered and unordered lists or banks of check
boxes or radio buttons.

## Synopsis

WORepetition {list=_anObjectList_;
item=_anIteratedObject_; [index=_aNumber_;]
[identifier=_aString_;] ... };
WORepetition {count=_aNumber_;
[index=_aNumber_;] ... };

## Bindings

**list**
: Array of objects that the WORepetition will iterate
through. Ideally, this should be an immutable array. If you must
pass a mutable array, your code must not alter the array while the
WORepetition is iterating through it.

**item**
: Current item in the list array. (This attribute's
value is updated with each iteration.)

**index**
: Index of the current iteration of the WORepetition.
(This attribute's value is updated with each iteration.

**count**
: Number of times this element will repeat its contents.

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
