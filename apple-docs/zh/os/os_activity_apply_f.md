---
title: os_activity_apply_f
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_apply_f
source_url: 'https://developer.apple.com/documentation/os/os_activity_apply_f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_apply_f.json'
content_hash: 'sha256:2ef7f5567cefb321'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md)

# os_activity_apply_f

<sub>函数</sub>

使用给定的活动对象执行一个函数。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_activity_apply_f(os_activity_t activity, void *context, os_function_t function);
```

## 参数

- `activity` — 一个活动对象。也可以传入某个全局活动常量，例如 [OS_ACTIVITY_NONE](os_activity_none.md) 或 [OS_ACTIVITY_CURRENT](os_activity_current.md)。

- `context` — 传给函数的上下文。可以为 `NULL`。

- `function` — 要在给定活动的上下文中调用的函数。此函数必须符合 [os_function_t](os_function_t.md) 定义的签名。

## 另请参阅

### 执行活动

- [os_activity_apply](os_activity_apply.md) — 使用给定的活动对象执行一个 block。
