---
title: inheritQoS
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchworkitemflags/inheritqos
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/inheritqos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchworkitemflags/inheritqos.json'
content_hash: 'sha256:33db29940200e5d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchWorkItemFlags](../dispatchworkitemflags.md)

# inheritQoS

<sub>Type Property</sub>

Prefer the quality-of-service class associated with the current execution context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let inheritQoS: DispatchWorkItemFlags
```

## Discussion

This flag prioritizes the quality-of-service class of the current execution context over the one associated with the block, as long as doing so does not lower the quality of service.

## See Also

### Work Item Flags

- [assignCurrentContext](assigncurrentcontext.md) — Set the attributes of the work item to match the attributes of the current execution context.
- [barrier](barrier.md) — Cause the work item to act as a barrier block when submitted to a concurrent queue.
- [detached](detached.md) — Disassociate the work item’s attributes from the current execution context.
- [enforceQoS](enforceqos.md) — Prefer the quality-of-service class associated with the block.
- [noQoS](noqos.md) — Execute the work item without assigning a quality-of-service class.
