---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/ClientSideComponents/Applets/ListApplet.html
archived_at: '2026-07-15T07:55:12.997414Z'
---
> 导航：[总目录](../../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](CSControls.mif.book.md)
[!Previous Section](ChoiceApplet.md)

---

# __ListApplet__

---

### Synopsis

__WOApplet__ { __code__ = "next.wo.client.controls.ListApplet.class";

__itemList__=_arrayOfItems_; __selectedItem__s=_arrayOfIndices_; __allowsMultipleSelection__="YES"|"NO"; __action__=_actionMethod_;

__selectionChanged__=_changeMethod_;...};

### Description

A ListApplet presents a list of items that allows multiple selections. Users select and deselect items in the list by clicking them. By default, this control disallows multiple selections, so you must set __allowsMultipleSelection__ to YES to get the multiple-selection capability. The way the _actionMethod_ is invoked in the component object differs for single and multiple selections. To invoke the method with a single selection, the user double-clicks the selection (this works even in multiple-selection mode). To invoke the _actionMethod_ when there are multiple selections, the user must press the Return key. A ListApplet also invokes the _changeMethod_ in the server-side component (if implemented) whenever a change is made in the selection.

**__itemList__**
: An array of string objects that are displayed as the choices.

**__selectedItems__**
: An array of string objects representing the numeric indices of the selected items in the list.

**__allowsMultipleSelection__**
: If this value of this key evaluates to "YES", the user can select multiple items by clicking them in series. If "NO", the prior selection is deselected every time the user makes a new selection.

**__action__**
: The method invoked when the user double-clicks a single item in the list or presses the Return key.

**__selectionChanged__**
: The method invoked when an item in the list is selected or deselected.

[!Table of Contents](CSControls.mif.book.md)
[!Next Section](RadioGroupApplet.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
