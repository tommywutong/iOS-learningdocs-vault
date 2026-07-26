---
title: os_security_config_get_for_proc
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_security_config_get_for_proc
source_url: 'https://developer.apple.com/documentation/os/os_security_config_get_for_proc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_security_config_get_for_proc.json'
content_hash: 'sha256:8abf8c0688566df7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_security_config_get_for_proc

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_security_config_get_for_proc(pid_t pid, os_security_config_t *config);
```

## Parameters

- `pid` — The process identifier (pid_t) of the target process.

- `config` — A pointer to an os_security_config_t variable where the resulting security configuration will be stored if the function succeeds. This parameter must not be NULL.

## Return Value

Returns 0 on success, in which case `*config` is populated, or -1 on failure.

## Discussion

Retrieves the security configuration bitmask for a target process, identified by its PID.

This function queries the kernel for the set of security properties active for the specified process.
