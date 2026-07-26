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
doc_path: /documentation/swift/asyncstream/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/iterator/next%28%29.json'
content_hash: 'sha256:21eb4310893fdcd0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncStream](../../asyncstream.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

The next value from the asynchronous stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async -> Element?
```

## Discussion

When `next()` returns `nil`, this signifies the end of the `AsyncStream`.

It is a programmer error to invoke `next()` from a concurrent context that contends with another such call, which results in a call to `fatalError()`.

If you cancel the task this iterator is running in while `next()` is awaiting a value, the `AsyncStream` terminates. In this case, `next()` might return `nil` immediately, or return `nil` on subsequent calls.
