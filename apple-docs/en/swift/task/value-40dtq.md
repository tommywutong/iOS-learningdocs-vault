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
doc_path: /documentation/swift/task/value-40dtq
source_url: 'https://developer.apple.com/documentation/swift/task/value-40dtq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/value-40dtq.json'
content_hash: 'sha256:6409c6611137941f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# value

<sub>Instance Property</sub>

The result from a nonthrowing task, after it completes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var value: Success { get async }
```

## Discussion

If the task hasn’t completed yet, accessing this property waits for it to complete and its priority increases to that of the current task. Note that this might not be as effective as creating the task with the correct priority, depending on the executor’s scheduling details.

Tasks that never throw an error can still check for cancellation, but they need to use an approach like returning `nil` instead of throwing an error.

## See Also

### Accessing Results

- [value](value-60t02.md) — The result from a throwing task, after it completes.
- [result](result.md) — The result or error from a throwing task, after it completes.
