---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOBrowser.html
archived_at: '2026-07-15T08:14:38.873376Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOBrowser

## Element Description

WOBrowser displays itself as a selection list that displays
multiple items at a time. The related element [WOPopUpButton](WOPopUpButton.md#apple-ijduor2hirdek) is
similar to WOBrowser except that it restricts the display to only
one item at a time.

You should provide the title of an item in __displayString__ rather
than in __value__. If there is no binding for __displayString__,
the string assigned to __value__ is used for
the item.

## Synopsis

WOBrowser { list=_anArray_;
item=_anItem_; [displayString=_displayValue_;
value=_optionValue_;] [escapeHTML=_aBoolean_;]
[selections=_objectArray_; | selectedValues=_valueArray_;] [name=_fieldName_;]
[disabled=_aBoolean_;] [multiple = _aBoolean_;]
[size=_anInt_;]... };

## Bindings

**list**
: Array of objects from which the browser derives its
values. For example, colleges could name the list containing objects
that represent individual schools.

**item**
: Identifier for the elements of the list. For example, `aCollege` could
represent an object in the colleges array.

**displayString**
: Value to display in the selection list; for example, `aCollege.name` for
each college object in the list.

**value**
: For each OPTION tag within the selection, this is the __value__ attribute
(that is, `<OPTION value=someValue>`).
This value can be used as an identifier of an item in the list.

**escapeHTML**
: If __escapeHTML__ evaluates to `true` (or `YES`),
the string rendered by __displayString__ is
converted so that characters which would be interpreted as HTML
control characters become their escaped equivalent (this is the
default). Thus, if a your __displayString__ is
"`a <b>bold</b> idea`",
the string passed to the client browser would be "`a
<B>bold</B> idea`", but
it would display in the browser as "`a <b>bold</b>
idea`". If __escapeHTML__ evaluates
to `false` (or `NO`),
WebObjects simply passes your data to the client browser "as is."
In this case, the above example would display in the client browser
as "a __bold__ idea". If you are certain that
your strings have no characters in them which might be interpretted
as HTML control characters, you get better performance if you set __escapeHTML__ to `false` (or `NO`).

**selections**
: Array of objects that the user chose from list. For
the college example, selections would hold college objects.

**selectedValues**
: Array of values that is used with DirectActions to specify
which options in a list are selected.

**name**
: Name that uniquely identifies this element within the
form. You can specify a name or let WebObjects automatically assign
one at runtime.

**disabled**
: If __disabled__ evaluates to `true` (or `YES`),
this element appears in the page but is not active. That is, selections
won't contain the user's selection when the page is submitted.

**multiple**
: If __multiple__ evaluates to `true` (or `YES`),
the user can select multiple items from the list. Otherwise, the
user can select only one item from the list. The default is `false` (or `NO`).

**size**
: How many items to display at one time. The default is
5. __size__ must be greater than 1.

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
