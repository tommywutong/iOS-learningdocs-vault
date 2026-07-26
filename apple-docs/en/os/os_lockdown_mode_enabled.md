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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_lockdown_mode_enabled

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern bool os_lockdown_mode_enabled();
```

## Return Value

True if Lockdown Mode is enabled; false if Lockdown Mode is disabled or not supported on the platform.

## Discussion

Returns a cached value indicating whether Lockdown Mode is currently enabled on the system.

This function will abort the process if an unexpected error occurs while querying the Lockdown Mode state.
