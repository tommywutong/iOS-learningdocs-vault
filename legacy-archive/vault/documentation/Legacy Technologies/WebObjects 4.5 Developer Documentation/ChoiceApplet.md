---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/Applets/ChoiceApplet.html
archived_at: '2026-07-15T08:09:51.945868Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
Applet Controls

---

[!Previous Section](CheckboxApplet.md)

---

# __ChoiceApplet__

---

### Synopsis

__WOApplet__ { __code__ = "next.wo.client.controls.ChoiceApplet.class";

__itemList__=_anArray_; __selectedItem__=_itemIndex_; __action__=_method_;...};

### Description

A ChoiceApplet displays a non-editable list of items from which the user can select one item.This control looks and behaves like a pull-down list or combo box. This class is based on the __java.awt.Choice__ class.

**__itemList__**
: An array of strings representing the choices available.

**__selectedItem__**
: Numeric index of the item selected in __itemList__. Index 0 identifies the first item in the array.

**__action__**
: The method invoked when a choice is made.

[!Next Section](ListApplet.md)
