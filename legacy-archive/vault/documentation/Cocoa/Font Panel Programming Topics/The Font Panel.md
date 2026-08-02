---
title: Font Panel Programming Topics
apple_id: 10000116i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontPanel/Concepts/TextFontPanel.html
archived_at: '2026-07-15T07:15:50.453703Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Panel Programming Topics](Introduction%20to%20Font%20Panel.md)


[Next](Creating%20a%20Font%20Panel.md)[Previous](Introduction%20to%20Font%20Panel.md)

# The Font Panel

The font panel is a user interface object that displays a list of available font families and styles, letting the user preview them and change the font used to display text. Text objects, such as NSTextView, work with NSFontPanel and NSFontManager objects to implement the Application Kit’s font conversion system. By default, a text object keeps the font panel updated with the first font in its selection, or with its typing attributes. It also changes the font in which it displays text in response to messages from the font panel and Font menu. Such changes apply to the selected text or typing attributes for a rich text object or to all the text in a plain text object.

NSFontManager is the hub for font conversion. It receives the messages from the font panel and sends messages up the responder chain for action on the text objects.

Normally, an application’s font panel displays all the standard fonts available on the system. If this isn’t appropriate for your application—for example, if only fixed-pitch fonts should be used—you can assign a delegate to the NSFontPanel object to filter the available fonts. Before the NSFontPanel object adds a particular font family or face to its list, the NSFontPanel asks its delegate to confirm the addition by sending the delegate a [fontManager:willIncludeFont:](https://developer.apple.com/documentation/objectivec/nsobject/1462359-fontmanager) message. If the delegate returns `true` (or doesn’t implement this method), the font is added. If the delegate returns `false`, the font isn’t added.

[Next](Creating%20a%20Font%20Panel.md)[Previous](Introduction%20to%20Font%20Panel.md)

