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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_security_config_get

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern os_security_config_t os_security_config_get();
```

## Return Value

An os_security_config_t value representing the active security flags. This function is not expected to fail for the current process.

## Discussion

Retrieves the security configuration bitmask for the current process.

This function inspects the value passed by the kernel to the current process.
