---
title: cancelAll()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/throwingdiscardingtaskgroup/cancelall()
source_url: 'https://developer.apple.com/documentation/swift/throwingdiscardingtaskgroup/cancelall()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingdiscardingtaskgroup/cancelall%28%29.json'
content_hash: 'sha256:cf3c3be949c832c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingDiscardingTaskGroup](../throwingdiscardingtaskgroup.md)

# cancelAll()

<sub>Instance Method</sub>

Cancel all of the remaining tasks in the group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancelAll()
```

## Discussion

If you add a task to a group after canceling the group, that task is canceled immediately after being added to the group.

Immediately canceled child tasks should therefore cooperatively check for and react  to cancellation, e.g. by throwing an `CancellationError` at their earliest convenience, or otherwise handling the cancellation.

There are no restrictions on where you can call this method. Code inside a child task or even another task can cancel a group, however one should be very careful to not keep a reference to the group longer than the `with...TaskGroup(...) { ... }` method body is executing.

> [!info] See Also
> `Task.isCancelled`

> [!info] See Also
> `ThrowingDiscardingTaskGroup.isCancelled`
