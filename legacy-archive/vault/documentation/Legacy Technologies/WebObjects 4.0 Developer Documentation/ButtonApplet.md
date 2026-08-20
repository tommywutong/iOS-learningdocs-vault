---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/Applets/ButtonApplet.html
archived_at: '2026-07-15T08:00:25.631067Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Applet Controls](Client-Side%20Applet%20Controls.md)

[!Previous Section](Introduction-4.md)

---

# __ButtonApplet__

---

### Synopsis

__WOApplet__ { __code__ = "next.wo.client.controls.ButtonApplet.class";

__title__=_aTitle_; __action__=_method_;...};

### Description

A ButtonApplet is a control that invokes an action method in the component containing the WOApplet. The ButtonApplet class "wraps" the __java.awt.Button__ class.

**__title__**
: The title of the button. If no title is specified, the title used is "Button".

**__action__**
: The method to invoke when this control is clicked.

[!Next Section](CheckboxApplet.md)
