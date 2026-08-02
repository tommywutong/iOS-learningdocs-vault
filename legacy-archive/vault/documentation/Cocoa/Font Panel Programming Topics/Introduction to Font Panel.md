---
title: Font Panel Programming Topics
apple_id: 10000116i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontPanel/FontPanel.html
archived_at: '2026-07-15T07:15:50.459071Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20Font%20Panel.md)

# Introduction to Font Panel

_Font
Panel_ explains how to use the font panel, which is defined by the [NSFontPanel](https://developer.apple.com/documentation/appkit/nsfontpanel) class.

You should read this document if you need to understand how the font panel interacts with the font manager and other components of the text system, particularly if you need to modify that behavior.

To understand the information in this document, you should understand generally the text system’s capabilities and architecture, and you should understand basic Cocoa programming conventions.

This document contains the following articles:

- [The Font Panel](The%20Font%20Panel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaztklkdjjbeeskbifda) describes the interaction of the font panel and Cocoa text objects and explains how to use the delegate of NSFontPanel to control the display of fonts in the font panel.
- [Creating a Font Panel](Creating%20a%20Font%20Panel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgq2dklkciffegrcijffa) explains how to add the font panel to your application using Interface Builder and, alternatively, how to create and modify the font panel programmatically.
- [Using the Font Panel](Using%20the%20Font%20Panel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaztmlkdjjbeeskbifda) describes the messages sent in the interaction among the font panel, font manager, and text objects.

For more information, refer to the following documents:

- _[Font Handling](../Font%20Handling/Introduction%20to%20Font%20Handling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4tg2i)_ discusses fonts, the font management system, and the user interface to allow the user to interact with available fonts.
[Next](The%20Font%20Panel.md)

