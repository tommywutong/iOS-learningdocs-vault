---
title: OS_SECURITY_CONFIG_NONE
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_security_config_t/os_security_config_none
source_url: 'https://developer.apple.com/documentation/os/os_security_config_t/os_security_config_none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_security_config_t/os_security_config_none.json'
content_hash: 'sha256:f1c2490a16a4ddb8'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [os_security_config_t](../os_security_config_t.md)

# OS_SECURITY_CONFIG_NONE

<sub>枚举 case</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_SECURITY_CONFIG_NONE
```

## 讨论

进程/任务可具有的受支持安全配置。这是一种位掩码（bitmask）类型，允许多种配置同时生效。

未设置任何安全配置标志。

表示已为该进程/任务启用 Hardened Heap 配置。这意味着系统内存分配器采用对安全性至关重要的设置。

表示已为该进程/任务启用 Trusted Path Read-Only（TPRO）。

表示已为该进程/任务启用内存标记扩展（Memory Tagging Extension，MTE）。

表示已为该进程/任务启用脚本限制（Script Restrictions）。

表示已为该进程/任务启用 Guard Objects 配置。
