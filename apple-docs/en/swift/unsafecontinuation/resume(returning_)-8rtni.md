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
doc_path: '/documentation/swift/unsafecontinuation/resume(returning:)-8rtni'
source_url: 'https://developer.apple.com/documentation/swift/unsafecontinuation/resume(returning:)-8rtni'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafecontinuation/resume%28returning%3A%29-8rtni.json'
content_hash: 'sha256:e59e5c55afc001ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeContinuation](../unsafecontinuation.md)

# resume(returning:)

<sub>Instance Method</sub>

Resume the task that’s awaiting the continuation by returning the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resume(returning value: sending T)
```

## Parameters

- `value` — The value to return from the continuation.

## Discussion

A continuation must be resumed exactly once. If the continuation has already resumed, then calling this method results in undefined behavior.

After calling this method, control immediately returns to the caller. The task continues executing when its executor schedules it.
