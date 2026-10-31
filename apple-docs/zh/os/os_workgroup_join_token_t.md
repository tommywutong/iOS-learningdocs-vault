---
title: os_workgroup_join_token_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_join_token_t
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_join_token_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_join_token_t.json'
content_hash: 'sha256:358661c0eb96f3f8'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_join_token_t

<sub>类型别名</sub>

表示线程与工作组之间连接的不透明令牌。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef struct os_workgroup_join_token_opaque_s * os_workgroup_join_token_t;
```

## 讨论

调用 `os_workgroup_join_self` 函数时，你需要提供一个未初始化的令牌结构；该函数会初始化此结构并填充相关信息。随后在调用 `os_workgroup_leave_self` 以将线程从工作组中移除时，请使用该令牌结构。

> [!important] 重要
> 从工作组中移除线程时，必须提供原始的线程、工作组以及令牌。如果这些值不匹配，系统会中止你的进程。

## 另请参阅

### 线程附着

- [os_workgroup_join](os_workgroup_join.md) — 将当前线程加入指定的工作组。
- [os_workgroup_leave](os_workgroup_leave.md) — 将当前线程从它先前加入的工作组中移除。
