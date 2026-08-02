---
title: Font Panel Programming Topics
apple_id: 10000116i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontPanel/Tasks/CreatingAFontPanel.html
archived_at: '2026-07-15T07:15:51.955632Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Panel Programming Topics](Introduction%20to%20Font%20Panel.md)


[Next](Using%20the%20Font%20Panel.md)[Previous](The%20Font%20Panel.md)

# Creating a Font Panel

In general, you add the facilities of the font panel to your application, along with the NSFontManager and the Font menu, through which the user opens the font panel, using Interface Builder. You do this by dragging a Font or Format menu (which contains a Font submenu) into one of your application’s menus. At runtime, the font panel object is created and hooked into the font conversion system. You can also create (or access) the font panel using the `sharedFontPanel` class method.

You can add a custom view object to an NSFontPanel using `setAccessoryView`, allowing you to add custom controls to the font panel. You can also limit the fonts displayed (by default, all fonts) by assigning a delegate to the application’s font manager object (see [The Font Panel](The%20Font%20Panel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaztklkdjjbeeskbifda)).

In Objective-C, if you want the NSFontManager to instantiate the font panel from some class other than NSFontPanel, use the NSFontManager class method `setFontPanelFactory:`. See [Converting Fonts Manually](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/Tasks/ConvertingFontsManually.html#//apple_ref/doc/uid/20000442) for more information on using the font conversion system.

[Next](Using%20the%20Font%20Panel.md)[Previous](The%20Font%20Panel.md)

