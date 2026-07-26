---
title: cancel()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafecurrenttask/cancel()
source_url: 'https://developer.apple.com/documentation/swift/unsafecurrenttask/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafecurrenttask/cancel%28%29.json'
content_hash: 'sha256:6386dbc0509d704e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeCurrentTask](../unsafecurrenttask.md)

# cancel()

<sub>Instance Method</sub>

Cancel the current task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

The task will be immediately cancelled and cancellation will propagate towards any child tasks it has.

### Interaction with Task Cancellation Shields

Note that cancellation may not be observed if a task is currently executing with an active task cancellation shield. Refer to cancellation shield documentation for detailed semantics.

> [!info] See Also
> `withTaskCancellationShield(operation:)`

> [!info] See Also
> `Task/hasActiveTaskCancellationShield`
