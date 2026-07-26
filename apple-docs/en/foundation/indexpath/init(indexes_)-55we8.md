---
title: 'init(indexes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexpath/init(indexes:)-55we8'
source_url: 'https://developer.apple.com/documentation/foundation/indexpath/init(indexes:)-55we8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexpath/init%28indexes%3A%29-55we8.json'
content_hash: 'sha256:c521a20fec3a4c05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexPath](../indexpath.md)

# init(indexes:)

<sub>Initializer</sub>

Creates an index path from a sequence of integers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<ElementSequence>(indexes: ElementSequence) where ElementSequence : Sequence, ElementSequence.Element == Int
```

## See Also

### Creating Index Paths

- [init()](<init().md>) — Creates an empty index path.
- [init(index:)](<init(index_).md>) — Creates an index path with a single element.
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — Creates an index path from an array literal.
- [init(indexes:)](<init(indexes_)-7auqk.md>) — Creates an index path from an array of elements.
- [Element](element.md) — A type that represents one node of an index path.
