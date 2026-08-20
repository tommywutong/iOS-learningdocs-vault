---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/ReusableComponents/D2WList.html
archived_at: '2026-07-15T08:11:31.399540Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

[![Table of Contents](attachments/images/up.gif)](../DirectToWebTOC.md)

# D2WList

## Component Description

This Direct to Web reusable component displays a list component.
See the "Direct to Web" chapter of _WebObjects Tools
and Techniques_ for information about the behavior and
appearance of this component.

## Synopsis

D2WList { [action=_anAction_;]
dataSource=_aDataSource_; | list=_anArray_;
[displayKeys=_keyArray_;] entityName=_nameString_;
[pageConfiguration=_aConfiguration_;]
};

## Bindings

**action**
: The action method to invoke when the user clicks Return.

**dataSource**
: An EODataSource containing the objects to display as
a list.

**list**
: An array containing the objects to display as a list.

**displayKeys**
: The properties of the entity to edit (NSArray). You
can also represent the array as a string: "(_prop1_, _prop2_,
...)".

**entityName**
: The name of the entity for this record (String).

**pageConfiguration**
: The named configuration containing the Web Assistant
settings for this component (String). If this binding is not specified,
the "\*all\*" configuration for the edit task and the _entityName_ entity
is used. See the "Direct to Web" chapter of _WebObjects
Tools and Techniques_ for more information about named
configurations.

## Example

> ```
> myList : D2WList {
>     entityName = "Movie";
>     dataSource = displayGroup.dataSource;
>     pageConfiguration = "myListMovieConfig";
> }
> ```

[![Table of Contents](attachments/images/up.gif)](../DirectToWebTOC.md)
