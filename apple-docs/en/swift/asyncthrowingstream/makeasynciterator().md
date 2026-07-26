---
title: makeAsyncIterator()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingstream/makeasynciterator()
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/makeasynciterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/makeasynciterator%28%29.json'
content_hash: 'sha256:5f7a5f8d5c9c7ee5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingStream](../asyncthrowingstream.md)

# makeAsyncIterator()

<sub>Instance Method</sub>

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeAsyncIterator() -> AsyncThrowingStream<Element, Failure>.Iterator
```

## See Also

### Creating an Iterator

- [Iterator](iterator.md) — The asynchronous iterator for iterating an asynchronous stream.
