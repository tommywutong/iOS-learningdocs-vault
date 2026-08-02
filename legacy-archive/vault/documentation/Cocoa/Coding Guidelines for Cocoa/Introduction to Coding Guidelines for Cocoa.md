---
title: Cocoa 编码规范
apple_id: 10000146i
resource_type: Guide
platform: watchOS|iOS|macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CodingGuidelines/CodingGuidelines.html
archived_at: '2026-07-15T07:13:28.315885Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Code%20Naming%20Basics.md)

# Cocoa 编码规范简介

开发带有公开 API 的 [Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) [框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)、插件或其他可执行文件时，所采用的思路和约定与开发应用程序时有所不同。你的产品的主要客户是开发者，因此绝不能让他们对你的编程接口感到困惑。这正是 API 命名规范（naming convention）的用武之地，它能帮助你把接口写得一致而清晰。此外还有一些编程技术是框架所特有的，或者说在框架中格外重要，例如版本管理、二进制兼容性、错误处理和[内存管理](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)。本主题既介绍 Cocoa 的命名规范，也介绍针对框架的推荐编程实践。

本主题包含的文章大致分为两类。第一类篇幅较大，介绍编程接口的命名[规范](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/CodingConventions.html#//apple_ref/doc/uid/TP40008195-CH53)。Apple 自己的 Cocoa 框架采用的正是这套规范（少数细节除外）。介绍命名规范的文章包括：

- [代码命名基础](Code%20Naming%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dclkcijbuqqsgifea)
- [方法命名](Naming%20Methods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4delkcineuoskkjjda)
- [函数命名](Naming%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dglkciffeor2difca)
- [属性与数据类型命名](Naming%20Properties%20and%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dilkciffeoskjjjcq)
- [可接受的缩写与首字母缩略词](Acceptable%20Abbreviations%20and%20Acronyms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dklkcineuqq2hifcq)

第二类（目前只有一篇）讨论框架编程的若干方面：

- [框架开发者的提示与技巧](Tips%20and%20Techniques%20for%20Framework%20Developers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dmlkciffesqsgjbca)

[下一页](Code%20Naming%20Basics.md)

