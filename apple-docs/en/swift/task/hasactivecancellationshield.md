---
title: hasActiveCancellationShield
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/task/hasactivecancellationshield
source_url: 'https://developer.apple.com/documentation/swift/task/hasactivecancellationshield'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/hasactivecancellationshield.json'
content_hash: 'sha256:0600ff843b58017a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# hasActiveCancellationShield

<sub>Type Property</sub>

Checks if the current task is executing in a scope with a task cancellation shield activated by the `withTaskCancellationShield(operation:)` function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var hasActiveCancellationShield: Bool { get }
```

## Discussion

An active task cancellation shield prevents a task’s ability to observe if it was cancelled, i.e. the `Task/isCancelled` property will always return `false` when the task is executing with an active shield.

This property is primarily aimed at  debugging and understanding cancellation behavior in complex call hierarchies, and should not be used in regular control flow.

Returns `true` when executing within a task that has an active cancellation shield.

Cancellation shields are not automatically inherited by child tasks; each child task must install its own shield if needed if it, independently, wanted to ignore cancellation during a specific scope.

> [!info] See Also
> `withTaskCancellationShield(operation:)`

> [!info] See Also
> [hasActiveCancellationShield](../unsafecurrenttask/hasactivecancellationshield.md)
