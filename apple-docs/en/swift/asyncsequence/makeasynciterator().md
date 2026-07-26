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
doc_path: /documentation/swift/asyncsequence/makeasynciterator()
source_url: 'https://developer.apple.com/documentation/swift/asyncsequence/makeasynciterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncsequence/makeasynciterator%28%29.json'
content_hash: 'sha256:a78c61f2154ef385'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncSequence](../asyncsequence.md)

# makeAsyncIterator()

<sub>Instance Method</sub>

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeAsyncIterator() -> Self.AsyncIterator
```

## Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.

## See Also

### Creating an Iterator

- [AsyncIterator](asynciterator.md) — The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [AsyncIteratorProtocol](../asynciteratorprotocol.md) — A type that asynchronously supplies the values of a sequence one at a time.
- [Element](element.md) — The type of element produced by this asynchronous sequence.
