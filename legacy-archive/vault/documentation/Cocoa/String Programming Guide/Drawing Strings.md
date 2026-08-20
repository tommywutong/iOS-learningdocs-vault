---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/DrawingStrings.html
archived_at: '2026-07-15T07:19:30.164277Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [字符串编程指南](Introduction%20to%20String%20Programming%20Guide.md)


[下一页](Document%20Revision%20History.md)[上一页](String%20Representations%20of%20File%20Paths.md)

# 绘制字符串

你可以使用 [drawAtPoint:withAttributes:](https://developer.apple.com/documentation/foundation/nsstring/1533109-drawatpoint) 之类的方法，把字符串对象直接绘制到已获得绘图焦点的 `NSView` 中（如果要绘制带有多种属性的字符串，比如使用多种文本字体，则必须使用 `NSAttributedString` 对象）。_[Cocoa 绘图指南](../Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_ 中的[文本](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Text/Text.html#//apple_ref/doc/uid/TP40003290-CH209)一章对这些方法作了简要介绍。

不过，这些简单方法是为绘制少量文本、或只偶尔绘制一次的文本而设计的——每次调用它们时，都会创建并销毁各种配套对象。如果需要反复绘制字符串，使用 `NSLayoutManager` 会更高效，具体做法参见 _[文本布局编程指南](../Text%20Layout%20Programming%20Guide/Introduction%20to%20Text%20Layout%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tq2i)_ 中的[绘制字符串](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextLayout/Tasks/DrawingStrings.html#//apple_ref/doc/uid/20001808)。`NSLayoutManager` 是 Cocoa 文本系统的一部分，要了解该系统的概况，请参阅 _[Cocoa 文本架构指南](../../Cocoa%20Text%20Architecture%20Guide/About%20the%20Cocoa%20Text%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinjz)_。

[下一页](Document%20Revision%20History.md)[上一页](String%20Representations%20of%20File%20Paths.md)

