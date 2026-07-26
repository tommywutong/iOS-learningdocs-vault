---
title: os_activity_apply
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_apply
source_url: 'https://developer.apple.com/documentation/os/os_activity_apply'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_apply.json'
content_hash: 'sha256:4d9490ab36723f49'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_activity_apply

<sub>Function</sub>

Execute a block using a given activity object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_activity_apply(os_activity_t activity, os_block_t block);
```

## Parameters

- `activity` — An activity object. You can alternatively pass one of the global activity constants, such as [OS_ACTIVITY_NONE](os_activity_none.md) or [OS_ACTIVITY_CURRENT](os_activity_current.md).

- `block` — The block to be executed within the context of the given activity.

## See Also

### Executing an Activity

- [os_activity_apply_f](os_activity_apply_f.md) — Execute a function using a given activity object.
