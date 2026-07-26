---
title: nw_path_monitor_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_path_monitor_t
source_url: 'https://developer.apple.com/documentation/network/nw_path_monitor_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_path_monitor_t.json'
content_hash: 'sha256:f3c1e0b6d5a5dd3d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_path_monitor_t

<sub>Type Alias</sub>

An observer that you use to monitor and react to network changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_path_monitor_t = any OS_nw_path_monitor
```

## Topics

### Creating Path Monitors

- [nw_path_monitor_create](<nw_path_monitor_create().md>) — Initializes a path monitor to observe all available interface types.
- [nw_path_monitor_create_with_type](<nw_path_monitor_create_with_type(__).md>) — Initializes a path monitor to observe a specific interface type.
- [nw_path_monitor_prohibit_interface_type](<nw_path_monitor_prohibit_interface_type(____).md>) — Prohibit a path monitor from using a specific interface type.
- [nw_path_monitor_set_queue](<nw_path_monitor_set_queue(____).md>) — Sets a queue on which to deliver path events.
- [nw_path_monitor_start](<nw_path_monitor_start(__).md>) — Starts monitoring path changes.

### Handling Path Updates

- [nw_path_monitor_set_update_handler](<nw_path_monitor_set_update_handler(____).md>) — Sets a handler to receive network path updates.
- [nw_path_monitor_update_handler_t](nw_path_monitor_update_handler_t.md) — A handler that delivers network path updates.

### Canceling Path Monitors

- [nw_path_monitor_cancel](<nw_path_monitor_cancel(__).md>) — Stops receiving network path updates.
- [nw_path_monitor_set_cancel_handler](<nw_path_monitor_set_cancel_handler(____).md>) — Sets a handler to determine when a monitor is fully cancelled and will no longer deliver events.
- [nw_path_monitor_cancel_handler_t](nw_path_monitor_cancel_handler_t.md) — A handler that indicates when a monitor has been cancelled.
