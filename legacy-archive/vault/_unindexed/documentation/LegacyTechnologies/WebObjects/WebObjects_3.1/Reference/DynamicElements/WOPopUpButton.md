---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOPopUpButton.html
archived_at: '2026-07-15T07:49:43.202398Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOPasswordField.md)

---

# __WOPopUpButton__

### Synopsis

__WOPopUpButton__ __{__ __list__=_`anArray`___;__ [__item__=_`anItem`___;__ __value__=_`displayedValue`___;__] [__selection__=_`objectArray`___;__] [__name__=_`fieldName`___;__] [__disabled__=YES|NO__;__] ... __};

### Description__

WOPopUpButton displays itself as a selection list that allows the user to select only one item at a time. The related element WOBrowser is similar to WOPopUpButton except that it allows the user to select more than one item at a time.

**__list__**
: Array of objects from which the WOPopUpButton derives its values. For example, __colleges__ could name the array containing objects that represent individual schools.

**__item__**
: Identifier for the elements of the list. For example, __aCollege__ could represent an object in the colleges array.

**__value__**
: Value to display in the selection list; for example, __aCollege.name__ for each college object in the list.

**__selection__**
: Array of objects that the user chose from the selection list. For the college example, selection would hold college objects. Since a WOPopUpButton lets the user select only one item at a time, this array holds no more than one item.

**__name__**
: Name that uniquely identifies this element within the form. You can specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If disabled evaluates to YES, this element appears in the page but is not active.

### Examples

[Forms and input elements](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WORadioButton.md)
