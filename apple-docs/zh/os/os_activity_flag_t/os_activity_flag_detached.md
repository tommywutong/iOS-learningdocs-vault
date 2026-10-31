---
title: OS_ACTIVITY_FLAG_DETACHED
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_flag_t/os_activity_flag_detached
source_url: 'https://developer.apple.com/documentation/os/os_activity_flag_t/os_activity_flag_detached'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_flag_t/os_activity_flag_detached.json'
content_hash: 'sha256:038fdd712c97d10d'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [os_activity_flag_t](../os_activity_flag_t.md)

# OS_ACTIVITY_FLAG_DETACHED

<sub>枚举 case</sub>

创建一个独立于所提供父活动的新活动。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_ACTIVITY_FLAG_DETACHED
```

## 讨论

在创建活动时设置此标志，系统会将该活动创建为新的顶层活动。如果你提供了父活动，新活动会记录这一事实，让你能够看到是哪个活动触发了新活动，而不会实际建立活动之间的关联。

不要同时传入 [OS_ACTIVITY_FLAG_DETACHED](os_activity_flag_detached.md) 和 [OS_ACTIVITY_FLAG_IF_NONE_PRESENT](os_activity_flag_if_none_present.md)。

## 另请参阅

### 调整活动创建

- [OS_ACTIVITY_FLAG_DEFAULT](os_activity_flag_default.md) — 创建新活动，并将其关联为所提供父活动的子活动。
- [OS_ACTIVITY_FLAG_IF_NONE_PRESENT](os_activity_flag_if_none_present.md) — 仅在尚不存在活动时创建新活动。
