---
title: 'finish(throwing:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingstream/continuation/finish(throwing:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/finish(throwing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/continuation/finish%28throwing%3A%29.json'
content_hash: 'sha256:cfdd5de0caa09d69'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncThrowingStream](../../asyncthrowingstream.md) · [Continuation](../continuation.md)

# finish(throwing:)

<sub>Instance Method</sub>

Resume the task awaiting the next iteration point by having it return nil, which signifies the end of the iteration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finish(throwing error: Failure? = nil)
```

## Parameters

- `error` — The error to throw, or `nil`, to finish normally.

## Discussion

Calling this function more than once has no effect. After calling finish, the stream enters a terminal state and doesn’t produce any additional elements.
