---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WONestedList.html
archived_at: '2026-07-15T08:09:53.380912Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

# WONestedList

## Element Description

WONestedList recursively displays a hierarchical, ordered
(numbered) or unordered (bulleted) list of hyperlinks. This element
is useful when you want to display hierarchical lists. When the
user clicks one of the objects in the list, it is returned in __selection__ and
the action method is invoked.

At any point during iteration of the list, the method specified
by the __sublist__ attribute returns the current
list's sublist (if any), __level__ specifies
the current nesting level (where the topmost level is zero), __index__ gives
index of the current item within that nesting level (__item__ returns
the actual item), and __isOrdered__ specifies
whether the current sublist should be a numbered list or a bulleted
list.

## Synopsis

WONestedList { list=_anObjectList_;
item=_anIteratedObject_; displayString=_displayedValue_;
sublist = _aSubarray_; action=_aMethod_;
selection=_selectedValue_; [index=_aCurrentIndex_;]
[level=_aCurrentLevel_;] [isOrdered=_aBoolean_;]
[prefix=_prefixString_;] [suffix=_suffixString_;] [escapeHTML=_aBoolean_;]...
};

## Bindings

**list**
: Hierarchical array of objects that the WONestedList
will iterate through.

**item**
: Current item in the list array. (This attribute's
value is updated with each iteration.)

**displayString**
: String to display as a hyperlink for the current item.

**sublist**
: Method that returns the sublist of the current item
or `nil` if the current item is a leaf.

**action**
: Action method to invoke when the element is activated.
This method must return a WOElement.

**selection**
: When the page is submitted, selection contains the item
that the user clicked.

**index**
: Index of the current iteration of the WONestedList.
The index is unique to each level-that is, it starts at 0 for
each sublist.

**level**
: Nesting level of the current iteration of the WONestedList.
The topmost level is level 0.

**isOrdered**
: If __isOrdered__ evaluates to `true` (or `YES`),
the current sublist is rendered as an ordered list. The default
is to render as an unordered list.

**prefix**
: An arbitrary HTML string inserted before each value.

**suffix**
: An arbitrary HTML string inserted after each value.

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

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
