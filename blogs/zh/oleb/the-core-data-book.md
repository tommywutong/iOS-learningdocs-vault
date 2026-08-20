---
title: Core Data 图书
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2015/12/core-data-book/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:781c0872d601e54d'
translated: true
---

> 原文：[The Core Data Book](https://oleb.net/blog/2015/12/core-data-book/)　·　Ole Begemann

# Core Data 图书

[![Core Data Book Cover](https://oleb.net/media/core-data-book-cover.png)](https://www.objc.io/books/core-data/)

Florian Kugler 和 Daniel Eggert 合著的 [Core Data 新书](https://www.objc.io/books/core-data/) 现已发布。我作为技术审阅者也参与了一小部分。

我最欣赏这本书的一点是，它远不止是一本各种特性的操作指南集合。Florian 和 Daniel 解释了 Core Data 各个层级（从托管对象上下文（managed object context）到底层持久化存储（persistent store））实际的工作原理。他们教你如何运用这些知识，为你的 App 选择合适的并发（concurrency）模型（没有唯一的正确答案），并避免性能陷阱。

在并发与同步的部分，他们讨论了大量你在别处找不到如此详细的内容。（示例 App 使用 CloudKit 作为服务器组件，但它完全适用于任何其他典型的 Web 服务。）

我非常享受与 Daniel 和 Florian 在这个项目上的合作。我从他们身上学到了很多，不仅关于 Core Data，还包括 App 架构。例如，他们为同步引擎编写了一个抽象层，使其可以将对 CloudKit 的调用替换为另一个仅记录应发送给服务器的命令的实现。这个最初为了让读者无需配置问题即可运行示例 App 的权宜之计，最终演变成了可用于测试的东西。

作者们已全面采用 Swift。示例代码是用 Swift 有效使用 Cocoa 的绝佳学习资源。Daniel 和 Florian 教授了一些不错的模式，使 Cocoa API（不仅仅是 Core Data）从 Swift 调用时更安全、更愉悦。

我强烈推荐这本书。
