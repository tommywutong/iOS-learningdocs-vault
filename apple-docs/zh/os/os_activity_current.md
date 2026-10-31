---
title: OS_ACTIVITY_CURRENT
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_current
source_url: 'https://developer.apple.com/documentation/os/os_activity_current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_current.json'
content_hash: 'sha256:f8f32de6205c7fb6'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OS_ACTIVITY_CURRENT

<sub>宏</sub>

一个特殊值，用于在存在当前活动时选中该活动。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define OS_ACTIVITY_CURRENT
```

## 讨论

创建新活动时，将此值作为活动的父活动传入，即可让新活动以当前活动作为父活动。如果不存在活跃的活动，创建函数会把新活动作为没有父活动的顶层活动返回。

## 另请参阅

### 选择特殊活动

- [OS_ACTIVITY_NONE](os_activity_none.md) — 一个表示不存在活动的特殊值。
