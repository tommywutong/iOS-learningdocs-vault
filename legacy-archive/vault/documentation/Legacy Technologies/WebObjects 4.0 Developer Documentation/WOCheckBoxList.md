---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOCheckBoxList.html
archived_at: '2026-07-15T08:00:34.963923Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOCheckBoxList

---

# Synopsis

WOCheckBoxList { list=_anObjectList_; item=_anIteratedObject_; displayString=_displayedValue_; [value=_aValue_;] [index=_aNumber_;] [prefix=_prefixString_;] [suffix=_suffixString_;] [selections=_selectedValues_;] [name=_fieldName_;] [disabled=YES|NO;] [escapeHTML=YES|NO;]... };

---

# Description

WOCheckBoxList displays a list of check boxes. The user may select several of the objects in the list, and this sublist is returned as selections.

You should provide the title of a checkbox in displayString rather than in value. If there is no binding for displayString, the string assigned to value is used to identify the checkbox.

---

# Bindings

**---

### list

Array of objects that the WOCheckBoxList will iterate through.

**---

### item

Current item in the list array. (This attribute's value is updated with each iteration.)

**---

### displayString

String to display beside the check box for the current item.

**---

### value

Value for the INPUT tag of the current item (INPUT type="Checkbox" value="_someValue_">. You can use this binding as an additional identifier of the itme.

**---

### index

Index of the current iteration of the WOCheckBoxList.

**---

### prefix

An arbitrary HTML string inserted before each value.

**---

### suffix

An arbitrary HTML string inserted after each value.

**---

### selections

An array of objects that the user chose from the list.

**---

### name

Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**---

### disabled

If disabled evaluates to YES, this element appears in the page but is not active.

**---

### escapeHTML

If escapeHTML is YES (the default), the string rendered by displayString is converted so that characters which would be interpretted as HTML control characters become their escaped equivalent. By default, WebObjects tries to ensure that data displays in the client browser just as it does in a normal editor. Thus, if a your displayString is "a <b>bold</b> idea", the string passed to the client browser would be "a <B>bold</B> idea", but it would display in the browser as "a <b>bold</b> idea". If escapeHTML is NO, WebObjects simply passes your data to the client browser "as is." In this case, the above example would display in the client browser as "a bold idea". If you are certain that your strings have no characters in them which might be interpretted as HTML control characters, you get better performance if you set escapeHTML to NO.**********************

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
