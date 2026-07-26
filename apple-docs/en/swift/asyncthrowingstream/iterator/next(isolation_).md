---
title: 'next(isolation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingstream/iterator/next(isolation:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/iterator/next(isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/iterator/next%28isolation%3A%29.json'
content_hash: 'sha256:a5dfe5402b00740d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncThrowingStream](../../asyncthrowingstream.md) · [Iterator](../iterator.md)

# next(isolation:)

<sub>Instance Method</sub>

The next value from the asynchronous stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(Failure) -> Element?
```

## Discussion

When `next()` returns `nil`, this signifies the end of the `AsyncThrowingStream`.

It is a programmer error to invoke `next()` from a concurrent context that contends with another such call, which results in a call to `fatalError()`.

If you cancel the task this iterator is running in while `next()` is awaiting a value, the `AsyncThrowingStream` terminates. In this case, `next()` may return `nil` immediately, or else return `nil` on subsequent calls.
