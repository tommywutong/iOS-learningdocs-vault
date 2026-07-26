---
title: AsyncIterator
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncsequence/asynciterator
source_url: 'https://developer.apple.com/documentation/swift/asyncsequence/asynciterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncsequence/asynciterator.json'
content_hash: 'sha256:f692b3c3f9e1a8dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncSequence](../asyncsequence.md)

# AsyncIterator

<sub>Associated Type</sub>

The type of asynchronous iterator that produces elements of this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype AsyncIterator : AsyncIteratorProtocol
```

## See Also

### Creating an Iterator

- [makeAsyncIterator()](<makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [AsyncIteratorProtocol](../asynciteratorprotocol.md) — A type that asynchronously supplies the values of a sequence one at a time.
- [Element](element.md) — The type of element produced by this asynchronous sequence.
