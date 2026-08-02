---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOToManyRelationship.html
archived_at: '2026-07-15T08:14:47.010383Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOToManyRelationship

## Component Description

The WOToManyRelationship component displays a set of possible
destination objects of an enterprise object's to-many relationship,
allows the user to select a subset of the destination objects, and
sets the enterprise object's relationship accordingly. It displays
the possible destination objects of the relationship in a browser
or as a set of checkboxes. This component must be embedded within
a WOForm.

## Synopsis

WOToManyRelationship { [uiStyle="checkbox"|"browser";]
sourceObject=_anObject_;
sourceEntityName=_aString_;
relationshipKey=_aString_; [destinationDisplayKey=_aString_;]
[isMandatory=_aboolean_;]
[maxColumns=_aNumber_;] [size=_aNumber_;]
[datasource=_aDataSource_;]
};

## Bindings

**uiStyle**
: The type of user interface. Defaults to "checkbox"
when the WOToManyRelationship component displays five or fewer objects.
Otherwise defaults to "browser".

**sourceObject**
: The enterprise object whose relationship is modified.
A display group's `queryMatch` dictionary
is also a valid source object. This allows you to query for objects
having a particular to-many relationship.

**sourceEntityName**
: The name of the entity that is modified.

**relationshipKey**
: The name of the relationship that is modified.

**destinationDisplayKey**
: A displayable attribute of the relationship's destination
objects. Defaults to "`userPresentableDescription`".

**isMandatory**
: A flag to indicate that a selection is necessary. Defaults
to `NO`.

**maxColumns**
: The maximum number of columns in the checkbox array.
Used only when the user interface style is "`checkbox`".

**size**
: The maximum number of rows in the browser. Used only
when the user interface style is "`browser`".

**dataSource**
: A data source for the relationship's destination objects.
By default, the WOToManyRelationship component creates an EODatabaseDataSource
containing all possible destination objects. However, if you want
to limit the number of destination objects the user can choose,
you can create your own EODatabaseDataSource that has a subset of the
possible destination objects and bind it to this attribute.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
