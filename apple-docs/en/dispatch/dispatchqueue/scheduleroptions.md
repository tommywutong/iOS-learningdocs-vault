---
title: DispatchQueue.SchedulerOptions
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue/scheduleroptions
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/scheduleroptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/scheduleroptions.json'
content_hash: 'sha256:54e7e29cf40bc951'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# DispatchQueue.SchedulerOptions

<sub>Structure</sub>

A set of options that affect the operation of the dispatch queue scheduler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SchedulerOptions
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating Dispatch Queue Scheduler Options

- [init(qos:flags:group:)](<scheduleroptions/init(qos_flags_group_).md>) — Creates a dispatch queue scheduler options instance with the given options.

### Inspecting Scheduler Options

- [qos](scheduleroptions/qos.md) — The dispatch queue quality of service.
- [flags](scheduleroptions/flags.md) — The dispatch queue work item flags.
- [group](scheduleroptions/group.md) — The dispatch group, if any, to use when performing actions.

## See Also

### Scheduling Combine Publishers

- [SchedulerTimeType](schedulertimetype.md) — The scheduler time type used by the dispatch queue.
