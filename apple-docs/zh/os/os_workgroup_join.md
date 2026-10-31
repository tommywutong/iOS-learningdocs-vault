---
title: os_workgroup_join
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_join
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_join'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_join.json'
content_hash: 'sha256:316c79b43e03ffd1'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_join

<sub>函数</sub>

将当前线程加入指定的工作组。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_workgroup_join(os_workgroup_t wg, os_workgroup_join_token_t token_out);
```

## 参数

- `wg` — 要加入的工作组。

- `token_out` — 一个空的令牌结构。此函数会用与工作组关系相关的信息填充所提供的结构。请保存此结构，以便稍后将线程从工作组中移除。

## 返回值

成功时返回 `0`，失败时返回表示失败原因的非零错误码。常见错误码包括 `EINVAL` 或 `EALREADY`。例如，若线程已属于某个工作组，此方法返回 `EALREADY`；若工作组已被取消，则返回 `EINVAL`。

## 讨论

调用此函数时，当前线程不得属于任何工作组。此函数会将线程加入指定工作组，并更新 `token_out` 参数。你可以从 app 的实时线程安全地调用此函数。

> [!important] 重要
> 请保存 `token_out` 参数，以便稍后将线程从工作组中移除。移除线程时，线程、工作组以及令牌数据必须与你为此函数指定的原始值匹配；若不匹配，系统会中止你的进程。

## 另请参阅

### 线程附着

- [os_workgroup_leave](os_workgroup_leave.md) — 将当前线程从它先前加入的工作组中移除。
- [os_workgroup_join_token_t](os_workgroup_join_token_t.md) — 表示线程与工作组之间连接的不透明令牌。
