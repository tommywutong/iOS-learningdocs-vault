---
title: os_unfair_lock_assert_not_owner
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_unfair_lock_assert_not_owner
source_url: 'https://developer.apple.com/documentation/os/os_unfair_lock_assert_not_owner'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_unfair_lock_assert_not_owner.json'
content_hash: 'sha256:cada18c6ce40e37d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_unfair_lock_assert_not_owner

<sub>Function</sub>

Triggers an assertion if the calling thread owns the specified unfair lock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_unfair_lock_assert_not_owner(const os_unfair_lock *lock);
```

## Parameters

- `lock` — A pointer to the unfair lock to check.

## Discussion

If the lock is unlocked or owned by a thread other than the calling thread, this function returns normally. If the lock is currently owned by the calling thread, this function asserts and terminates the process.

## See Also

### Unfair Locking

- [os_unfair_lock](os_unfair_lock.md) — A structure that contains the data for an unfair lock.
- [OS_UNFAIR_LOCK_INIT](os_unfair_lock_init.md) — A value you use to initialize a new unfair lock.
- [os_unfair_lock_t](os_unfair_lock_t.md) — A pointer to an unfair lock structure.
- [os_unfair_lock_lock](os_unfair_lock_lock.md) — A low-level lock that allows waiters to block efficiently on contention.
- [os_unfair_lock_trylock](os_unfair_lock_trylock.md) — Locks an unfair lock if it is not already locked.
- [os_unfair_lock_lock_with_flags](os_unfair_lock_lock_with_flags.md)
- [os_unfair_lock_unlock](os_unfair_lock_unlock.md) — Unlocks an unfair lock.
- [os_unfair_lock_assert_owner](os_unfair_lock_assert_owner.md) — Triggers an assertion if the calling thread doesn’t own the specified unfair lock.
- [os_unfair_lock_flags_t](os_unfair_lock_flags_t.md)
