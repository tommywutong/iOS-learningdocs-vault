---
title: 原子存储编程主题
apple_id: TP40004521
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2011-10-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AtomicStore_Concepts/Introduction/Introduction.html
archived_at: '2026-07-15T05:25:48.212658Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[下一页](Atomic%20Store%20Fundamentals.md)

# 原子存储编程主题简介

本文档介绍如何使用原子存储（atomic store）API，为 Core Data 应用程序创建自定义持久化存储。

如果你想创建一个由自己管理文件格式的 Core Data 持久化存储，就应该阅读本文档。

这不是一个入门级主题。你必须熟悉《Core Data Basics》和《Persistent Store Features》中所述的 Core Data 架构，并了解 Objective-C 类的设计与实现。你还必须理解自己的文件格式，以及如何读取、解析和写入你想要支持的文件。

本文档包含以下几篇文章：

- [原子存储基础](Atomic%20Store%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmrwfvjvomi) 介绍了原子存储的基本概念。
- [原子存储生命周期](Atomic%20Store%20Life-cycle.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmrxfvjvomi) 介绍了原子存储的生命周期。阅读本文可以了解在什么时机会调用存储的哪些方法，以及存储应该如何响应这些调用。这有助于你理解如何实现一个自定义存储。
- [注册自定义存储类型](Registering%20a%20Custom%20Store%20Type.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgmbrfvjvomi) 介绍了如何注册一个自定义的原子存储类型。
- [初始化存储与加载数据](Initializing%20a%20Store%20and%20Loading%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2teojyfvjvomi) 介绍了如何为自定义原子存储进行初始化并加载数据。

[下一页](Atomic%20Store%20Fundamentals.md)

