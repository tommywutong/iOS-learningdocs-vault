---
title: Font Handling
apple_id: 10000093i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/Tasks/CustomizingFontConversion.html
archived_at: '2026-07-15T07:15:47.448942Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Handling](Introduction%20to%20Font%20Handling.md)


[Next](Document%20Revision%20History.md)[Previous](Examining%20Fonts.md)

# Customizing the Font Conversion System

In Objective-C only, if you need to customize the font conversion
system by creating subclasses of NSFontManager or NSFontPanel, you
must inform the NSFontManager class of this change with a `setFontManagerFactory:` or `setFontPanelFactory:` message,
before either the shared font manager or shared Font panel is created.
These methods record your class as the one to instantiate the first
time the font manager or Font panel is requested.
You may be able to avoid using subclasses if all you need is to
add some custom controls to the Font panel. In this case, you can
invoke the NSFontPanel `setAccessoryView:` method
to add an NSView below its font browser.

In Java, to add some custom controls to the Font panel, invoke
NSFontPanel’s `setAccessoryView` to
add an NSView below its font browser.

If you provide your own Font menu, you should register it with the font manager
using the `setFontMenu` method.
The font manager is responsible for validating Font menu items and
changing their titles and tags according to the font of the selection.
For example, when the selected font is Italic, the font manager
changes the Italic Font menu item to Unitalic and changes its tag
to `UnitalicMask`. Your Font menu’s
items should use the appropriate action methods and tags. Here are
some examples:

| Font menu item | Action | Tag |
| --- | --- | --- |
| Italic | `addFontTrait` | `ItalicMask` |
| Bold | `addFontTrait` | `BoldMask` |
| Heavier | `modifyFont` | `HeavierFontAction` |
| Larger | `modifyFont` | `SizeUpFontAction` |

[Next](Document%20Revision%20History.md)[Previous](Examining%20Fonts.md)

