---
title: OS_SECURITY_CONFIG_HARDENED_HEAP
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_security_config_t/os_security_config_hardened_heap
source_url: 'https://developer.apple.com/documentation/os/os_security_config_t/os_security_config_hardened_heap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_security_config_t/os_security_config_hardened_heap.json'
content_hash: 'sha256:27e283f0b34eb37e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [os_security_config_t](../os_security_config_t.md)

# OS_SECURITY_CONFIG_HARDENED_HEAP

<sub>Enumeration Case</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_SECURITY_CONFIG_HARDENED_HEAP
```

## Discussion

Supported security configurations that a process/task can have. This is a bitmask type, allowing multiple configurations to be active.

No security config flags set.

Indicates that the Hardened Heap configuration is enabled for the process/task. This implies security-critical settings for the system memory allocator.

Indicates that Trusted Path Read-Only (TPRO) is enabled for the process/task.

Indicates that Memory Tagging Extension (MTE) is enabled for the process/task.

Indicates Script Restrictions are enabled for the process/task.

Indicates that the Guard Objects configuration is enabled for the process/task.
