---
title: IndexPath.Indices
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/indexpath/indices
source_url: 'https://developer.apple.com/documentation/foundation/indexpath/indices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexpath/indices.json'
content_hash: 'sha256:1da3ca2aa8693b41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexPath](../indexpath.md)

# IndexPath.Indices

<sub>Type Alias</sub>

A type that represents a group of nodes in an index path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Indices = DefaultIndices<IndexPath>
```

## See Also

### Manipulating Indexes

- [Index](index.md) — A type that points to a particular node in an index path, similar to an array index.
- [startIndex](startindex.md) — The index of the first node in the index path.
- [endIndex](endindex.md) — One past the index of the last node in the index path.
- [index(after:)](<index(after_).md>) — Returns the index that follows the given index.
- [index(before:)](<index(before_).md>) — Returns the index that precedes the given index.
