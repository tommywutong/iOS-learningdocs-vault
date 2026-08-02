---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOPopUpButton.html
archived_at: '2026-07-15T08:00:45.243442Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOPopUpButton

---

# Synopsis

WOPopUpButton { list=_anArray_; item=_anItem_; displayString=_displayedValue_; [value=_optionValue_;] [selection=_theSelection_;] [name=_fieldName_;] [disabled=YES|NO;] [escapeHTML=YES|NO;] [noSelectionString=_aString_]... };

---

# Description

WOPopUpButton, when clicked, displays itself as a selection list that allows the user to select only one item at a time. The related element WOBrowser is similar to WOPopUpButton except that it allows the user to select more than one item at a time.

You should provide the title of an item in displayString rather than in value. If there is no binding for displayString, the string assigned to value is used for the item.

---

# Bindings

**---

### list

Array of objects from which the WOPopUpButton derives its values. For example, colleges could name the array containing objects that represent individual schools.

**---

### item

Identifier for the elements of the list. For example, aCollege could represent an object in the colleges array.

**---

### displayString

Value to display in the selection list; for example, aCollege.name for each college object in the list.

**---

### value

For each OPTION tag within the selection, this is the "value" attribute (that is, <OPTION value="_someValue_">). You can use this binding to specify additional identifiers of each item in the menu.

**---

### selection

Object that the user chose from the selection list. For the college example, selection would be a college object.

**---

### name

Name that uniquely identifies this element within the form. You can specify a name or let WebObjects automatically assign one at runtime.

**---

### disabled

If disabled evaluates to YES, this element appears in the page but is not active. That is, selection does not contain the user's selection when the page is submitted.

**---

### escapeHTML

If escapeHTML is YES (the default), the string rendered by displayString is converted so that characters which would be interpretted as HTML control characters become their escaped equivalent. By default, WebObjects tries to ensure that data displays in the client browser just as it does in a normal editor. Thus, if a your displayString is "a <b>bold</b> idea", the string passed to the client browser would be "a <B>bold</B> idea", but it would display in the browser as "a <b>bold</b> idea". If escapeHTML is NO, WebObjects simply passes your data to the client browser "as is." In this case, the above example would display in the client browser as "a __bold__  idea". If you are certain that your strings have no characters in them which might be interpretted as HTML control characters, you get better performance if you set escapeHTML to NO.

**---

### noSelectionString

Enables the first item to be "empty." Bind this attribute to a string (such as an empty string) that, if chosen, represents an empty selection. When this item is selected, then the selection attribute is set to nil or null.******************

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
