---
title: OS_SYNC_WAKE_BY_ADDRESS_NONE
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_sync_wake_by_address_flags_t/os_sync_wake_by_address_none
source_url: 'https://developer.apple.com/documentation/os/os_sync_wake_by_address_flags_t/os_sync_wake_by_address_none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_sync_wake_by_address_flags_t/os_sync_wake_by_address_none.json'
content_hash: 'sha256:7b215a9f1150912a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [os_sync_wake_by_address_flags_t](../os_sync_wake_by_address_flags_t.md)

# OS_SYNC_WAKE_BY_ADDRESS_NONE

<sub>Enumeration Case</sub>

The default behavior for futex functions that wake a thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_SYNC_WAKE_BY_ADDRESS_NONE
```

## Discussion

Use this flag when you pass an address only accessed in the calling process’s memory space. This flag enables kernel optimizations that can’t be used on shared memory.
