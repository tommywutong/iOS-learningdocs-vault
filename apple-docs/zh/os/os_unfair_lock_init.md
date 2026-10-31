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
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OS_UNFAIR_LOCK_INIT

<sub>宏</sub>

一个用于初始化新 unfair lock 的值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define OS_UNFAIR_LOCK_INIT
```

## 另请参阅

### Unfair Locking

- [os_unfair_lock](os_unfair_lock.md)——一种包含 unfair lock 数据的结构。
- [os_unfair_lock_t](os_unfair_lock_t.md)——一个指向 unfair lock 结构的指针。
- [os_unfair_lock_lock](os_unfair_lock_lock.md)——一种低层级锁，允许等待线程在争用时阻塞。
- [os_unfair_lock_trylock](os_unfair_lock_trylock.md)——锁定一个尚未被锁定的 unfair lock。
- [os_unfair_lock_lock_with_flags](os_unfair_lock_lock_with_flags.md)
- [os_unfair_lock_unlock](os_unfair_lock_unlock.md)——解锁一个 unfair lock。
- [os_unfair_lock_assert_owner](os_unfair_lock_assert_owner.md)——如果调用线程不拥有指定的 unfair lock，则触发断言。
- [os_unfair_lock_assert_not_owner](os_unfair_lock_assert_not_owner.md)——如果调用线程拥有指定的 unfair lock，则触发断言。
- [os_unfair_lock_flags_t](os_unfair_lock_flags_t.md)
