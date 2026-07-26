---
title: isCancelled
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/taskgroup/iscancelled
source_url: 'https://developer.apple.com/documentation/swift/taskgroup/iscancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskgroup/iscancelled.json'
content_hash: 'sha256:e992a157bd110da6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskGroup](../taskgroup.md)

# isCancelled

<sub>Instance Property</sub>

A Boolean value that indicates whether the group was canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isCancelled: Bool { get }
```

## Discussion

To cancel a group, call the `TaskGroup.cancelAll()` method.

If the task that’s currently running this group is canceled, the group is also implicitly canceled, which is also reflected in this property’s value.

### Interaction with task cancellation shields

Cancellation may be suppressed by an active task cancellation shield (`withTaskCancellationShield(operation:)`), which may cause `isCancelled` to return `false` even though the task has been cancelled externally.

> [!info] See Also
> `withTaskCancellationShield(operation:)`

## See Also

### Canceling Tasks

- [cancelAll()](<cancelall().md>) — Cancel all of the remaining tasks in the group.
