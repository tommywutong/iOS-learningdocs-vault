---
title: OS_SYNC_WAKE_BY_ADDRESS_SHARED
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_sync_wake_by_address_flags_t/os_sync_wake_by_address_shared
source_url: 'https://developer.apple.com/documentation/os/os_sync_wake_by_address_flags_t/os_sync_wake_by_address_shared'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_sync_wake_by_address_flags_t/os_sync_wake_by_address_shared.json'
content_hash: 'sha256:47676082f99d9ba3'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [os_sync_wake_by_address_flags_t](../os_sync_wake_by_address_flags_t.md)

# OS_SYNC_WAKE_BY_ADDRESS_SHARED

<sub>枚举 case</sub>

表明地址位于共享内存区域的标志，允许你唤醒另一个正在等待的进程。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_SYNC_WAKE_BY_ADDRESS_SHARED
```

## 讨论

当你向任何 futex 唤醒函数传入在共享内存中分配的地址时，使用此标志。共享内存可用于单个进程内的等待与唤醒，但会带来性能损失。

> [!important] 重要
> 在唤醒曾以 [OS_SYNC_WAIT_ON_ADDRESS_SHARED](../os_sync_wait_on_address_flags_t/os_sync_wait_on_address_shared.md) 标志等待的线程时，请使用此标志。
