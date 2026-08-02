---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/Applets/TextFieldApplet.html
archived_at: '2026-07-15T08:00:30.325680Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Applet Controls](Client-Side%20Applet%20Controls.md)

[!Previous Section](ScrollingTextApplet.md)

---

# __TextFieldApplet__

---

### Synopsis

__WOApplet__ { __code__ = "next.wo.client.controls.TextFieldApplet.class";

__stringValue__=_text_; __echoCharacter__=_character_; __action__=_method_;...};

### Description

A TextFieldApplet displays a line of editable text within a rectangular border. Pressing the Return key can trigger an action method in the server-side component. This control also can function as a password field where entered characters are masked by a specified replacement character.TextFieldApplet "wraps" the __java.awt.TextField__ class.

**__stringValue__**
: During page generation, __stringvalue__ contains the initialized value. In each subsequent synchronization point, it contains any modification to the text the user makes and the text the action method assigns to it.

**__echoCharacter__**
: The character to display when the user types a character in the field (often an asterisk or a space character). This character is specified in the ".wod" file as a string, not as a character enclosed by single quotation marks.

**__action__**
: The method invoked when the user presses the Return key.
