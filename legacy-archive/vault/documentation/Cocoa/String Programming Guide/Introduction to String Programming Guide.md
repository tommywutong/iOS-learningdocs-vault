---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html
archived_at: '2026-07-15T07:19:35.690398Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Strings.md)

# 字符串编程指南简介

_字符串编程指南_ 介绍如何创建、搜索、拼接和绘制字符串。它还介绍了字符集（可用于在字符串中搜索属于某一组的字符）以及扫描器（可在数字与字符串之间相互转换）。

如果你需要直接处理字符串或字符集，就应当阅读本文档。

本文档包含以下文章：

- [字符串](Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dklkcijbugr2hinbq) 介绍 Cocoa 和 Cocoa Touch 中字符串对象的特性。
- [创建与转换字符串对象](Creating%20and%20Converting%20String%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dqlkdjjbegssijbeq) 说明 `NSString` 及其子类 `NSMutableString` 如何创建字符串对象，以及如何在它们支持的各种字符编码之间转换内容。
- [格式化字符串对象](Formatting%20String%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2dglkdjjbekqkfjbea) 介绍如何格式化 `NSString` 对象。
- [字符串格式说明符](String%20Format%20Specifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denrvfvjvomi) 介绍 `NSString` 支持的 `printf` 风格格式说明符。
- [从文件和 URL 读取字符串以及将字符串写入文件和 URL](Reading%20Strings%20From%20and%20Writing%20Strings%20To%20Files%20and%20URLs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztinjzfvjvomi) 介绍如何从文件和 URL 读取字符串，以及如何把字符串写入文件和 URL。
- [搜索、比较与排序字符串](Searching%2C%20Comparing%2C%20and%20Sorting%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dslkdjjbeer2cifeq) 介绍在字符串中查找字符和子串，以及比较两个字符串的各种方法。
- [词、段落与换行](Words%2C%20Paragraphs%2C%20and%20Line%20Breaks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamjwfvjvomi) 介绍词、段落与换行是如何界定的。
- [字符与字素簇](Characters%20and%20Grapheme%20Clusters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4damrvfvjvomi) 介绍如何把字符串拆分成用户所感知的字符。
- [字符集](Character%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dmlkciffeessiindq) 说明如何使用字符集对象，以及如何用 `NSCharacterSet` 的方法创建标准字符集和自定义字符集。
- [扫描器](Scanners.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dolkcineukrshjbbq) 介绍 `NSScanner` 对象，它可以解释 `NSString` 对象中的字符并把它们转换成数值和字符串值。
- [文件路径的字符串表示](String%20Representations%20of%20File%20Paths.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2telkcijbueskhjbea) 介绍那些把字符串当作文件系统路径来操作的 `NSString` 方法。
- [绘制字符串](Drawing%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2tclkcijbuqqkhirdq) 讨论 `NSString` 类中支持直接在 `NSView` 对象里绘制的方法。

更多信息请参阅以下文档：

- _[属性字符串编程指南](../Attributed%20String%20Programming%20Guide/Introduction%20to%20Attributed%20String%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztm2i)_ 与 _字符串编程指南_ 密切相关。它介绍了 `NSAttributedString` 对象，这类对象管理与字符串或单个字符相关联的一组属性（attribute），例如字体和字距。
- _[数据格式化指南](../Data%20Formatting%20Guide/Introduction%20to%20Data%20Formatting%20Programming%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazds2i)_ 介绍如何使用创建、解释和校验文本的对象来格式化数据。
- _[国际化与本地化指南](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_ 介绍如何本地化项目中的字符串，其中包括如何调整字符串格式化参数的顺序。
- Core Foundation 中的 _[Core Foundation 字符串编程指南](../../Core%20Foundation/String%20Programming%20Guide%20for%20Core%20Foundation/Introduction%20to%20Strings%20Programming%20Guide%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeztc2i)_ 讨论 Core Foundation 的不透明类型 CFString，它与 `NSString` 类之间是免费桥接（toll-free bridged）的。
[下一页](Strings.md)

