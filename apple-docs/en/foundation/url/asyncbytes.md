---
title: URL.AsyncBytes
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/asyncbytes
source_url: 'https://developer.apple.com/documentation/foundation/url/asyncbytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/asyncbytes.json'
content_hash: 'sha256:bdca24c5e6a5b89b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# URL.AsyncBytes

<sub>Structure</sub>

An asynchronous sequence of bytes loaded from the URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AsyncBytes
```

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating an iterator

- [makeAsyncIterator()](<asyncbytes/makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [AsyncIterator](asyncbytes/asynciterator.md) — The iterator type that produces elements of this asynchronous sequence.

### Adapting Textual Sequences

- [lines](lines.md) — The URL’s resource data, as an asynchronous sequence of lines of text.

### Supporting Types

- [Element](asyncbytes/element.md) — The type of element produced by this asynchronous sequence.

## See Also

### Loading URL contents asynchronously

- [resourceBytes](resourcebytes.md) — The URL’s resource data, as an asynchronous sequence of bytes.
- [lines](lines.md) — The URL’s resource data, as an asynchronous sequence of lines of text.
