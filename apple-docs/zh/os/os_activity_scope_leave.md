---
title: os_activity_scope_leave
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_scope_leave
source_url: 'https://developer.apple.com/documentation/os/os_activity_scope_leave'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_scope_leave.json'
content_hash: 'sha256:ac96daa1b82b0a19'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_activity_scope_leave

<sub>函数</sub>

将当前活动恢复到先前保存的状态。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_activity_scope_leave(os_activity_scope_state_t state);
```

## 参数

- `state` — 指向作用域状态结构体的指针，其中保存了你要恢复的执行状态。

## 另请参阅

### 保存和恢复活动状态

- [os_activity_scope_enter](os_activity_scope_enter.md) — 切换当前活动，并保存现有的执行上下文。
- [os_activity_scope_state_t](os_activity_scope_state_t.md) — 包含已保存活动执行上下文的不透明结构体。
