---
title: Text System Storage Layer Overview
apple_id: 10000087i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextStorageLayer/Tasks/DisplayingTextCont.html
archived_at: '2026-07-15T07:20:30.210879Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text System Storage Layer Overview](Introduction%20to%20Text%20System%20Storage%20Layer%20Overview.md)


[Next](Calculating%20Region%2C%20Bounding%20Rectangle%2C%20and%20Inset.md)[Previous](Changing%20Text%20Storage.md)

# Displaying a Text Container

You normally use an [NSTextView](https://developer.apple.com/documentation/appkit/nstextview) object to display the text laid out in an [NSTextContainer](https://developer.apple.com/documentation/appkit/nstextcontainer). An `NSTextView` can have only one `NSTextContainer`; however, because the two are separate objects, you can replace an `NSTextView`’s container to change the layout of the text it displays. You can also display an `NSTextContainer`’s text in any [NSView](https://developer.apple.com/documentation/appkit/nsview) by locking the graphic focus on it with [lockFocus](https://developer.apple.com/documentation/appkit/nsview/1483608-lockfocus) and using the [NSLayoutManager](https://developer.apple.com/documentation/appkit/nslayoutmanager) methods [drawBackgroundForGlyphRange:atPoint:](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402949-drawbackground) and [drawGlyphsForGlyphRange:atPoint:](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403158-drawglyphsforglyphrange). If you have no need to actually display the text—if you’re only calculating line breaks or number of lines or pages, for example—you can use an `NSTextContainer` without an `NSTextView`.

[Next](Calculating%20Region%2C%20Bounding%20Rectangle%2C%20and%20Inset.md)[Previous](Changing%20Text%20Storage.md)

