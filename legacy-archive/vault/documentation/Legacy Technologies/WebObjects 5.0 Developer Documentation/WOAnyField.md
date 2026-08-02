---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOAnyField.html
archived_at: '2026-07-15T08:14:39.714925Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOAnyField

## Component Description

The WOAnyField component provides an interface for the user
to qualify a WODisplayGroup's enterprise objects based on a single
attribute of the objects. The user can choose the attribute, an operator
(less than, greater than, equal to, or not equal to), and a value
for the attribute. The attribute can be an attribute of the displayed
objects, or an attribute of another object obtained by traversing
a relationship. The component sets a WODisplayGroup's `queryMatch` dictionary
according to the user's choices but does not redisplay the objects.

This component must be embedded within a WOForm. If you want
to redisplay the objects with the new qualifier, bind the `value` attribue
of the WOForm's submit button to the WODisplayGroup's __qualifyDataSource__
method.

![[image: Art/WOExtWOAnyField.gif]](Art/WOExtWOAnyField.gif)

## Synopsis

WOAnyField { displayGroup=_aDisplayGroup_;
displayKey=_aString_;] [formatter=_formatterObj_;
key=_aString_; keyList=_anArray_;
[relationshipKey=_aString_;] [selectedKey=_aString_;]
sourceEntityName=_aString_;
[value=_anObject_;] };

## Bindings

**displayGroup**
: The display group for which the WOAnyField component
sets the `queryMatch` dictionary.

**displayKey**
: The string corresponding to `key` that
the WOAnyField component displays. Can be bound to the same String
(NSString in Objective-C) as `key`.

**formatter**
: An instance of an NSFormatter subclass
for the attribute corresponding to `key` used
to format the attribute's values for display as strings and format
user entered strings back into the attribute's values. The `formatter`
attribute should specify a variable containing (or method returning)
a preconfigured formatter object.

**key**
: The key corresponding to the current iteration through
the key list.

**keyList**
: An array containing keys corresponding to the attributes
with which the user can qualify the displayed objects.

**relationshipKey**
: The key corresponding to one of the source entity's
relationships. If this binding is specified, the WOAnyField component
builds the `queryMatch` dictionary
based on attributes from the destination object. This binding allows
you to query with a single level of indirection. For example, you
can query for all movies produced by studios starting with 'P'.
If this binding is omitted, the source entity's attributes are
used.

**selectedKey**
: The key that is selected when the WOAnyField component
is first displayed.

**sourceEntityName**
: The name of entity displayed by the display group.

**value**
: The value that appears in the value text field when
the WOAnyField component is first displayed.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
