---
title: detached
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchworkitemflags/detached
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/detached'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchworkitemflags/detached.json'
content_hash: 'sha256:3adebb38519d7a16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchWorkItemFlags](../dispatchworkitemflags.md)

# detached

<sub>Type Property</sub>

Disassociate the work item’s attributes from the current execution context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let detached: DispatchWorkItemFlags
```

## Discussion

When this flag is set, the system does not apply attributes from the current execution context to the work item.

## See Also

### Work Item Flags

- [assignCurrentContext](assigncurrentcontext.md) — Set the attributes of the work item to match the attributes of the current execution context.
- [barrier](barrier.md) — Cause the work item to act as a barrier block when submitted to a concurrent queue.
- [enforceQoS](enforceqos.md) — Prefer the quality-of-service class associated with the block.
- [inheritQoS](inheritqos.md) — Prefer the quality-of-service class associated with the current execution context.
- [noQoS](noqos.md) — Execute the work item without assigning a quality-of-service class.
