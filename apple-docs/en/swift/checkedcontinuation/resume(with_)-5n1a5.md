---
title: 'resume(with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/checkedcontinuation/resume(with:)-5n1a5'
source_url: 'https://developer.apple.com/documentation/swift/checkedcontinuation/resume(with:)-5n1a5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/checkedcontinuation/resume%28with%3A%29-5n1a5.json'
content_hash: 'sha256:ead9cf87b8fdfbb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CheckedContinuation](../checkedcontinuation.md)

# resume(with:)

<sub>Instance Method</sub>

Resume the task awaiting the continuation by having it either return normally or throw an error based on the state of the given `Result` value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resume<Er>(with result: sending Result<T, Er>) where E == any Error, Er : Error
```

## Parameters

- `result` — A value to either return or throw from the continuation.

## Discussion

A continuation must be resumed exactly once. If the continuation has already been resumed through this object, then the attempt to resume the continuation will trap.

After `resume` enqueues the task, control immediately returns to the caller. The task continues executing when its executor is able to reschedule it.
