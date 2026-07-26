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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_security_config_get_for_task

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_security_config_get_for_task(task_t task, os_security_config_t *config);
```

## Parameters

- `task` — The Mach task port (task_t) of the target task.

- `config` — A pointer to an os_security_config_t variable where the resulting security configuration will be stored if the function succeeds. This parameter must not be NULL.

## Return Value

Returns 0 on success, in which case `*config` is populated, or -1 on failure.

## Discussion

Retrieves the security configuration bitmask for a target Mach task.

This function queries the kernel for the set of security properties active for the specified Mach task.
