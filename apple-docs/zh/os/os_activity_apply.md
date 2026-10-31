---
title: os_activity_apply
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_apply
source_url: 'https://developer.apple.com/documentation/os/os_activity_apply'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_apply.json'
content_hash: 'sha256:4d9490ab36723f49'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md)

# os_activity_apply

<sub>函数</sub>

使用给定的活动对象执行一个 block。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_activity_apply(os_activity_t activity, os_block_t block);
```

## 参数

- `activity` — 一个活动对象。也可以传入某个全局活动常量，例如 [OS_ACTIVITY_NONE](os_activity_none.md) 或 [OS_ACTIVITY_CURRENT](os_activity_current.md)。

- `block` — 要在给定活动的上下文中执行的 block。

## 另请参阅

### 执行活动

- [os_activity_apply_f](os_activity_apply_f.md) — 使用给定的活动对象执行一个函数。
