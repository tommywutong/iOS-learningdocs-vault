---
title: DispatchWorkItemFlags
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchworkitemflags
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchworkitemflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchworkitemflags.json'
content_hash: 'sha256:4901186f94e67227'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchWorkItemFlags

<sub>Structure</sub>

A set of behaviors for a work item, such as its quality-of-service class and whether to create a barrier or spawn a new detached thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DispatchWorkItemFlags
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Work Item Flags

- [assignCurrentContext](dispatchworkitemflags/assigncurrentcontext.md) — Set the attributes of the work item to match the attributes of the current execution context.
- [barrier](dispatchworkitemflags/barrier.md) — Cause the work item to act as a barrier block when submitted to a concurrent queue.
- [detached](dispatchworkitemflags/detached.md) — Disassociate the work item’s attributes from the current execution context.
- [enforceQoS](dispatchworkitemflags/enforceqos.md) — Prefer the quality-of-service class associated with the block.
- [inheritQoS](dispatchworkitemflags/inheritqos.md) — Prefer the quality-of-service class associated with the current execution context.
- [noQoS](dispatchworkitemflags/noqos.md) — Execute the work item without assigning a quality-of-service class.

## See Also

### Creating a Work Item

- [init(qos:flags:block:)](<dispatchworkitem/init(qos_flags_block_).md>) — Creates a new dispatch work item from an existing block and assigns it the specified quality-of-service class.
