---
title: assignCurrentContext
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchworkitemflags/assigncurrentcontext
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/assigncurrentcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchworkitemflags/assigncurrentcontext.json'
content_hash: 'sha256:c441eaf2308e8f92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchWorkItemFlags](../dispatchworkitemflags.md)

# assignCurrentContext

<sub>Type Property</sub>

Set the attributes of the work item to match the attributes of the current execution context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let assignCurrentContext: DispatchWorkItemFlags
```

## Discussion

When this flag is set, the work item inherits attributes such as the quality-of-service class from the dispatch queue or thread responsible for executing the task.

## See Also

### Work Item Flags

- [barrier](barrier.md) — Cause the work item to act as a barrier block when submitted to a concurrent queue.
- [detached](detached.md) — Disassociate the work item’s attributes from the current execution context.
- [enforceQoS](enforceqos.md) — Prefer the quality-of-service class associated with the block.
- [inheritQoS](inheritqos.md) — Prefer the quality-of-service class associated with the current execution context.
- [noQoS](noqos.md) — Execute the work item without assigning a quality-of-service class.
