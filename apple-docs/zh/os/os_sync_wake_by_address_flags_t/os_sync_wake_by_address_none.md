---
title: OS_SYNC_WAKE_BY_ADDRESS_NONE
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_sync_wake_by_address_flags_t/os_sync_wake_by_address_none
source_url: 'https://developer.apple.com/documentation/os/os_sync_wake_by_address_flags_t/os_sync_wake_by_address_none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_sync_wake_by_address_flags_t/os_sync_wake_by_address_none.json'
content_hash: 'sha256:7b215a9f1150912a'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [os_sync_wake_by_address_flags_t](../os_sync_wake_by_address_flags_t.md)

# OS_SYNC_WAKE_BY_ADDRESS_NONE

<sub>枚举 case</sub>

会唤醒线程的 futex 函数的默认行为。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_SYNC_WAKE_BY_ADDRESS_NONE
```

## 讨论

当你传入的地址仅在调用进程的内存空间中被访问时，使用此标志。此标志可启用无法用于共享内存的内核优化。
