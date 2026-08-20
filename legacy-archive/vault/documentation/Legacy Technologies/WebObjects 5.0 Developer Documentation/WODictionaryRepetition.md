---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WODictionaryRepetition.html
archived_at: '2026-07-15T08:14:42.746049Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WODictionaryRepetition

## Component Description

A WODictionaryRepetition is a container element that repeats
its contents (that is, everything between the `<WEBOBJECT...>` and
`</WEBOBJECT...>` tags
in the template file) for each entry in a dictionary. You can use
a WODictionaryRepetition to create dynamically generated unordered
lists or banks of check boxes or radio buttons.

## Synopsis

WODictionaryRepetition {dictionary=_aDictionary_;
item=_anObject_; key=_aString_;
};

## Bindings

**dictionary**
: Dictionary of key/value pairs through which the WODictionaryRepetition
iterates.

**key**
: Current key in the dictionary. This attribute's value
is updated with each iteration.

**item**
: Current object corresponding to the key in the dictionary.
This attribute's value is updated with each iteration.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
