---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/ReusableComponents/D2WSelect.html
archived_at: '2026-07-15T08:12:46.345134Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

# D2WSelect

## Component Description

This Direct to Web reusable component displays a select component.
See the "Direct to Web" chapter of _WebObjects Tools
and Techniques_ for information about the behavior and
appearance of this component.

## Synopsis

D2WSelect { [action=_anAction_;]
dataSource=_aDataSource_ | list=_anArray_; [displayKeys=_keyArray_;] entityName=_nameString_;
[pageConfiguration=_configurationName_;]
selectedObject=_anObject_; };

## Bindings

**action**
: The action method to invoke when the user clicks Select
or Return.

**dataSource**
: An EODataSource containing the objects the user can
select from.

**list**
: An array containing the objects to display as a list.

**displayKeys**
: The properties of the entity to edit (NSArray). You
can also represent the array as a string: "(_prop1_, _prop2_,
...)".

**entityName**
: The name of the entity this component displays (String).

**pageConfiguration**
: The named configuration containing the Web Assistant
settings for this component (String). If this binding is not specified,
the "\*all\*" configuration for the select task and the _entityName_ entity
is used. See the "Direct to Web" chapter of _WebObjects
Tools and Techniques_ for more information about named
configurations.

**selectedObject**
: The object the user selects with this component or `null` if
no object is selected.

## Example

> ```
> mySelect : D2WSelect {
>     entityName = "Movie";
>     selectedObject = displayGroup.selectedObject;
>     dataSource = displayGroup.dataSource;
>     action = selectAction;
> }
> ```

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
