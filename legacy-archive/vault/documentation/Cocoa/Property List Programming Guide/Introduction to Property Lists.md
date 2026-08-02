---
title: 属性列表编程指南
apple_id: 10000048i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html
archived_at: '2026-07-15T07:18:02.569123Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Quick%20Start%20for%20Property%20Lists.md)

# 属性列表简介

属性列表（property list）借助若干种对象类型，把数据组织成带名字的值以及值的列表。这些类型让你能够生成结构清晰、便于传输、便于存储、便于访问，同时又尽可能高效的数据。运行在 OS X 和 iOS 上的应用程序频繁使用属性列表。Cocoa 和 Core Foundation 提供的属性列表编程接口，可以把这些基本对象类型按层次结构组合起来，并在它们与标准 XML 之间相互转换。你可以把 XML 数据保存到磁盘，之后再用它重建原来的对象。

本文档介绍属性列表及其各种表示形式，以及如何使用 Cocoa 的若干 Foundation 类和 Core Foundation 的 Property List Services 来操作属性列表。

本文档包含以下章节：

- [属性列表快速入门](Quick%20Start%20for%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2jninedilktk42q) 是一份属性列表的小教程，让你亲手体验 XML 属性列表和 Objective-C 序列化 API。
- [关于属性列表](About%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2jninedglktk4za) 解释什么是属性列表，以及什么时候应该使用它。
- [以编程方式创建属性列表](Creating%20Property%20Lists%20Programmatically.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2jninedklktk4yq) 展示如何用 Cocoa 和 Core Foundation 的 API 创建具有层次结构的属性列表。
- [理解 XML 属性列表](Understanding%20XML%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2jninedmlktk4yq) 介绍 XML 属性列表的格式。
- [序列化属性列表](Serializing%20a%20Property%20List.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2jninedolktk4yq) 讨论如何在属性列表的运行时表示与静态表示之间进行序列化和反序列化。
- [读写属性列表数据](Reading%20and%20Writing%20Property-List%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2jninedqlktk4yq) 介绍如何把属性列表保存到文件或 URL 资源，以及之后如何恢复它们。
- [旧式 ASCII 属性列表](Old-Style%20ASCII%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgaytelkcijbuerccjjcq) 是一份附录，介绍旧式（OpenStep）ASCII 属性列表的格式。

[下一页](Quick%20Start%20for%20Property%20Lists.md)

