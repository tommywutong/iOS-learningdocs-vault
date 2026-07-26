---
title: os_sync_wake_by_address_any
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_sync_wake_by_address_any
source_url: 'https://developer.apple.com/documentation/os/os_sync_wake_by_address_any'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_sync_wake_by_address_any.json'
content_hash: 'sha256:50475f222b0d1d46'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_sync_wake_by_address_any

<sub>Function</sub>

An atomic operation that wakes one thread blocked on a futex wait, used to implement higher-level synchronization primitives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_sync_wake_by_address_any(void *addr, size_t size, os_sync_wake_by_address_flags_t flags);
```

## Parameters

- `addr` — The user-space address waited on to wake. This address must be aligned to `size`.

- `size` — The size of the wait value, in bytes. Values can be 4 or 8 bytes, where 4-byte values use the lower bytes of `value`.

- `flags` — Flags for the operation.

## Return Value

Returns 0 on success, and -1 on error with `errno` set.

## Discussion

This function wakes a single thread waiting on `addr`. There’s no guarantee which thread wakes in the case of multiple waiters.

Pass consistent values across wait and wake APIs for `addr`, `size`, and `flags`. See [os_sync_wake_by_address_flags_t](os_sync_wake_by_address_flags_t.md) for details.

> [!important] Important
> Use this function only for implementing synchronization primitives that don’t have a sense of ownership, such as condition variables or semaphores. In particular, this function doesn’t provide priority inversion avoidance. For locking APIs, use existing OS primitives, such as `pthread` threads or [Unfair Locking](synchronization.md#Unfair-Locking) APIs. For synchronization and threading managed by the OS, use a higher-level API, such as [Dispatch](../dispatch.md).

### Error Codes

When this function returns `-1`, the global `errno` contains one of these values, indicating the corresponding error.

| Error code | Description |
|---|---|
| `EINVAL` | Invalid flags or size.![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)The `addr` passed is NULL.![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)The operation associated with the existing kernel state at `addr` is inconsistent with other function arguments. |
| `ENOENT` | There are no compare-and-wait operations on `addr`. |
| `EDOM` | The `addr` is in use for non-compare-and-wait synchronization. |

## See Also

### Futex Conditional Wait Primitives

- [os_sync_wait_on_address](os_sync_wait_on_address.md) — An atomic compare-and-wait operation, used to implement higher-level synchronization primitives.
- [os_sync_wait_on_address_with_deadline](os_sync_wait_on_address_with_deadline.md) — An atomic compare-and-wait operation with a deadline, used to implement higher-level synchronization primitives.
- [os_sync_wait_on_address_with_timeout](os_sync_wait_on_address_with_timeout.md) — An atomic compare-and-wait operation with a timeout, used to implement higher-level synchronization primitives.
- [os_sync_wait_on_address_flags_t](os_sync_wait_on_address_flags_t.md) — Flags to control futex wait behavior.
- [os_sync_wake_by_address_all](os_sync_wake_by_address_all.md) — An atomic operation that wakes all threads blocked on a futex wait, used to implement higher-level synchronization primitives.
- [os_sync_wake_by_address_flags_t](os_sync_wake_by_address_flags_t.md) — Flags to control futex wake behavior.
