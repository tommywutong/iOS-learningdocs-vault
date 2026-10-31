---
title: os_activity_create
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_create
source_url: 'https://developer.apple.com/documentation/os/os_activity_create'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_create.json'
content_hash: 'sha256:824fb2d59df4d114'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md)

# os_activity_create

<sub>宏</sub>

创建一个新的活动对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_activity_create(description, parent_activity, flags)
```

## 参数

- `description` — 描述该活动的 C 字符串。该描述必须是调用可执行文件或库内的常量字符串。

- `parent_activity` — 表示父活动的 [os_activity_t](os_activity_t.md) 对象。也可以传入 [OS_ACTIVITY_NONE](os_activity_none.md) 或 [OS_ACTIVITY_CURRENT](os_activity_current.md)。

- `flags` — 创建新活动时使用的标志。某些标志会覆盖 parent_activity 参数；参见 [os_activity_flag_t](os_activity_flag_t.md)。

## 返回值

新活动的 [os_activity_t](os_activity_t.md) 对象。

## 讨论

要执行新活动，请调用 [os_activity_apply](os_activity_apply.md) 函数。

## 另请参阅

### 创建活动

- [os_activity_initiate](os_activity_initiate.md) — 使用提供的 block 同步执行一个新活动。
- [os_activity_initiate_f](os_activity_initiate_f.md) — 使用提供的函数同步执行一个新活动。
- [os_activity_label_useraction](os_activity_label_useraction.md) — 为 AppKit 或 UIKit 自动生成的活动添加标签。
- [os_activity_flag_t](os_activity_flag_t.md) — 在创建活动时调整行为的标志。
