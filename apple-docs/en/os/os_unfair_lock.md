---
title: os_unfair_lock
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_unfair_lock
source_url: 'https://developer.apple.com/documentation/os/os_unfair_lock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_unfair_lock.json'
content_hash: 'sha256:8cfca699923686a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_unfair_lock

<sub>Type Alias</sub>

A structure that contains the data for an unfair lock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef struct os_unfair_lock_s os_unfair_lock;
```

## Discussion

To create a lock, allocate a variable of this type and initialize it to [OS_UNFAIR_LOCK_INIT](os_unfair_lock_init.md).

## See Also

### Unfair Locking

- [OS_UNFAIR_LOCK_INIT](os_unfair_lock_init.md) — A value you use to initialize a new unfair lock.
- [os_unfair_lock_t](os_unfair_lock_t.md) — A pointer to an unfair lock structure.
- [os_unfair_lock_lock](os_unfair_lock_lock.md) — A low-level lock that allows waiters to block efficiently on contention.
- [os_unfair_lock_trylock](os_unfair_lock_trylock.md) — Locks an unfair lock if it is not already locked.
- [os_unfair_lock_lock_with_flags](os_unfair_lock_lock_with_flags.md)
- [os_unfair_lock_unlock](os_unfair_lock_unlock.md) — Unlocks an unfair lock.
- [os_unfair_lock_assert_owner](os_unfair_lock_assert_owner.md) — Triggers an assertion if the calling thread doesn’t own the specified unfair lock.
- [os_unfair_lock_assert_not_owner](os_unfair_lock_assert_not_owner.md) — Triggers an assertion if the calling thread owns the specified unfair lock.
- [os_unfair_lock_flags_t](os_unfair_lock_flags_t.md)
