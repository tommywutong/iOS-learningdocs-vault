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
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_sync_wait_on_address_flags_t

<sub>枚举</sub>

用于控制 futex 等待行为的标志。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef enum { ... } os_sync_wait_on_address_flags_t;
```

## 主题

### 枚举 case

- [OS_SYNC_WAIT_ON_ADDRESS_NONE](os_sync_wait_on_address_flags_t/os_sync_wait_on_address_none.md) — 会阻塞线程的 futex 函数的默认行为。
- [OS_SYNC_WAIT_ON_ADDRESS_SHARED](os_sync_wait_on_address_flags_t/os_sync_wait_on_address_shared.md) — 表明地址位于共享内存区域的标志，允许来自另一进程的 futex 唤醒。

## 另请参阅

### Futex 条件等待原语

- [os_sync_wait_on_address](os_sync_wait_on_address.md) — 一种原子比较并等待操作，用于实现更高层的同步原语。
- [os_sync_wait_on_address_with_deadline](os_sync_wait_on_address_with_deadline.md) — 一种带截止时间的原子比较并等待操作，用于实现更高层的同步原语。
- [os_sync_wait_on_address_with_timeout](os_sync_wait_on_address_with_timeout.md) — 一种带超时的原子比较并等待操作，用于实现更高层的同步原语。
- [os_sync_wake_by_address_all](os_sync_wake_by_address_all.md) — 一种唤醒所有阻塞在 futex 等待上的线程的原子操作，用于实现更高层的同步原语。
- [os_sync_wake_by_address_any](os_sync_wake_by_address_any.md) — 一种唤醒一个阻塞在 futex 等待上的线程的原子操作，用于实现更高层的同步原语。
- [os_sync_wake_by_address_flags_t](os_sync_wake_by_address_flags_t.md) — 用于控制 futex 唤醒行为的标志。
