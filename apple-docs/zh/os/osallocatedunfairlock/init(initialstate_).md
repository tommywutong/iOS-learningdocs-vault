---
title: 'init(initialState:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osallocatedunfairlock/init(initialstate:)'
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/init(initialstate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/init%28initialstate%3A%29.json'
content_hash: 'sha256:b8b1ea93a1581fde'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# init(initialState:)

<sub>初始化方法</sub>

创建一个维护并保护状态数据的锁对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(initialState: State)
```

## 参数

- `initialState` — 操作的起始状态。

## 另请参阅

### 创建锁对象

- [init()](<init().md>) — 创建一个不保护状态数据的锁对象。
