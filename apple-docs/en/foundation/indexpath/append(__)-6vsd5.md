---
title: 'append(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexpath/append(_:)-6vsd5'
source_url: 'https://developer.apple.com/documentation/foundation/indexpath/append(_:)-6vsd5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexpath/append%28_%3A%29-6vsd5.json'
content_hash: 'sha256:fba9f34d17c71f42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexPath](../indexpath.md)

# append(_:)

<sub>Instance Method</sub>

Appends an array of elements to this index path as additional nodes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(_ other: Array<IndexPath.Element>)
```

## See Also

### Selecting Nodes

- [append(_:)](<append(__)-6dxrh.md>) — Appends the nodes of another index path to this one.
- [append(_:)](<append(__)-7qv6f.md>) — Appends a single element to this index path as a new node.
- [appending(_:)](<appending(__)-93eco.md>) — Returns a new index path containing the elements of this one plus the given element.
- [appending(_:)](<appending(__)-53tcl.md>) — Returns a new index path containing the elements of this one plus those of another index path.
- [appending(_:)](<appending(__)-174v0.md>) — Returns a new index path containing the elements of this one plus an array of additional elements.
- [compare(_:)](<compare(__).md>) — Compares this index path to another in depth-first traversal order.
- [dropLast()](<droplast().md>) — Return a new index path containing all but the last element.
- [index(after:)](<index(after_).md>) — Returns the index that follows the given index.
- [index(before:)](<index(before_).md>) — Returns the index that precedes the given index.
- [makeIterator()](<makeiterator().md>) — Returns an iterator over the nodes of the index path.
