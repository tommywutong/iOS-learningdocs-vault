---
title: os_security_config_t
framework: os
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_security_config_t
source_url: 'https://developer.apple.com/documentation/os/os_security_config_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_security_config_t.json'
content_hash: 'sha256:ef867228f69ff82b'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_security_config_t

<sub>枚举</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef enum { ... } os_security_config_t;
```

## 概述

进程/任务可具有的受支持安全配置。这是一种位掩码（bitmask）类型，允许多种配置同时生效。

未设置任何安全配置标志。

表示已为该进程/任务启用 Hardened Heap 配置。这意味着系统内存分配器采用对安全性至关重要的设置。

表示已为该进程/任务启用 Trusted Path Read-Only（TPRO）。

表示已为该进程/任务启用内存标记扩展（Memory Tagging Extension，MTE）。

表示已为该进程/任务启用脚本限制（Script Restrictions）。

表示已为该进程/任务启用 Guard Objects 配置。

## 主题

### 枚举 case

- [OS_SECURITY_CONFIG_GUARD_OBJECTS](os_security_config_t/os_security_config_guard_objects.md)
- [OS_SECURITY_CONFIG_HARDENED_HEAP](os_security_config_t/os_security_config_hardened_heap.md)
- [OS_SECURITY_CONFIG_MTE](os_security_config_t/os_security_config_mte.md)
- [OS_SECURITY_CONFIG_NONE](os_security_config_t/os_security_config_none.md)
- [OS_SECURITY_CONFIG_SCRIPT_RESTRICTIONS](os_security_config_t/os_security_config_script_restrictions.md)
- [OS_SECURITY_CONFIG_TPRO](os_security_config_t/os_security_config_tpro.md)
