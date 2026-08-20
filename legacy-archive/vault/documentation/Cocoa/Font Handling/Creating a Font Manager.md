---
title: Font Handling
apple_id: 10000093i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/Tasks/CreatingAFontManager.html
archived_at: '2026-07-15T07:15:46.435278Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Handling](Introduction%20to%20Font%20Handling.md)


[Next](Responding%20to%20Font%20Changes.md)[Previous](Initiating%20Font%20Changes.md)

# Creating a Font Manager

You normally set up a font manager and the Font menu using Interface Builder.
However, you can also do so programmatically by getting the shared
font manager instance and having it create the standard Font menu
at runtime, as in this Objective-C example:

```
NSFontManager *fontManager = [NSFontManager sharedFontManager];
NSMenu *fontMenu = [fontManager fontMenu:YES];
```

You can then add the Font menu to your application’s menus.
Once the Font menu is installed, your application automatically
gains the functionality of both the Font menu and the Font panel.

[Next](Responding%20to%20Font%20Changes.md)[Previous](Initiating%20Font%20Changes.md)

