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
doc_path: '/documentation/swift/unsafecontinuation/resume(with:)-7t959'
source_url: 'https://developer.apple.com/documentation/swift/unsafecontinuation/resume(with:)-7t959'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafecontinuation/resume%28with%3A%29-7t959.json'
content_hash: 'sha256:7b58ae94dc7a631e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeContinuation](../unsafecontinuation.md)

# resume(with:)

<sub>Instance Method</sub>

Resume the task that’s awaiting the continuation by returning or throwing the given result value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resume<Er>(with result: sending Result<T, Er>) where E == any Error, Er : Error
```

## Parameters

- `result` — The result. If it contains a `.success` value, the continuation returns that value; otherwise, it throws the `.error` value.

## Discussion

A continuation must be resumed exactly once. If the continuation has already resumed, then calling this method results in undefined behavior.

After calling this method, control immediately returns to the caller. The task continues executing when its executor schedules it.
