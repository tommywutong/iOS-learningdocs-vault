---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/Applets/ScrollingTextApplet.html
archived_at: '2026-07-15T08:00:29.832372Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Applet Controls](Client-Side%20Applet%20Controls.md)

[!Previous Section](RadioGroupApplet.md)

---

# __ScrollingTextApplet__

---

### Synopsis

__WOApplet__ { __code__ = "next.wo.client.controls.ScrollingTextApplet.class";

__stringValue__=_text_;...};

### Description

A ScrollingTextApplet is a bordered area on the page that allows viewing and editing of one or more lines of text. If the amount of text exceeds the display area, scrollbars enable the user to move text up and down within the display area. Pressing the Return key inserts a carriage return instead of (like TextFieldApplet) triggering an action method. The ScrollingTextApplet class "wraps" the __java.awt.TextArea__ class.

__Note__: A ScrollingTextApplet does not wrap text as it approaches the right side of the display area. Instead, it scrolls text to the left. This is a limitation of __java.awt.TextArea__.

**__stringValue__**
: During page generation, __stringvalue__ contains the initialized value. In each subsequent synchronization point, it contains any modification to the text the user makes and the text the action method assigns to it.

[!Next Section](TextFieldApplet.md)
