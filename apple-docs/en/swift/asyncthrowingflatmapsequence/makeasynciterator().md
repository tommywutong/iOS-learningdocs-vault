---
title: makeAsyncIterator()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingflatmapsequence/makeasynciterator()
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingflatmapsequence/makeasynciterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingflatmapsequence/makeasynciterator%28%29.json'
content_hash: 'sha256:9f3f0a96b3b6e1c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingFlatMapSequence](../asyncthrowingflatmapsequence.md)

# makeAsyncIterator()

<sub>Instance Method</sub>

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeAsyncIterator() -> AsyncThrowingFlatMapSequence<Base, SegmentOfResult>.Iterator
```

## Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.
