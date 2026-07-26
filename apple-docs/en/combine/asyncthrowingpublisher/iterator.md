---
title: AsyncThrowingPublisher.Iterator
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/asyncthrowingpublisher/iterator
source_url: 'https://developer.apple.com/documentation/combine/asyncthrowingpublisher/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/asyncthrowingpublisher/iterator.json'
content_hash: 'sha256:d399600de198b1ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [AsyncThrowingPublisher](../asyncthrowingpublisher.md)

# AsyncThrowingPublisher.Iterator

<sub>Structure</sub>

The iterator that produces elements of the asynchronous publisher sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Iterator
```

## Relationships

- **Conforms To**: [AsyncIteratorProtocol](../../swift/asynciteratorprotocol.md)

## Topics

### Iterating over elements

- [next()](<iterator/next().md>) — Produces the next element in the prefix sequence.

## See Also

### Creating an iterator

- [makeAsyncIterator()](<makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
