---
title: OS_ACTIVITY_FLAG_IF_NONE_PRESENT
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_flag_t/os_activity_flag_if_none_present
source_url: 'https://developer.apple.com/documentation/os/os_activity_flag_t/os_activity_flag_if_none_present'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_flag_t/os_activity_flag_if_none_present.json'
content_hash: 'sha256:5c32b336638dfdeb'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [os_activity_flag_t](../os_activity_flag_t.md)

# OS_ACTIVITY_FLAG_IF_NONE_PRESENT

<sub>枚举 case</sub>

仅在尚不存在活动时创建新活动。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_ACTIVITY_FLAG_IF_NONE_PRESENT
```

## 讨论

在调用用于创建活动的函数时包含此标志：如果活动已存在，该函数会返回该活动；否则，函数会创建并返回一个新活动。

不要同时传入 [OS_ACTIVITY_FLAG_DETACHED](os_activity_flag_detached.md) 和 [OS_ACTIVITY_FLAG_IF_NONE_PRESENT](os_activity_flag_if_none_present.md)。

## 另请参阅

### 调整活动创建

- [OS_ACTIVITY_FLAG_DEFAULT](os_activity_flag_default.md) — 创建新活动，并将其关联为所提供父活动的子活动。
- [OS_ACTIVITY_FLAG_DETACHED](os_activity_flag_detached.md) — 创建一个独立于所提供父活动的新活动。
