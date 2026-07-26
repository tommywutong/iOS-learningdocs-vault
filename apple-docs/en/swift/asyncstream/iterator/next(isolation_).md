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
doc_path: '/documentation/swift/asyncstream/iterator/next(isolation:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/iterator/next(isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/iterator/next%28isolation%3A%29.json'
content_hash: 'sha256:f478a068dcdb1c24'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncStream](../../asyncstream.md) · [Iterator](../iterator.md)

# next(isolation:)

<sub>Instance Method</sub>

The next value from the asynchronous stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async -> Element?
```

## Discussion

When `next()` returns `nil`, this signifies the end of the `AsyncStream`.

It is a programmer error to invoke `next()` from a concurrent context that contends with another such call, which results in a call to `fatalError()`.

If you cancel the task this iterator is running in while `next()` is awaiting a value, the `AsyncStream` terminates. In this case, `next()` might return `nil` immediately, or return `nil` on subsequent calls.
