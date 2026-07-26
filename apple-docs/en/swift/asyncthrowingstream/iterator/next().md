---
title: next()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingstream/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/iterator/next%28%29.json'
content_hash: 'sha256:f0a9fbc8f30a179f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncThrowingStream](../../asyncthrowingstream.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

The next value from the asynchronous stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async throws -> Element?
```

## Discussion

When `next()` returns `nil`, this signifies the end of the `AsyncThrowingStream`.

It is a programmer error to invoke `next()` from a concurrent context that contends with another such call, which results in a call to `fatalError()`.

If you cancel the task this iterator is running in while `next()` is awaiting a value, the `AsyncThrowingStream` terminates. In this case, `next()` may return `nil` immediately, or else return `nil` on subsequent calls.
