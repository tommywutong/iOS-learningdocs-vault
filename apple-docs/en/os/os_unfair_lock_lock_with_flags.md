---
title: os_unfair_lock_lock_with_flags
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_unfair_lock_lock_with_flags
source_url: 'https://developer.apple.com/documentation/os/os_unfair_lock_lock_with_flags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_unfair_lock_lock_with_flags.json'
content_hash: 'sha256:476690ac2098770d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_unfair_lock_lock_with_flags

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_unfair_lock_lock_with_flags(os_unfair_lock_t lock, os_unfair_lock_flags_t flags);
```

## See Also

### Unfair Locking

- [os_unfair_lock](os_unfair_lock.md) — A structure that contains the data for an unfair lock.
- [OS_UNFAIR_LOCK_INIT](os_unfair_lock_init.md) — A value you use to initialize a new unfair lock.
- [os_unfair_lock_t](os_unfair_lock_t.md) — A pointer to an unfair lock structure.
- [os_unfair_lock_lock](os_unfair_lock_lock.md) — A low-level lock that allows waiters to block efficiently on contention.
- [os_unfair_lock_trylock](os_unfair_lock_trylock.md) — Locks an unfair lock if it is not already locked.
- [os_unfair_lock_unlock](os_unfair_lock_unlock.md) — Unlocks an unfair lock.
- [os_unfair_lock_assert_owner](os_unfair_lock_assert_owner.md) — Triggers an assertion if the calling thread doesn’t own the specified unfair lock.
- [os_unfair_lock_assert_not_owner](os_unfair_lock_assert_not_owner.md) — Triggers an assertion if the calling thread owns the specified unfair lock.
- [os_unfair_lock_flags_t](os_unfair_lock_flags_t.md)
