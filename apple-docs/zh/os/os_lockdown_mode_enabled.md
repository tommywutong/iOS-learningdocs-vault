---
title: os_lockdown_mode_enabled
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/os/os_lockdown_mode_enabled
source_url: 'https://developer.apple.com/documentation/os/os_lockdown_mode_enabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_lockdown_mode_enabled.json'
content_hash: 'sha256:4d807ea7dd0f6930'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_lockdown_mode_enabled

<sub>函数</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern bool os_lockdown_mode_enabled();
```

## 返回值

若已启用锁定模式（Lockdown Mode），则为 true；若锁定模式已禁用或平台不支持，则为 false。

## 讨论

返回一个缓存值，指示系统当前是否已启用锁定模式。

如果在查询锁定模式状态时发生意外错误，此函数将终止进程。
