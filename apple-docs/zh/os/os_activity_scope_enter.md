---
title: os_activity_scope_enter
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_scope_enter
source_url: 'https://developer.apple.com/documentation/os/os_activity_scope_enter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_scope_enter.json'
content_hash: 'sha256:317ae5734c5351af'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_activity_scope_enter

<sub>函数</sub>

切换当前活动，并保存现有的执行上下文。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_activity_scope_enter(os_activity_t activity, os_activity_scope_state_t state);
```

## 参数

- `activity` — 一个活动对象。你也可以传入某个全局活动常量，例如 [OS_ACTIVITY_NONE](os_activity_none.md) 或 [OS_ACTIVITY_CURRENT](os_activity_current.md)。

- `state` — 指向作用域状态结构体的指针，用于保存当前执行上下文。

## 讨论

请在调用此函数的那个函数中把该结构体分配在栈上，并在离开包含该结构体的作用域之前调用 [os_activity_scope_leave](os_activity_scope_leave.md)。

## 另请参阅

### 保存和恢复活动状态

- [os_activity_scope_leave](os_activity_scope_leave.md) — 将当前活动恢复到先前保存的状态。
- [os_activity_scope_state_t](os_activity_scope_state_t.md) — 包含已保存活动执行上下文的不透明结构体。
