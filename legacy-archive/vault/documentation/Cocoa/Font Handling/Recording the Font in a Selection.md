---
title: Font Handling
apple_id: 10000093i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/Concepts/RecordingSelectedFont.html
archived_at: '2026-07-15T07:15:43.925048Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Handling](Introduction%20to%20Font%20Handling.md)


[Next](Initiating%20Font%20Changes.md)[Previous](Special%20Glyphs.md)

# Recording the Font in a Selection

Any object
that records fonts that the user can change should tell the font
manager what the
font of its selection is whenever it becomes the first responder and
whenever its selection changes while it’s the first responder.
The object does so by sending the shared font manager a `setSelectedFont` message.
It should pass in the first font of the selection, along with a
flag indicating whether there’s more than one font.

The font manager uses this information to update the Font
panel and Font
menu to reflect the font
in the selection. For example, suppose the font is Helvetica Oblique
12.0 point. In this case, the Font panel selects that font and displays
its name; the Font menu changes its Italic command to Unitalic;
if there’s no Bold variant of Helvetica available, the Bold menu item
is disabled; and so on.

If you need to draw text using PostScript operators
such as `show`, it’s
recommended that you set the current font using NSFont’s `set` method,
rather than the PostScript operators `setfont` or `selectfont`.
This allows the Application Kit printing mechanism to record the fonts
used in the PostScript output. If you absolutely must set the font
using a PostScript operator, you can record the font with the Application
Kit using the NSFont static method `useFont`.
See the description of that method for more information.

[Next](Initiating%20Font%20Changes.md)[Previous](Special%20Glyphs.md)

