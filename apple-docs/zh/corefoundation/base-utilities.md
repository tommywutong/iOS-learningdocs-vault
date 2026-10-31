---
title: 基础实用工具
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/base-utilities
source_url: 'https://developer.apple.com/documentation/corefoundation/base-utilities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/base-utilities.json'
content_hash: 'sha256:0cf3ce3fef34d977'
translated: true
---

> 导航： [技术](../technologies.md) · [Core Foundation](../corefoundation.md)

# 基础实用工具

<sub>API 集合</sub>

## 概述

Core Foundation 定义了若干杂项符号，它们要么被多种不透明类型使用（例如 [CFIndex](cfindex.md)），要么适用于整个 Core Foundation（例如 [kCFCoreFoundationVersionNumber](kcfcorefoundationversionnumber.md)）。这些符号集中在此一并说明。

## 主题

### Core Foundation 基础实用工具杂项函数

- [CFRangeMake](<cfrangemake(____).md>) — 声明并初始化一个 `CFRange` 结构体。

### 回调

- [CFComparatorFunction](cfcomparatorfunction.md) — 比较两个值的回调函数。你在某些 Core Foundation 排序函数中提供指向此回调的指针。

### 数据类型

- [CFIndex](cfindex.md) — 用于 kAXPriorityKey 的优先级值
- [CFOptionFlags](cfoptionflags.md) — 用于向 Core Foundation 函数传入特殊分配及其他请求的位域。
- [CFRange](cfrange.md) — 表示容器中连续项范围的结构体，例如缓冲区中的字符或集合中的元素。

### 常量

- [CFComparisonResult](cfcomparisonresult.md) — 比较函数返回的常量，指示某个值等于、小于还是大于另一个值。
- [未找到值](value-not-found.md) — 当 Core Foundation 函数无法定位所请求的值时返回的特殊值。
- [当前框架版本号](current-framework-version-number.md) — Core Foundation 框架的当前版本号。
- [框架版本号](framework-version-numbers.md) — Core Foundation 框架的版本号。

## 另请参阅

### 相关文档

- [Core Foundation 设计概念](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/CFDesignConcepts.html#//apple_ref/doc/uid/10000122i)

### 实用工具

- [字节序实用工具](byte-order-utilities.md)
- [Core Foundation URL 访问实用工具](core-foundation-url-access-utilities.md)
- [偏好设置实用工具](preferences-utilities.md)
- [套接字名称服务器实用工具](socket-name-server-utilities.md)
- [时间实用工具](time-utilities.md)
