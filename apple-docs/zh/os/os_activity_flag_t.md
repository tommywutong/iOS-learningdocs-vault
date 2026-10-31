---
title: os_activity_flag_t
framework: os
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_flag_t
source_url: 'https://developer.apple.com/documentation/os/os_activity_flag_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_flag_t.json'
content_hash: 'sha256:73737929dd04b45e'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_activity_flag_t

<sub>枚举</sub>

在你创建活动时用于调整行为的标志。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef enum { ... } os_activity_flag_t;
```

## 主题

### 调整活动创建

- [OS_ACTIVITY_FLAG_DEFAULT](os_activity_flag_t/os_activity_flag_default.md) — 创建新活动，并将其关联为所提供父活动的子活动。
- [OS_ACTIVITY_FLAG_DETACHED](os_activity_flag_t/os_activity_flag_detached.md) — 创建一个独立于所提供父活动的新活动。
- [OS_ACTIVITY_FLAG_IF_NONE_PRESENT](os_activity_flag_t/os_activity_flag_if_none_present.md) — 仅在尚不存在活动时创建新活动。

## 另请参阅

### 创建活动

- [os_activity_initiate](os_activity_initiate.md) — 使用所提供的 block 同步执行一个新活动。
- [os_activity_initiate_f](os_activity_initiate_f.md) — 使用所提供的函数同步执行一个新活动。
- [os_activity_create](os_activity_create.md) — 创建一个新的活动对象。
- [os_activity_label_useraction](os_activity_label_useraction.md) — 为 AppKit 或 UIKit 自动生成的活动添加标签。
