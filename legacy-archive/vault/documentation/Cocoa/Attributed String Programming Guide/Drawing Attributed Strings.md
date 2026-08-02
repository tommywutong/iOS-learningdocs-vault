---
title: 属性字符串编程指南
apple_id: 10000036i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/Tasks/DrawingAttrStrings.html
archived_at: '2026-07-15T05:25:53.163694Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [属性字符串编程指南](Introduction%20to%20Attributed%20String%20Programming%20Guide.md)


[下一页](RTF%20Files%20and%20Attributed%20Strings.md)[上一页](Changing%20an%20Attributed%20String.md)

# 绘制属性字符串

Application Kit 的 NSStringDrawing 扩展让你可以使用多种方法在获得焦点的图形上下文（通常是一个 NSView）中绘制属性字符串，这些方法包括：`drawAtPoint:`、`drawInRect:`，以及（在 OS X v10.4 及更高版本中）`drawWithRect:options:`。这些方法适用于绘制少量文本，或者只需偶尔绘制一次的文本。每次调用这些方法时，都会创建并释放各种辅助文本对象。若要反复绘制字符串，使用 NSLayoutManager 会更高效，具体说明见[绘制字符串](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextLayout/Tasks/DrawingStrings.html#//apple_ref/doc/uid/20001808)。

请注意，Application Kit 也为 NSString 定义了绘制方法，使任何字符串对象都能自行绘制。这些方法——`drawAtPoint:withAttributes:`、`drawInRect:withAttributes:`，以及（在 OS X v10.4 及更高版本中）`drawWithRect:options:attributes:`——在 NSString Additions 中有详细说明。

在 OS X v10.4 及更高版本中，你可以使用 `boundingRectWithSize:options:` 方法获取排布某个属性字符串所需的矩形区域。同样，也存在一个类似的方法——`boundingRectWithSize:options:attributes:`——可以在给定一组属性的情况下，确定渲染某个 NSString 对象所需的矩形区域。

[下一页](RTF%20Files%20and%20Attributed%20Strings.md)[上一页](Changing%20an%20Attributed%20String.md)

