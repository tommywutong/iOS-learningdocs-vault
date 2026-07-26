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
doc_path: /documentation/swift/unsafecurrenttask/iscancelled
source_url: 'https://developer.apple.com/documentation/swift/unsafecurrenttask/iscancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafecurrenttask/iscancelled.json'
content_hash: 'sha256:b05525ac9a8b7974'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeCurrentTask](../unsafecurrenttask.md)

# isCancelled

<sub>Instance Property</sub>

A Boolean value that indicates whether the current task was canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isCancelled: Bool { get }
```

## Discussion

After the value of this property becomes `true`, it remains `true` indefinitely. There is no way to uncancel a task.

This property returns the actual cancellation state of the task, regardless of whether a cancellation shield is active. Use `Task/isCancelled` (the static property) if you need cancellation checking that respects active shields.

### Instance property isCancelled ignores Task Cancellation Shields

The instance property `task.isCancelled` is not contextual and therefore does not respect cancellation shields. If a task was cancelled and is executing with an active cancellation shield, this property will return the _actual_ cancellation status of the specific task.

It is possible to determine if a shield is active and then actively determine that the cancelled status should be temporarily ignored by using this pair of APIs:

```swift
withUnsafeCurrentTask { unsafeTask in
  if unsafeTask.hasActiveCancellationShield {
    false
  } else {
    unsafeTask.isCancelled
  }
}
```

Which is equivalent to the contextually aware static `Task.isCancelled` property:

```swift
// Contextually aware, and equivalent to the snippet using UnsafeCurrentTask:
Task.isCancelled
```

Prefer using `Task.isCancelled` (the static property) in most situations when checking the cancellation status from inside the task.

> [!info] See Also
> `Task/isCancelled`

> [!info] See Also
> [checkCancellation()](<../task/checkcancellation().md>)

> [!info] See Also
> [hasActiveCancellationShield](../task/hasactivecancellationshield.md)

> [!info] See Also
> `withTaskCancellationShield(operation:)`
