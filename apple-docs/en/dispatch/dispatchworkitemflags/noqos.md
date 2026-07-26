---
title: noQoS
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchworkitemflags/noqos
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/noqos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchworkitemflags/noqos.json'
content_hash: 'sha256:3ae21ac1e45988ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchWorkItemFlags](../dispatchworkitemflags.md)

# noQoS

<sub>Type Property</sub>

Execute the work item without assigning a quality-of-service class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let noQoS: DispatchWorkItemFlags
```

## Discussion

This flag takes priority over the [assignCurrentContext](assigncurrentcontext.md) flag.

## See Also

### Work Item Flags

- [assignCurrentContext](assigncurrentcontext.md) — Set the attributes of the work item to match the attributes of the current execution context.
- [barrier](barrier.md) — Cause the work item to act as a barrier block when submitted to a concurrent queue.
- [detached](detached.md) — Disassociate the work item’s attributes from the current execution context.
- [enforceQoS](enforceqos.md) — Prefer the quality-of-service class associated with the block.
- [inheritQoS](inheritqos.md) — Prefer the quality-of-service class associated with the current execution context.
