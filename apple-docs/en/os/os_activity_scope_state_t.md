---
title: os_activity_scope_state_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_scope_state_t
source_url: 'https://developer.apple.com/documentation/os/os_activity_scope_state_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_scope_state_t.json'
content_hash: 'sha256:cc57ca9818dc9245'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_activity_scope_state_t

<sub>Type Alias</sub>

An opaque structure that contains a saved activity-execution context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef struct os_activity_scope_state_s * os_activity_scope_state_t;
```

## Topics

### Instance Properties

- [opaque](os_activity_scope_state_s/opaque.md) — Opaque data that the system uses to store the execution state.

## See Also

### Saving and Restoring Activity States

- [os_activity_scope_enter](os_activity_scope_enter.md) — Switches the current activity, saving the existing execution context.
- [os_activity_scope_leave](os_activity_scope_leave.md) — Restores the current activity to a previously saved state.
