---
title: URL.AsyncBytes.AsyncIterator
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/asyncbytes/asynciterator
source_url: 'https://developer.apple.com/documentation/foundation/url/asyncbytes/asynciterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/asyncbytes/asynciterator.json'
content_hash: 'sha256:9d8d84a05fe0a002'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [AsyncBytes](../asyncbytes.md)

# URL.AsyncBytes.AsyncIterator

<sub>Structure</sub>

The iterator type that produces elements of this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AsyncIterator
```

## Relationships

- **Conforms To**: [AsyncIteratorProtocol](../../../swift/asynciteratorprotocol.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Producing iterator values

- [next()](<asynciterator/next().md>) — Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

### Supporting types

- [Element](element.md) — The type of element produced by this asynchronous sequence.

## See Also

### Creating an iterator

- [makeAsyncIterator()](<makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
