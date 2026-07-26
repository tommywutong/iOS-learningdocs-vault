---
title: OS_dispatch_workloop
framework: Dispatch
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/os_dispatch_workloop
source_url: 'https://developer.apple.com/documentation/dispatch/os_dispatch_workloop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/os_dispatch_workloop.json'
content_hash: 'sha256:8d3e816c03e06b6a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# OS_dispatch_workloop

<sub>Protocol</sub>

A dispatch queue that prioritizes the execution of tasks based on their quality-of-service level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@protocol OS_dispatch_workloop <OS_dispatch_queue>
```

## Relationships

- **Inherits From**: [OS_dispatch_queue](os_dispatch_queue.md)

## See Also

### Creating a Dispatch Workloop

- [dispatch_workloop_create](dispatch_workloop_create.md) — Creates a new workloop with the specified label.
- [dispatch_workloop_create_inactive](dispatch_workloop_create_inactive.md) — Creates a new inactive workloop with the specified label.
- [dispatch_workloop_t](dispatch_workloop_t.md) — A dispatch queue that prioritizes the execution of tasks based on their quality-of-service level.
