---
title: RandomAccessCollection Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/utf16view/randomaccesscollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/utf16view/randomaccesscollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/utf16view/randomaccesscollection-implementations.json'
content_hash: 'sha256:89f59bff3f524468'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Swift Standard Library](../../../swift-standard-library.md) · [Strings and Text](../../../strings-and-text.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [UTF16View](../utf16view.md)

# RandomAccessCollection Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [endIndex](endindex.md) — The “past the end” position—that is, the position one greater than the last valid subscript argument.
- [indices](indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.
- [startIndex](startindex.md) — The position of the first code unit.

### Instance Methods

- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [index(before:)](<index(before_).md>) — Returns the position immediately after the given index.

### Subscripts

- [subscript(_:)](<subscript(__).md>) — Accesses the code unit at the specified position.
