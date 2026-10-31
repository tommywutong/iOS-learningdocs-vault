---
title: OS_ACTIVITY_NONE
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_none
source_url: 'https://developer.apple.com/documentation/os/os_activity_none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_none.json'
content_hash: 'sha256:1513259a1b2cead1'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OS_ACTIVITY_NONE

<sub>宏</sub>

一个表示不存在活动的特殊值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define OS_ACTIVITY_NONE
```

## 讨论

在创建新活动时，将此值作为活动的父活动传入，即可创建没有父活动的顶级活动。

## 另请参阅

### 选择特殊活动

- [OS_ACTIVITY_CURRENT](os_activity_current.md) — 一个选择当前活动（若存在）的特殊值。
