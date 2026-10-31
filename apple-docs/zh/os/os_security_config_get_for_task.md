---
title: os_security_config_get_for_task
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_security_config_get_for_task
source_url: 'https://developer.apple.com/documentation/os/os_security_config_get_for_task'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_security_config_get_for_task.json'
content_hash: 'sha256:4bc45d74654ce67b'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_security_config_get_for_task

<sub>函数</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_security_config_get_for_task(task_t task, os_security_config_t *config);
```

## 参数

- `task` — 目标任务的 Mach 任务端口（task_t）。

- `config` — 指向 os_security_config_t 变量的指针；若函数成功，结果安全配置将存储于此。此参数不得为 NULL。

## 返回值

成功时返回 0，此时会填充 `*config`；失败时返回 -1。

## 讨论

检索目标 Mach 任务的安全配置位掩码。

此函数向内核查询指定 Mach 任务当前生效的安全属性集合。
