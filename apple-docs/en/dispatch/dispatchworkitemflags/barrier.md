---
title: barrier
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchworkitemflags/barrier
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/barrier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchworkitemflags/barrier.json'
content_hash: 'sha256:04cff8aa94c58e0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchWorkItemFlags](../dispatchworkitemflags.md)

# barrier

<sub>Type Property</sub>

Cause the work item to act as a barrier block when submitted to a concurrent queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let barrier: DispatchWorkItemFlags
```

## Discussion

When submitted to a concurrent queue, a work item with this flag acts as a barrier. Work items submitted prior to the barrier execute to completion, at which point the barrier work item executes. Once the barrier work item finishes, the queue returns to scheduling work items that were submitted after the barrier.

## See Also

### Work Item Flags

- [assignCurrentContext](assigncurrentcontext.md) — Set the attributes of the work item to match the attributes of the current execution context.
- [detached](detached.md) — Disassociate the work item’s attributes from the current execution context.
- [enforceQoS](enforceqos.md) — Prefer the quality-of-service class associated with the block.
- [inheritQoS](inheritqos.md) — Prefer the quality-of-service class associated with the current execution context.
- [noQoS](noqos.md) — Execute the work item without assigning a quality-of-service class.
