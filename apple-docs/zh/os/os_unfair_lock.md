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
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_unfair_lock

<sub>类型别名</sub>

一种包含 unfair lock 数据的结构。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef struct os_unfair_lock_s os_unfair_lock;
```

## 讨论

要创建一个锁，请分配一个此类型的变量，并将其初始化为 [OS_UNFAIR_LOCK_INIT](os_unfair_lock_init.md)。

## 另请参阅

### Unfair Locking

- [OS_UNFAIR_LOCK_INIT](os_unfair_lock_init.md)——一个用于初始化新 unfair lock 的值。
- [os_unfair_lock_t](os_unfair_lock_t.md)——一个指向 unfair lock 结构的指针。
- [os_unfair_lock_lock](os_unfair_lock_lock.md)——一种低层级锁，允许等待线程在争用时阻塞。
- [os_unfair_lock_trylock](os_unfair_lock_trylock.md)——锁定一个尚未被锁定的 unfair lock。
- [os_unfair_lock_lock_with_flags](os_unfair_lock_lock_with_flags.md)
- [os_unfair_lock_unlock](os_unfair_lock_unlock.md)——解锁一个 unfair lock。
- [os_unfair_lock_assert_owner](os_unfair_lock_assert_owner.md)——如果调用线程不拥有指定的 unfair lock，则触发断言。
- [os_unfair_lock_assert_not_owner](os_unfair_lock_assert_not_owner.md)——如果调用线程拥有指定的 unfair lock，则触发断言。
- [os_unfair_lock_flags_t](os_unfair_lock_flags_t.md)
