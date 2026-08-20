---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WONestedList.html
archived_at: '2026-07-15T08:00:43.770656Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


![Developer Documentation](attachments/images/wothinban.gif)

__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WONestedList

---

# Synopsis

WONestedList { list=_anObjectList_; item=_anIteratedObject_; displayString=_displayedValue_; sublist = _aSubarray_; action=_aMethod_; selection=_selectedValue_; [index=_aCurrentIndex_;] [level=_aCurrentLevel_;] [isOrdered=YES|NO;] [prefix=_prefixString_;] [suffix=_suffixString_;] [escapeHTML=YES|NO;]... };

---

# Description

WONestedList recursively displays a hierarchical, ordered (numbered) or unordered (bulleted) list of hyperlinks. This element is useful when you want to display hierarchical lists. When the user clicks one of the objects in the list, it is returned in selection and the action method is invoked.

At any point during iteration of the list, the method specified by the sublist attribute returns the current list's sublist (if any), level specifies the current nesting level (where the topmost level is zero), index gives index of the current item within that nesting level (item returns the actual item), and isOrdered specifies whether the current sublist should be a numbered list or a bulleted list.

---

# Bindings

**---

### list

Hierarchical array of objects that the WONestedList will iterate through.

**---

### item

Current item in the list array. (This attribute's value is updated with each iteration.)

**---

### displayString

String to display as a hyperlink for the current item.

**---

### sublist

Method that returns the sublist of the current item or nil if the current item is a leaf.

**---

### action

Action method to invoke when the element is activated. This method must return a WOElement.

**---

### selection

When the page is submitted, selection contains the item that the user clicked.

**---

### index

Index of the current iteration of the WONestedList. The index is unique to each level-that is, it starts at 0 for each sublist.

**---

### level

Nesting level of the current iteration of the WONestedList. The topmost level is level 0.

**---

### isOrdered

If isOrdered evaluates to YES, the current sublist is rendered as an ordered list. The default is to render as an unordered list.

**---

### prefix

An arbitrary HTML string inserted before each value.

**---

### suffix

An arbitrary HTML string inserted after each value.

**---

### escapeHTML

If escapeHTML is YES (the default), the string rendered by displayString is converted so that characters which would be interpretted as HTML control characters become their escaped equivalent. By default, WebObjects tries to ensure that data displays in the client browser just as it does in a normal editor. Thus, if a your displayString is "a <b>bold</b> idea", the string passed to the client browser would be "a <B>bold</B> idea", but it would display in the browser as "a <b>bold</b> idea". If escapeHTML is NO, WebObjects simply passes your data to the client browser "as is." In this case, the above example would display in the client browser as "a bold idea". If you are certain that your strings have no characters in them which might be interpretted as HTML control characters, you get better performance if you set escapeHTML to NO.************************

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
