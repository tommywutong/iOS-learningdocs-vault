---
title: isCancelled
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/throwingdiscardingtaskgroup/iscancelled
source_url: 'https://developer.apple.com/documentation/swift/throwingdiscardingtaskgroup/iscancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingdiscardingtaskgroup/iscancelled.json'
content_hash: 'sha256:e5aca0d0f8f99f6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingDiscardingTaskGroup](../throwingdiscardingtaskgroup.md)

# isCancelled

<sub>Instance Property</sub>

A Boolean value that indicates whether the group was canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isCancelled: Bool { get }
```

## Discussion

To cancel a group, call the `ThrowingDiscardingTaskGroup.cancelAll()` method.

If the task that’s currently running this group is canceled, the group is also implicitly canceled, which is also reflected in this property’s value.

### Interaction with task cancellation shields

Cancellation may be suppressed by an active task cancellation shield (`withTaskCancellationShield(operation:)`), which may cause `isCancelled` to return `false` even though the task has been cancelled externally.

> [!info] See Also
> `withTaskCancellationShield(operation:)`
