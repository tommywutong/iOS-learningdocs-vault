---
title: 'resume(returning:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/checkedcontinuation/resume(returning:)'
source_url: 'https://developer.apple.com/documentation/swift/checkedcontinuation/resume(returning:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/checkedcontinuation/resume%28returning%3A%29.json'
content_hash: 'sha256:32a46c6662b30a17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CheckedContinuation](../checkedcontinuation.md)

# resume(returning:)

<sub>Instance Method</sub>

Resume the task awaiting the continuation by having it return normally from its suspension point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resume(returning value: sending T)
```

## Parameters

- `value` — The value to return from the continuation.

## Discussion

A continuation must be resumed exactly once. If the continuation has already been resumed through this object, then the attempt to resume the continuation will trap.

After `resume` enqueues the task, control immediately returns to the caller. The task continues executing when its executor is able to reschedule it.
