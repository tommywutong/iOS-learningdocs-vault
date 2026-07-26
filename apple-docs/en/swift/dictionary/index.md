---
title: Dictionary.Index
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/index
source_url: 'https://developer.apple.com/documentation/swift/dictionary/index'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/index.json'
content_hash: 'sha256:c9ecf114e59f56fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# Dictionary.Index

<sub>Structure</sub>

The position of a key-value pair in a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Index
```

## Overview

Dictionary has two subscripting interfaces:

1. Subscripting with a key, yielding an optional value:

  ```swift
  v = d[k]!
  ```
2. Subscripting with an index, yielding a key-value pair:

  ```swift
  (k, v) = d[i]
  ```

## Relationships

- **Conforms To**: [Comparable](../comparable.md), [Equatable](../equatable.md), [Hashable](../hashable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Default Implementations

- [Comparable Implementations](index/comparable-implementations.md)
- [Equatable Implementations](index/equatable-implementations.md)
- [Hashable Implementations](index/hashable-implementations.md)

## See Also

### Supporting Types

- [Keys](keys-swift.struct.md) — A view of a dictionary’s keys.
- [Values](values-swift.struct.md) — A view of a dictionary’s values.
- [Indices](indices.md) — A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Iterator](iterator.md) — An iterator over the members of a `Dictionary<Key, Value>`.
