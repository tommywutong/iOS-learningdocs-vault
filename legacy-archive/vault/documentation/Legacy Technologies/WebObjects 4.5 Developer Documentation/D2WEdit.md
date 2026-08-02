---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/ReusableComponents/D2WEdit.html
archived_at: '2026-07-15T08:11:31.372010Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

[![Table of Contents](attachments/images/up.gif)](../DirectToWebTOC.md)

# D2WEdit

## Component Description

This Direct to Web reusable component displays an edit component.
See the "Direct to Web" chapter of _WebObjects Tools
and Techniques_ for information about the behavior and
appearance of this component.

## Synopsis

D2WEdit { [action=_anAction_;]
[displayKeys=_keyArray_;] entityName=_nameString_; object=_anEnterpriseObject_;
[pageConfiguration=_configurationName_;]
};

## Bindings

**action**
: The action method to invoke when the user clicks Save
or Cancel. This method is invoked after the object is saved or discarded.

**displayKeys**
: The properties of the entity to edit (NSArray). You
can also represent the array as a string: "(_prop1_, _prop2_,
...)".

**entityName**
: The name of the entity for this record (String).

**object**
: The object edited by this component.

**pageConfiguration**
: The named configuration containing the Web Assistant
settings for this component (String). If this binding is not specified,
the "\*all\*" configuration for the edit task and the _entityName_ entity
is used. See the "Direct to Web" chapter of _WebObjects
Tools and Techniques_ for more information about named
configurations.

## Example

> ```
> myEdit : D2WEdit {
>     entityName = "Movie";
>     object = displayGroup.selectedObject;
>     action = editAction;
>     pageConfiguration = "userEditMovieConfig";
> }
> ```

[![Table of Contents](attachments/images/up.gif)](../DirectToWebTOC.md)
