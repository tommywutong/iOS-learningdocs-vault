---
title: os_activity_initiate
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_initiate
source_url: 'https://developer.apple.com/documentation/os/os_activity_initiate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_initiate.json'
content_hash: 'sha256:db4f220205b6c7d6'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_activity_initiate

<sub>宏</sub>

使用所提供的 block 同步执行一个新活动。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_activity_initiate(description, flags, activity_block)
```

## 参数

- `description` — 描述该活动的 C 字符串。该描述必须是调用方可执行文件或库内的常量字符串。

- `flags` — 定义应如何创建活动的标志。参见 [os_activity_flag_t](os_activity_flag_t.md)。

- `activity_block` — 包含要为该活动执行的代码的 block。

## 讨论

此函数会隐式创建一个新的活动对象，作为当前线程上当前活动对象的子活动。该对象在 activity block 执行期间持续存在。

## 另请参阅

### 创建活动

- [os_activity_initiate_f](os_activity_initiate_f.md) — 使用所提供的函数同步执行一个新活动。
- [os_activity_create](os_activity_create.md) — 创建一个新的活动对象。
- [os_activity_label_useraction](os_activity_label_useraction.md) — 为 AppKit 或 UIKit 自动生成的活动添加标签。
- [os_activity_flag_t](os_activity_flag_t.md) — 在你创建活动时用于调整行为的标志。
