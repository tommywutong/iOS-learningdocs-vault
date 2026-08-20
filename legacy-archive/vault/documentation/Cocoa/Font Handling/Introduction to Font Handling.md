---
title: Font Handling
apple_id: 10000093i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/FontHandling.html
archived_at: '2026-07-15T07:15:44.436798Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Creating%20a%20Font%20Object.md)

# Introduction to Font Handling

_Font
Handling_ discusses fonts, the font management system,
and the user interface to allow the user to interact with available
fonts.

You should read this document if you need to understand how
the text system manages font objects, how the font manager works,
and how to modify that behavior. If your application allows users
to manipulate fonts, for example, especially if it goes beyond default
Cocoa behavior, then you should read this document.

To understand the information in this programming topic, you
should understand generally the text system’s capabilities and
architecture, and you should understand basic Cocoa programming
conventions.

These articles discuss working with NSFont objects:

- [Creating a Font Object](Creating%20a%20Font%20Object.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg44dilkdjjbeerkji5ca) describes
  the methods you use to create font objects.
- [Getting Font Metrics](Getting%20Font%20Metrics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgqztslkcijbuuq2fjjca) describes
  font metrics and correlates them with the methods you use to retrieve
  that information.
- [Querying Aqua Font Variations](Querying%20Aqua%20Font%20Variations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg44dqlkdjjbeqqsdi5ba) lists
  the methods you use to retrieve the standard fonts used in the Aqua
  user interface.
- [Characters and Glyphs](Characters%20and%20Glyphs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaztilkdjjbeuschifdq) defines
  and differentiates characters and glyphs and explains how the text
  system converts character strings into glyphs for display.
- [Calculating Glyph Layout](Calculating%20Glyph%20Layout.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgqztilkdjjbekscgjjbq) describes
  the sequential, overstruck, and stacked methods of laying out glyphs.
- [Special Glyphs](Special%20Glyphs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgqztklkcijbumq2fjffa) describes null
  glyphs and control glyphs.

These articles discuss working with the font manager:

- [Recording the Font in a Selection](Recording%20the%20Font%20in%20a%20Selection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgqztmlkcineuorkkijfa) explains
  how an object that enables the user to select fonts should interact
  with the font manager.
- [Initiating Font Changes](Initiating%20Font%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgqztolkcijbusrkijbdq) describes
  the font-changing action methods of the font manager.
- [Creating a Font Manager](Creating%20a%20Font%20Manager.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgq2dalkdjjbeerkji5ca) explains
  how to set up a font manager object programmatically.
- [Responding to Font Changes](Responding%20to%20Font%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgq2dclkdjjbeqqsdi5ba) explains
  how a text object should respond to a font-changing message from
  the font manager.
- [Converting Fonts Manually](Converting%20Fonts%20Manually.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgq2delkdjjbeoqsbivdq) describes
  the NSFontManager methods you use to convert the traits and characteristics
  of a font.
- [Examining Fonts](Examining%20Fonts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgq2dglkdjjbeeskbifda) describes
  the methods applications can use to retrieve information about font
  availability and characteristics.
- [Customizing the Font Conversion System](Customizing%20the%20Font%20Conversion%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgq2dilkcijbumsciirea) discusses
  adding custom controls to the Font panel, subclassing NSFontManager
  and NSFontPanel, and using your own Font menu.

For further reading, refer to the following documents:

- _[Font Panel Programming Topics](../Font%20Panel%20Programming%20Topics/Introduction%20to%20Font%20Panel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeytm2i)_ explains
  how the Font panel interacts with the text system.
- _[Attributed String Programming Guide](../Attributed%20String%20Programming%20Guide/Introduction%20to%20Attributed%20String%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztm2i)_ describes NSAttributedString objects, which manage
  sets of attributes, such as font and kerning, that are associated
  with character strings or individual characters.
- _[Text Layout Programming Guide](../Text%20Layout%20Programming%20Guide/Introduction%20to%20Text%20Layout%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tq2i)_ describes how the Cocoa text system converts strings
  of text characters, font information, and page specifications into
  lines of glyphs placed at specific locations on a page, suitable
  for display and printing.

For related reference information, see the following documents:

- NSFont
- NSFontManager
- NSFontPanel
[Next](Creating%20a%20Font%20Object.md)

