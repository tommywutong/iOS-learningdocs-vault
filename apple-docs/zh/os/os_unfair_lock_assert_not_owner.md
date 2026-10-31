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
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_unfair_lock_assert_not_owner

<sub>函数</sub>

如果调用线程拥有指定的 unfair lock，则触发断言。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_unfair_lock_assert_not_owner(const os_unfair_lock *lock);
```

## 参数

- `lock` — 指向要检查的 unfair lock 的指针。

## 讨论

如果该锁未锁定，或由调用线程以外的其他线程拥有，此函数正常返回。如果该锁当前由调用线程拥有，此函数会断言并终止进程。

## 另请参阅

### Unfair Locking

- [os_unfair_lock](os_unfair_lock.md) — 一种包含 unfair lock 数据的结构。
- [OS_UNFAIR_LOCK_INIT](os_unfair_lock_init.md) — 一个用于初始化新 unfair lock 的值。
- [os_unfair_lock_t](os_unfair_lock_t.md) — 一个指向 unfair lock 结构的指针。
- [os_unfair_lock_lock](os_unfair_lock_lock.md) — 一种低层级锁，允许等待线程在争用时阻塞。
- [os_unfair_lock_trylock](os_unfair_lock_trylock.md) — 锁定一个尚未被锁定的 unfair lock。
- [os_unfair_lock_lock_with_flags](os_unfair_lock_lock_with_flags.md)
- [os_unfair_lock_unlock](os_unfair_lock_unlock.md) — 解锁一个 unfair lock。
- [os_unfair_lock_assert_owner](os_unfair_lock_assert_owner.md) — 如果调用线程不拥有指定的 unfair lock，则触发断言。
- [os_unfair_lock_flags_t](os_unfair_lock_flags_t.md)
