---
title: OS_SYNC_WAKE_BY_ADDRESS_SHARED
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_sync_wake_by_address_flags_t/os_sync_wake_by_address_shared
source_url: 'https://developer.apple.com/documentation/os/os_sync_wake_by_address_flags_t/os_sync_wake_by_address_shared'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_sync_wake_by_address_flags_t/os_sync_wake_by_address_shared.json'
content_hash: 'sha256:47676082f99d9ba3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [os_sync_wake_by_address_flags_t](../os_sync_wake_by_address_flags_t.md)

# OS_SYNC_WAKE_BY_ADDRESS_SHARED

<sub>Enumeration Case</sub>

A flag to indicate an address is in a shared memory region, allowing you to wake another waiting process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_SYNC_WAKE_BY_ADDRESS_SHARED
```

## Discussion

Use this flag when you pass an address allocated in shared memory to any futex wake function. Shared memory can be used for waits and wakes within a single process, but incur a performance hit.

> [!important] Important
> Use this flag when waking threads which were waited on with the [OS_SYNC_WAIT_ON_ADDRESS_SHARED](../os_sync_wait_on_address_flags_t/os_sync_wait_on_address_shared.md) flag.
