---
title: os_activity_scope_state_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_scope_state_t
source_url: 'https://developer.apple.com/documentation/os/os_activity_scope_state_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_scope_state_t.json'
content_hash: 'sha256:cc57ca9818dc9245'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_activity_scope_state_t

<sub>类型别名</sub>

一个包含已保存的活动执行上下文的不透明结构。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef struct os_activity_scope_state_s * os_activity_scope_state_t;
```

## 主题

### 实例属性

- [opaque](os_activity_scope_state_s/opaque.md) — 系统用来存储执行状态的不透明数据。

## 另请参阅

### 保存和恢复活动状态

- [os_activity_scope_enter](os_activity_scope_enter.md) — 切换当前活动，并保存现有的执行上下文。
- [os_activity_scope_leave](os_activity_scope_leave.md) — 将当前活动恢复到之前保存的状态。
