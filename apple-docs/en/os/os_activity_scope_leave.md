---
title: os_activity_scope_leave
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_scope_leave
source_url: 'https://developer.apple.com/documentation/os/os_activity_scope_leave'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_scope_leave.json'
content_hash: 'sha256:ac96daa1b82b0a19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_activity_scope_leave

<sub>Function</sub>

Restores the current activity to a previously saved state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_activity_scope_leave(os_activity_scope_state_t state);
```

## Parameters

- `state` — A pointer to a scope state struct that holds the execution state you want to restore.

## See Also

### Saving and Restoring Activity States

- [os_activity_scope_enter](os_activity_scope_enter.md) — Switches the current activity, saving the existing execution context.
- [os_activity_scope_state_t](os_activity_scope_state_t.md) — An opaque structure that contains a saved activity-execution context.
