---
title: OS_UNFAIR_LOCK_INIT
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_unfair_lock_init
source_url: 'https://developer.apple.com/documentation/os/os_unfair_lock_init'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_unfair_lock_init.json'
content_hash: 'sha256:5f1609037a119c56'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OS_UNFAIR_LOCK_INIT

<sub>Macro</sub>

A value you use to initialize a new unfair lock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define OS_UNFAIR_LOCK_INIT
```

## See Also

### Unfair Locking

- [os_unfair_lock](os_unfair_lock.md) — A structure that contains the data for an unfair lock.
- [os_unfair_lock_t](os_unfair_lock_t.md) — A pointer to an unfair lock structure.
- [os_unfair_lock_lock](os_unfair_lock_lock.md) — A low-level lock that allows waiters to block efficiently on contention.
- [os_unfair_lock_trylock](os_unfair_lock_trylock.md) — Locks an unfair lock if it is not already locked.
- [os_unfair_lock_lock_with_flags](os_unfair_lock_lock_with_flags.md)
- [os_unfair_lock_unlock](os_unfair_lock_unlock.md) — Unlocks an unfair lock.
- [os_unfair_lock_assert_owner](os_unfair_lock_assert_owner.md) — Triggers an assertion if the calling thread doesn’t own the specified unfair lock.
- [os_unfair_lock_assert_not_owner](os_unfair_lock_assert_not_owner.md) — Triggers an assertion if the calling thread owns the specified unfair lock.
- [os_unfair_lock_flags_t](os_unfair_lock_flags_t.md)
