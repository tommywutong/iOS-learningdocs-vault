---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOBrowser.html
archived_at: '2026-07-15T07:55:22.338947Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOBody.md)

## WOBrowser

### Synopsis

__WOBrowser__ __{__ __list__=_anArray___;__ [__item__=_anItem___;__ __value__=_displayedValue___;__] [__selections__=_objectArray___;__] [__name__=_fieldName___;__] [__disabled__=YES|NO__;__] [__multiple__ = YES|NO;] [__size__=_anInt_;]... __};__

### Description

WOBrowser displays itself as a selection list that displays multiple items at a time. The related element WOPopUpButton is similar to WOBrowser except that it restricts the display to only one item at a time.

**__list__**
: Array of objects from which the browser derives its values. For example, colleges could name the list containing objects that represent individual schools.

**__item__**
: Identifier for the elements of the list. For example, __aCollege__ could represent an object in the colleges array.

**__value__**
: Value to display in the selection list; for example, __aCollege.name__ for each college object in the list.

**__selections__**
: Array of objects that the user chose from list. For the college example, __selections__ would hold college objects.

**__name__**
: Name that uniquely identifies this element within the form. You can specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If __disabled__ evaluates to YES, this element appears in the page but is not active. That is, __selections__ won't contain the user's selection when the page is submitted.

**__multiple__**
: If __multiple__ evaluates to YES, the user can select multiple items from the list. If NO, the user can select only one item from the list. The default is NO.

**__size__**
: How many items to display at one time. The default is 5. __size__ must be greater than 1.

### Examples

[Forms and input elements](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOCheckBox.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
