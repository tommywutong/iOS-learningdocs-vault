---
title: result
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/task/result
source_url: 'https://developer.apple.com/documentation/swift/task/result'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/result.json'
content_hash: 'sha256:039c75d9d1b717a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# result

<sub>Instance Property</sub>

The result or error from a throwing task, after it completes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var result: Result<Success, Failure> { get async }
```

## Return Value

If the task succeeded, `.success` with the task’s result as the associated value; otherwise, `.failure` with the error as the associated value.

## Discussion

If the task hasn’t completed, accessing this property waits for it to complete and its priority increases to that of the current task. Note that this might not be as effective as creating the task with the correct priority, depending on the executor’s scheduling details.

## See Also

### Accessing Results

- [value](value-60t02.md) — The result from a throwing task, after it completes.
- [value](value-40dtq.md) — The result from a nonthrowing task, after it completes.
