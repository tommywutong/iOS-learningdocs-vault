---
title: DispatchQueue.SchedulerTimeType
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue/schedulertimetype
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/schedulertimetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/schedulertimetype.json'
content_hash: 'sha256:9aa8e56420b32e2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# DispatchQueue.SchedulerTimeType

<sub>Structure</sub>

The scheduler time type used by the dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SchedulerTimeType
```

## Relationships

- **Conforms To**: [Comparable](../../swift/comparable.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [Strideable](../../swift/strideable.md)

## Topics

### Creating Scheduler Times

- [init(_:)](<schedulertimetype/init(__).md>) — Creates a dispatch queue time type instance.

### Working with Scheduler Time Intervals

- [advanced(by:)](<schedulertimetype/advanced(by_).md>)
- [distance(to:)](<schedulertimetype/distance(to_).md>)

### Inspecting Scheduler Time Properties

- [dispatchTime](schedulertimetype/dispatchtime.md) — The dispatch time represented by this type.

## See Also

### Scheduling Combine Publishers

- [SchedulerOptions](scheduleroptions.md) — A set of options that affect the operation of the dispatch queue scheduler.
