---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOPopUpButton.html
archived_at: '2026-07-15T08:09:53.424416Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

# WOPopUpButton

## Element Description

WOPopUpButton, when clicked, displays itself as a selection
list that allows the user to select only one item at a time. The
related element [WOBrowser](WOBrowser.md#apple-ijbesr2bindus) is
similar to WOPopUpButton except that it allows the user to select
more than one item at a time.

You should provide the title of an item in __displayString__ rather
than in __value__. If there is no binding for __displayString__,
the string assigned to __value__ is used for
the item.

## Synopsis

WOPopUpButton { list=_anArray_;
item=_anItem_; displayString=_displayedValue_;
[value=_optionValue_;] [selection=_theSelection_;
| selectedValue=_selectedValue_;] [name=_fieldName_;] [disabled=_aBoolean_;]
[escapeHTML=_aBoolean_;] [noSelectionString=_aString_]...
};

## Bindings

**list**
: Array of objects from which the WOPopUpButton derives
its values.

**item**
: Identifier for the elements of the list. For example, `aCollege` could
represent an object in a `colleges` array.

**displayString**
: Value to display in the selection list; for example, `aCollege.name` for
each `college` object in the
list.

**value**
: For each `OPTION` tag
within the selection, this is the "value" attribute (that is, `<OPTION value="someValue">`).
You can use this binding to specify additional identifiers of each
item in the menu.

**selection**
: Object that the user chose from the selection list.
For the college example, __selection__ would be
a `college` object.

**selectedValue**
: Value that is used with DirectActions to specify which
option in the list is selected.

**name**
: Name that uniquely identifies this element within the
form. You can specify a name or let WebObjects automatically assign
one at runtime.

**disabled**
: If __disabled__ evaluates to `true` (or `YES`),
this element appears in the page but is not active. That is, __selection__ does
not contain the user's selection when the page is submitted.

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
as "`a bold idea`".
If you are certain that your strings have no characters in them
which might be interpreted as HTML control characters, you get better
performance if you set __escapeHTML__ to `false` (or `NO`).

**noSelectionString**
: Enables the first item to be "empty." Bind this
attribute to a string (such as an empty string) that, if chosen,
represents an empty selection. When this item is selected, the __selection__ attribute
is set to `nil` or `null`.

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
