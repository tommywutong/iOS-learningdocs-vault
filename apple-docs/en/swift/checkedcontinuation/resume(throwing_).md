---
title: 'resume(throwing:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/checkedcontinuation/resume(throwing:)'
source_url: 'https://developer.apple.com/documentation/swift/checkedcontinuation/resume(throwing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/checkedcontinuation/resume%28throwing%3A%29.json'
content_hash: 'sha256:82e104952ee39c31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CheckedContinuation](../checkedcontinuation.md)

# resume(throwing:)

<sub>Instance Method</sub>

Resume the task awaiting the continuation by having it throw an error from its suspension point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resume(throwing error: E)
```

## Parameters

- `error` — The error to throw from the continuation.

## Discussion

A continuation must be resumed exactly once. If the continuation has already been resumed through this object, then the attempt to resume the continuation will trap.

After `resume` enqueues the task, control immediately returns to the caller. The task continues executing when its executor is able to reschedule it.
