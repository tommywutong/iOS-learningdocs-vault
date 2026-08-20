---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/Applets/CheckboxApplet.html
archived_at: '2026-07-15T08:09:51.930391Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
Applet Controls

---

[!Previous Section](ButtonApplet.md)

---

# __CheckboxApplet__

---

### Synopsis

__WOApplet__ { __code__ = "next.wo.client.controls.CheckboxApplet.class";

__title__=_aTitle_; __action__=_method_; __checked__="YES"|"NO";...};

### Description

A CheckboxApplet is a control that uses an image of a check box to indicate "off" and "on" (or unselected and selected) states. It can invoke an action method upon a change of state. The CheckboxApplet class "wraps" the __java.awt.Checkbox__ class.

**__title__**
: The title of the check box.

**__action__**
: The method to invoke when the check box is clicked.

**__checked__**
: During page generation, if __checked__ evaluates to "YES", the check box appears in the checked state. In each subsequent synchronization point, __checked__ reflects the state the user left the check box in and the state it's set to by the action method.

[!Next Section](ChoiceApplet.md)
