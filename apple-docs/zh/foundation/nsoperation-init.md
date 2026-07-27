---
title: init
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsoperation-init
source_url: 'https://developer.apple.com/documentation/foundation/nsoperation-init'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsoperation-init.json'
content_hash: 'sha256:ba7f564f1103efb7'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [进程与线程](processes-and-threads.md) · [Operation](operation.md)

# init

<sub>文章</sub>

返回已初始化的 `NSOperation` 对象。

## 概述

你的自定义子类必须调用此方法。默认实现会初始化对象的实例变量，并为使用它做好准备。此方法在当前线程上运行，也就是你用于分配操作对象的线程。

## 另请参阅

### 相关文档

- [并发编程指南](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091)
