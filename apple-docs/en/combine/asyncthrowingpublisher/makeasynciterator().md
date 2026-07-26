---
title: makeAsyncIterator()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/asyncthrowingpublisher/makeasynciterator()
source_url: 'https://developer.apple.com/documentation/combine/asyncthrowingpublisher/makeasynciterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/asyncthrowingpublisher/makeasynciterator%28%29.json'
content_hash: 'sha256:cdf6ed6d1ace7aef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [AsyncThrowingPublisher](../asyncthrowingpublisher.md)

# makeAsyncIterator()

<sub>Instance Method</sub>

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeAsyncIterator() -> AsyncThrowingPublisher<P>.Iterator
```

## Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.

## See Also

### Creating an iterator

- [Iterator](iterator.md) — The iterator that produces elements of the asynchronous publisher sequence.
