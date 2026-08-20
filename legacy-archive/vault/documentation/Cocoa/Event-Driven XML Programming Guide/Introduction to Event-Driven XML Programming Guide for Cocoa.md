---
title: 事件驱动 XML 编程指南
apple_id: 10000186i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/XMLParsing/XMLParsing.html
archived_at: '2026-07-15T07:21:28.960569Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一篇](Parser%20Capabilities%20and%20Architecture.md)

# Cocoa 事件驱动 XML 编程指南简介

XML 是一种标记语言，允许你使用可任意定义的标签，完全以文本形式描述文档数据的结构。（“XML”是“Extensible Markup Language”，即“可扩展标记语言”的缩写。）约束这种结构的规则由 DTD（Document Type Definition，文档类型定义）等语言模式指定。Cocoa 提供了 NSXMLParser 类，其实例是事件驱动解析器（有时称为流式解析器），可按顺序查找 XML 文档中的结构及任何关联的 DTD 声明。解析器会将找到的内容报告给委托，再由委托处理这些数据。本文档介绍如何使用 NSXMLParser。

本编程主题包括以下文章：

- [解析器功能与架构](Parser%20Capabilities%20and%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dglkcineuqqkijjcq)概述了 Cocoa 流式解析器（NSXMLParser）如何处理 XML 文档，以及它最适合执行哪些任务。
- [XML 解析基础](XML%20Parsing%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dilkcineusssfivea)介绍了使用 NSXMLParser 的基本步骤：创建并初始化实例、响应委托消息以及处理解析错误。
- [处理 XML 元素和属性](Handling%20XML%20Elements%20and%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dklkcineuurshjjeq)提供了处理 XML 属性和元素这两类最常见 XML 结构的建议与示例。
- [处理解析错误](Handling%20Parsing%20Errors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dmlkdjjbesrciizba)介绍如何处理 NSXMLParser 对象在 XML 中发现的错误。
- [使用多个委托](Using%20Multiple%20Delegates.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dolkciffeurcfinba)讨论如何通过为 NSXMLParser 实例使用多个委托，简化 XML 处理并提高处理效率。
- [构建 XML 树结构](Constructing%20XML%20Tree%20Structures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dqlkcineukqkcivcq)提供了使用 NSXMLParser 创建 DOM 风格树的一些建议。
- [验证技巧与方法](Validation%20Tips%20and%20Techniques.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dslkcijbumqsbjbba)提供了使用 NSXMLParser 依据 DTD 或其他模式验证 XML 文档的建议。
- [XML 术语表](XML%20Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3tclkdjjbeiqsiizdq)列出了 NSXMLParser 编程接口中涉及的 XML 和 DTD 术语定义。

许多网站都提供了丰富的 XML、DTD、XML 工具、开源解析器以及相关规范和技术资料。下面列出了其中几个；你也可以在互联网上搜索（例如在搜索框中输入“XML 教程”），找到许多优秀的信息来源：

- 万维网联盟（World Wide Web Consortium）— [http://www.w3.org/](http://www.w3.org/)
- 带注解的 XML 规范（The Annotated XML Specification）— [http://www.xml.com/axml/testaxml.htm](http://www.xml.com/axml/testaxml.htm)
- O’Reilly XML.com — [http://www.xml.com/](http://www.xml.com/)
- Gnome 的 XML 解析器和工具包（libxml）— [http://xmlsoft.org/](http://xmlsoft.org/)

[下一篇](Parser%20Capabilities%20and%20Architecture.md)
