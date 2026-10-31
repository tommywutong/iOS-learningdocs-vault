---
title: os_activity_initiate_f
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_initiate_f
source_url: 'https://developer.apple.com/documentation/os/os_activity_initiate_f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_initiate_f.json'
content_hash: 'sha256:397fa6d69c8d6972'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_activity_initiate_f

<sub>宏</sub>

使用所提供的函数同步执行一个新活动。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_activity_initiate_f(description, flags, context, function)
```

## 参数

- `description` — 描述该活动的 C 字符串。描述必须是调用方可执行文件或库内的常量字符串。

- `flags` — 定义应如何创建该活动的标志。请参阅 [os_activity_flag_t](os_activity_flag_t.md)。

- `context` — 要传给该函数的上下文。可以为 `NULL`。

- `function` — 在给定活动的上下文中调用的函数。此函数必须匹配 [os_function_t](os_function_t.md) 所定义的签名。

## 讨论

此函数会隐式创建一个新的活动对象，作为当前线程上当前活动对象的子活动。该对象会在活动 block 的执行期间一直存在。

## 另请参阅

### 创建活动

- [os_activity_initiate](os_activity_initiate.md) — 使用所提供的 block 同步执行一个新活动。
- [os_activity_create](os_activity_create.md) — 创建一个新的活动对象。
- [os_activity_label_useraction](os_activity_label_useraction.md) — 为 AppKit 或 UIKit 自动生成的活动添加标签。
- [os_activity_flag_t](os_activity_flag_t.md) — 在创建活动时调整行为的标志。
