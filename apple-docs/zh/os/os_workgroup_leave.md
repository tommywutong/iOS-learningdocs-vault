---
title: os_workgroup_leave
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_leave
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_leave'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_leave.json'
content_hash: 'sha256:d8b67010e0290c01'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_leave

<sub>函数</sub>

将当前线程从它先前加入的工作组中移除。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_workgroup_leave(os_workgroup_t wg, os_workgroup_join_token_t token);
```

## 参数

- `wg` — 要离开的工作组。此工作组必须是该线程先前加入的同一个工作组。若不是，此函数会中止进程。

- `token` — 线程加入工作组时收到的令牌。若令牌中的数据无效、令牌属于其他线程，或 `wg` 参数中的工作组与令牌中的信息不匹配，此函数会中止进程。

## 讨论

调用此函数时，务必使用加入时所用的同一 [os_workgroup_t](os_workgroup_t.md) 和 [os_workgroup_join_token_t](os_workgroup_join_token_t.md) 结构。若工作组或令牌信息不匹配，此函数会中止当前进程。你可以从 app 的实时线程安全地调用此函数。

> [!important] 重要
> 务必在线程退出之前将其从工作组中移除。若线程在终止时仍已加入某个工作组，系统会中止当前进程。

## 另请参阅

### 线程附着

- [os_workgroup_join](os_workgroup_join.md) — 将当前线程加入指定的工作组。
- [os_workgroup_join_token_t](os_workgroup_join_token_t.md) — 表示线程与工作组之间连接的不透明令牌。
