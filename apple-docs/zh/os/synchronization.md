---
title: 同步
framework: os
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/os/synchronization
source_url: 'https://developer.apple.com/documentation/os/synchronization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/synchronization.json'
content_hash: 'sha256:b1b55c8cdbc98a5d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md)

# 同步

<sub>API 集合</sub>

访问底层同步机制，控制线程间的状态。

## 概述

> [!note] 注意
> 尽可能使用更高层的同步原语，例如 `pthread`、Grand Central Dispatch，或 Swift 的并发特性，来控制不同线程间对状态的访问。详见 [Updating an App to Use Swift Concurrency](../swift/updating_an_app_to_use_swift_concurrency.md)。

## 主题

### Swift 包装器

- [OSAllocatedUnfairLock](osallocatedunfairlock.md) — 一个创建 unfair lock 的结构体。
- [OSAllocatedUnfairLockFlags](osallocatedunfairlockflags.md)
