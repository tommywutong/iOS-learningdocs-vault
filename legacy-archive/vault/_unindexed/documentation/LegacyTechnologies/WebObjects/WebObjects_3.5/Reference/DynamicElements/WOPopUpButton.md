---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOPopUpButton.html
archived_at: '2026-07-15T07:55:30.287499Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOPasswordField.md)

## WOPopUpButton

### Synopsis

__WOPopUpButton__ __{__ __list__=_anArray___;__ [__item__=_anItem___;__ __value__=_displayedValue___;__] [__selection__=_theSelection___;__] [__name__=_fieldName___;__] [__disabled__=YES|NO__;__] ... __};__

### Description

WOPopUpButton displays itself as a selection list that allows the user to select only one item at a time. The related element WOBrowser is similar to WOPopUpButton except that it allows the user to select more than one item at a time.

**__list__**
: Array of objects from which the WOPopUpButton derives its values. For example, __colleges__ could name the array containing objects that represent individual schools.

**__item__**
: Identifier for the elements of the list. For example, __aCollege__ could represent an object in the colleges array.

**__value__**
: Value to display in the selection list; for example, __aCollege.name__ for each college object in the list.

**__selection__**
: Object that the user chose from the selection list. For the college example, __selection__ would be a college object.

**__name__**
: Name that uniquely identifies this element within the form. You can specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If disabled evaluates to YES, this element appears in the page but is not active. That is, __selection__ does not contain the user's selection when the page is submitted.

### Examples

[Forms and input elements](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WORadioButton.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
