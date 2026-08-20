---
title: 事件驱动 XML 编程指南
apple_id: 10000186i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/XMLParsing/Articles/ParserArchitecture.html
archived_at: '2026-07-15T07:21:26.473180Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [事件驱动 XML 编程指南](Introduction%20to%20Event-Driven%20XML%20Programming%20Guide%20for%20Cocoa.md)


[下一篇](XML%20Parsing%20Basics.md) [上一篇](Introduction%20to%20Event-Driven%20XML%20Programming%20Guide%20for%20Cocoa.md)

# 解析器功能与架构

解析和处理 XML 通常有两种方法，各自采用不同风格的 API：

- _基于树的 API_：这种方法将 XML 文档映射为符合模式所描述逻辑结构的内部树结构，随后可方便地导航和操作该树。已有许多基于树的 API，其中包括万维网联盟（W3C）提出的 DOM（Document Object Model，文档对象模型）。XML 路径语言（XPath）、XML 包含（XInclude）和 XML 指针语言（XPointer）都是 W3C 用于查询和处理 DOM 风格树结构中 XML 的编程接口。
- _事件驱动 API_：采用这种方法时，解析器在遇到解析事件（例如每个元素的开始和结束）时，便将事件报告给应用程序。在基于 C 的 API 中，这类报告通过应用程序实现的回调完成，以处理各种事件。SAX 是这种解析 API 风格中最著名的示例。这类解析器有时也称为流式解析器。

NSXMLParser 类采用事件驱动的解析方式。但 NSXMLParser 对象（简称解析器）不使用回调，而是向其委托发送消息；每种解析事件都会对应一条不同的消息。解析器按顺序遇到 XML 或 DTD 文件中的各个项目——元素、属性、声明、实体引用等——时，会连同相关上下文一起将其报告给委托（前提是委托实现了对应方法）。除报告之外，解析器不会对该项目进行任何处理。

例如，假设你有如下简单的 XML 文件：

```xml
<?xml version="1.0" encoding="UTF8"?>
<article author="John Doe">
    <para>This is a very short article.</para>
</article>
```

解析器会向其委托报告以下一系列事件：

1. 开始解析文档
2. 找到元素 `article` 的开始标签
3. 找到元素 `article` 的属性 `author`，值为“John Doe”
4. 找到元素 `para` 的开始标签
5. 找到字符 `This is a very short article.`
6. 找到元素 `para` 的结束标签
7. 找到元素 `article` 的结束标签
8. 结束解析文档

基于树和基于事件的解析方法各有优缺点。构建表示 XML 文档的内部树可能需要大量内存，文档较大时尤其如此。如果还需要将解析所得文档的树结构映射为类型更明确、面向特定应用程序的树结构，这个问题会更加突出。

事件驱动解析每次只处理一个 XML 结构，而不是同时处理全部结构，因此比基于树的解析占用少得多的内存。它非常适合重视性能、且无须修改已解析 XML 的场景。事件驱动解析的一种应用方式，是在 XML 文档存储库（甚至是包含多条“记录”的单个 XML 文档）中搜索特定元素，并对元素内容执行操作。例如，你可以使用 NSXMLParser 搜索 Bonjour 网络中所有计算机上的属性列表偏好设置文件，以收集网络配置信息。

对于需要对 XML 执行复杂用户查询，或需要修改 XML 并将其写回文件的任务，事件驱动解析就不太适合。NSXMLParser 之类的事件驱动解析器也不会协助完成验证（即检查 XML 是否符合 DTD 或其他模式中指定的结构规则）。这类任务需要 DOM 风格的树。不过，你可以使用 NSXMLParser 等事件驱动解析器自行构建内部树结构。

除报告解析事件外，NSXMLParser 对象还会验证 XML 或 DTD 是否格式良好。例如，它会检查元素的开始标签是否有匹配的结束标签，以及属性是否已赋值。如果遇到任何此类语法错误，解析器会停止解析并通知委托。

虽然解析器在标记语言层面只“理解”XML 和 DTD，但它可以解析任何基于 XML 的语言模式，例如 RELAX NG 和 XML Schema。

[下一篇](XML%20Parsing%20Basics.md) [上一篇](Introduction%20to%20Event-Driven%20XML%20Programming%20Guide%20for%20Cocoa.md)
