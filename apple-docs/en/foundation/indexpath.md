---
title: IndexPath
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/indexpath
source_url: 'https://developer.apple.com/documentation/foundation/indexpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexpath.json'
content_hash: 'sha256:404748449a8425e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# IndexPath

<sub>Structure</sub>

A list of indexes that together represent the path to a specific location in a tree of nested arrays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct IndexPath
```

## Overview

Each index in an index path represents the index into an array of children from one node in the tree to another, deeper, node.

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [Comparable](../swift/comparable.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Hashable](../swift/hashable.md), [MutableCollection](../swift/mutablecollection.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Creating Index Paths

- [init()](<indexpath/init().md>) — Creates an empty index path.
- [init(index:)](<indexpath/init(index_).md>) — Creates an index path with a single element.
- [init(arrayLiteral:)](<indexpath/init(arrayliteral_).md>) — Creates an index path from an array literal.
- [init(indexes:)](<indexpath/init(indexes_)-7auqk.md>) — Creates an index path from an array of elements.
- [init(indexes:)](<indexpath/init(indexes_)-55we8.md>) — Creates an index path from a sequence of integers.
- [Element](indexpath/element.md) — A type that represents one node of an index path.

### Working with Special Node Names

- [endIndex](indexpath/endindex.md) — One past the index of the last node in the index path.
- [item](indexpath/item-8cp0y.md) — The value of the item element of the index path.
- [row](indexpath/row.md) — The value of the row element of the index path.
- [section](indexpath/section-8h7wo.md) — The value of the section element of the index path.
- [startIndex](indexpath/startindex.md) — The index of the first node in the index path.

### Accessing Nodes

- [subscript(_:)](<indexpath/subscript(__)-6p6ul.md>) — Accesses one of the index path’s nodes.
- [subscript(_:)](<indexpath/subscript(__)-4pgu1.md>) — Accesses a contiguous subrange of the index path’s nodes.

### Adding Nodes

- [+(_:_:)](<indexpath/+(____).md>) — Combines the elements of two index paths into a single index path.
- [+=(_:_:)](<indexpath/+=(____).md>) — Appends the elements of another index path to this index path.

### Selecting Nodes

- [append(_:)](<indexpath/append(__)-6dxrh.md>) — Appends the nodes of another index path to this one.
- [append(_:)](<indexpath/append(__)-6vsd5.md>) — Appends an array of elements to this index path as additional nodes.
- [append(_:)](<indexpath/append(__)-7qv6f.md>) — Appends a single element to this index path as a new node.
- [appending(_:)](<indexpath/appending(__)-93eco.md>) — Returns a new index path containing the elements of this one plus the given element.
- [appending(_:)](<indexpath/appending(__)-53tcl.md>) — Returns a new index path containing the elements of this one plus those of another index path.
- [appending(_:)](<indexpath/appending(__)-174v0.md>) — Returns a new index path containing the elements of this one plus an array of additional elements.
- [compare(_:)](<indexpath/compare(__).md>) — Compares this index path to another in depth-first traversal order.
- [dropLast()](<indexpath/droplast().md>) — Return a new index path containing all but the last element.
- [index(after:)](<indexpath/index(after_).md>) — Returns the index that follows the given index.
- [index(before:)](<indexpath/index(before_).md>) — Returns the index that precedes the given index.
- [makeIterator()](<indexpath/makeiterator().md>) — Returns an iterator over the nodes of the index path.

### Excluding Nodes

- [dropLast()](<indexpath/droplast().md>) — Return a new index path containing all but the last element.

### Iterating over Nodes

- [makeIterator()](<indexpath/makeiterator().md>) — Returns an iterator over the nodes of the index path.

### Comparing Index Paths

- [compare(_:)](<indexpath/compare(__).md>) — Compares this index path to another in depth-first traversal order.

### Manipulating Indexes

- [Index](indexpath/index.md) — A type that points to a particular node in an index path, similar to an array index.
- [startIndex](indexpath/startindex.md) — The index of the first node in the index path.
- [endIndex](indexpath/endindex.md) — One past the index of the last node in the index path.
- [index(after:)](<indexpath/index(after_).md>) — Returns the index that follows the given index.
- [index(before:)](<indexpath/index(before_).md>) — Returns the index that precedes the given index.
- [Indices](indexpath/indices.md) — A type that represents a group of nodes in an index path.

### Using Reference Types

- [NSIndexPath](nsindexpath.md) — A list of indexes that together represent the path to a specific location in a tree of nested arrays.

### Initializers

- [init(item:section:)](<indexpath/init(item_section_)-359jo.md>) — Creates an index path that references an item in a particular section.
- [init(item:section:)](<indexpath/init(item_section_)-rib.md>) — Initialize for use with `NSCollectionView`.
- [init(row:section:)](<indexpath/init(row_section_).md>) — Creates an index path that references a row in a particular section.

### Instance Properties

- [item](indexpath/item-6rh8l.md) — The item of this index path, when used with `NSCollectionView`.
- [section](indexpath/section-2059m.md) — The section of this index path, when used with `NSCollectionView`.

## See Also

### Indexes

- [IndexSet](indexset.md) — A collection of unique integer values that represent the indexes of elements in another collection.
