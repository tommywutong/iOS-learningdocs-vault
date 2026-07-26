---
title: value
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/task/value-60t02
source_url: 'https://developer.apple.com/documentation/swift/task/value-60t02'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/value-60t02.json'
content_hash: 'sha256:e61e22cd9d06abba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# value

<sub>Instance Property</sub>

The result from a throwing task, after it completes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var value: Success { get async throws }
```

## Return Value

The task’s result.

## Discussion

If the task hasn’t completed, accessing this property waits for it to complete and its priority increases to that of the current task. Note that this might not be as effective as creating the task with the correct priority, depending on the executor’s scheduling details.

If the task throws an error, this property propagates that error. Tasks that respond to cancellation by throwing `CancellationError` have that error propagated here upon cancellation.

## See Also

### Accessing Results

- [value](value-40dtq.md) — The result from a nonthrowing task, after it completes.
- [result](result.md) — The result or error from a throwing task, after it completes.
