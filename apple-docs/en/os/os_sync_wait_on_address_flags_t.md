---
title: os_sync_wait_on_address_flags_t
framework: os
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_sync_wait_on_address_flags_t
source_url: 'https://developer.apple.com/documentation/os/os_sync_wait_on_address_flags_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_sync_wait_on_address_flags_t.json'
content_hash: 'sha256:1cf0a6b0f70621ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_sync_wait_on_address_flags_t

<sub>Enumeration</sub>

Flags to control futex wait behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef enum { ... } os_sync_wait_on_address_flags_t;
```

## Topics

### Enumeration Cases

- [OS_SYNC_WAIT_ON_ADDRESS_NONE](os_sync_wait_on_address_flags_t/os_sync_wait_on_address_none.md) — Default behavior for futex functions that block a thread.
- [OS_SYNC_WAIT_ON_ADDRESS_SHARED](os_sync_wait_on_address_flags_t/os_sync_wait_on_address_shared.md) — Flag to indicate an address is in a shared memory region, allowing for a futex wake from another process.

## See Also

### Futex Conditional Wait Primitives

- [os_sync_wait_on_address](os_sync_wait_on_address.md) — An atomic compare-and-wait operation, used to implement higher-level synchronization primitives.
- [os_sync_wait_on_address_with_deadline](os_sync_wait_on_address_with_deadline.md) — An atomic compare-and-wait operation with a deadline, used to implement higher-level synchronization primitives.
- [os_sync_wait_on_address_with_timeout](os_sync_wait_on_address_with_timeout.md) — An atomic compare-and-wait operation with a timeout, used to implement higher-level synchronization primitives.
- [os_sync_wake_by_address_all](os_sync_wake_by_address_all.md) — An atomic operation that wakes all threads blocked on a futex wait, used to implement higher-level synchronization primitives.
- [os_sync_wake_by_address_any](os_sync_wake_by_address_any.md) — An atomic operation that wakes one thread blocked on a futex wait, used to implement higher-level synchronization primitives.
- [os_sync_wake_by_address_flags_t](os_sync_wake_by_address_flags_t.md) — Flags to control futex wake behavior.
