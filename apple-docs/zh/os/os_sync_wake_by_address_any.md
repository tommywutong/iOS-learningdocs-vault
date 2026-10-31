---
title: os_sync_wake_by_address_any
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_sync_wake_by_address_any
source_url: 'https://developer.apple.com/documentation/os/os_sync_wake_by_address_any'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_sync_wake_by_address_any.json'
content_hash: 'sha256:50475f222b0d1d46'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_sync_wake_by_address_any

<sub>函数</sub>

一种唤醒一个阻塞在 futex 等待上的线程的原子操作，用于实现更高层的同步原语。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_sync_wake_by_address_any(void *addr, size_t size, os_sync_wake_by_address_flags_t flags);
```

## 参数

- `addr` — 用于唤醒所等待地址的用户空间地址。此地址必须按 `size` 对齐。

- `size` — 等待值的大小，以字节为单位。取值可为 4 或 8 字节；其中 4 字节值使用 `value` 的低位字节。

- `flags` — 操作的标志。

## 返回值

成功时返回 0，出错时返回 -1，并设置 `errno`。

## 讨论

此函数唤醒一个等待在 `addr` 上的线程。在存在多个等待者时，不保证唤醒哪一个线程。

在 wait 与 wake API 之间为 `addr`、`size` 和 `flags` 传递一致的值。详情见 [os_sync_wake_by_address_flags_t](os_sync_wake_by_address_flags_t.md)。

> [!important] 重要
> 仅将此函数用于实现没有所有权语义的同步原语，例如条件变量或信号量。特别是，此函数不提供优先级反转规避。对于加锁 API，请使用既有的 OS 原语，例如 `pthread` 线程或 [Unfair Locking](synchronization.md#Unfair-Locking) API。对于由 OS 管理的同步与线程处理，请使用更高层的 API，例如 [Dispatch](../dispatch.md)。

### 错误码

当此函数返回 `-1` 时，全局 `errno` 会包含下列值之一，表示对应错误：

| 错误码 | 说明 |
|---|---|
| `EINVAL` | 无效的标志或大小。![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)传入的 `addr` 为 NULL。![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)与此 `addr` 处既有内核状态关联的操作，与其他函数参数不一致。 |
| `ENOENT` | `addr` 上没有比较并等待操作。 |
| `EDOM` | `addr` 正用于非比较并等待的同步。 |

## 另请参阅

### Futex 条件等待原语

- [os_sync_wait_on_address](os_sync_wait_on_address.md) — 一种原子比较并等待操作，用于实现更高层的同步原语。
- [os_sync_wait_on_address_with_deadline](os_sync_wait_on_address_with_deadline.md) — 一种带截止时间的原子比较并等待操作，用于实现更高层的同步原语。
- [os_sync_wait_on_address_with_timeout](os_sync_wait_on_address_with_timeout.md) — 一种带超时的原子比较并等待操作，用于实现更高层的同步原语。
- [os_sync_wait_on_address_flags_t](os_sync_wait_on_address_flags_t.md) — 用于控制 futex 等待行为的标志。
- [os_sync_wake_by_address_all](os_sync_wake_by_address_all.md) — 一种唤醒所有阻塞在 futex 等待上的线程的原子操作，用于实现更高层的同步原语。
- [os_sync_wake_by_address_flags_t](os_sync_wake_by_address_flags_t.md) — 用于控制 futex 唤醒行为的标志。
