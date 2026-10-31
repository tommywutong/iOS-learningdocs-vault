---
title: os_unfair_lock_lock
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_unfair_lock_lock
source_url: 'https://developer.apple.com/documentation/os/os_unfair_lock_lock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_unfair_lock_lock.json'
content_hash: 'sha256:6ca68e2296512024'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_unfair_lock_lock

<sub>函数</sub>

一种低层级锁，允许等待线程在争用时高效地阻塞。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_unfair_lock_lock(os_unfair_lock_t lock);
```

## 参数

- `lock`——指向要锁定的 unfair lock 的指针。

## 讨论

请将锁的数据视为不透明且由实现定义。锁包含线程所有权信息，系统可能使用这些信息尝试解决优先级反转。

锁只能在锁定它的同一线程中解锁。尝试从不同线程解锁会导致运行时错误。

不得通过共享或多重映射的内存从多个进程或线程访问锁，因为锁的实现依赖于锁值的地址以及拥有该锁的进程。

> [!note] 注意
> 这是已废弃的 `OSSpinLock` 的替代。此函数在争用时不会自旋，而是在内核中等待，直到被解锁操作唤醒。与 `OSSpinLock` 一样，此函数不强制公平性或加锁顺序——例如，解锁者有可能立即重新获取锁，赶在被唤醒的等待线程有机会尝试获取锁之前。这可能有利于性能，但也使等待线程发生饥饿成为可能。

## 另请参阅

### Unfair Locking

- [os_unfair_lock](os_unfair_lock.md)——一种包含 unfair lock 数据的结构。
- [OS_UNFAIR_LOCK_INIT](os_unfair_lock_init.md)——一个用于初始化新 unfair lock 的值。
- [os_unfair_lock_t](os_unfair_lock_t.md)——一个指向 unfair lock 结构的指针。
- [os_unfair_lock_trylock](os_unfair_lock_trylock.md)——锁定一个尚未被锁定的 unfair lock。
- [os_unfair_lock_lock_with_flags](os_unfair_lock_lock_with_flags.md)
- [os_unfair_lock_unlock](os_unfair_lock_unlock.md)——解锁一个 unfair lock。
- [os_unfair_lock_assert_owner](os_unfair_lock_assert_owner.md)——如果调用线程不拥有指定的 unfair lock，则触发断言。
- [os_unfair_lock_assert_not_owner](os_unfair_lock_assert_not_owner.md)——如果调用线程拥有指定的 unfair lock，则触发断言。
- [os_unfair_lock_flags_t](os_unfair_lock_flags_t.md)
