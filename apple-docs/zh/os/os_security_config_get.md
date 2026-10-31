---
title: os_security_config_get
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_security_config_get
source_url: 'https://developer.apple.com/documentation/os/os_security_config_get'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_security_config_get.json'
content_hash: 'sha256:002b1aceec3be156'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_security_config_get

<sub>函数</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern os_security_config_t os_security_config_get();
```

## 返回值

一个表示当前有效安全标志的 os_security_config_t 值。对于当前进程，此函数预计不会失败。

## 讨论

检索当前进程的安全配置位掩码。

此函数检查内核传递给当前进程的值。
