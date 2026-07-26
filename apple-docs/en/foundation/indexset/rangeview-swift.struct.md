---
title: IndexSet.RangeView
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/indexset/rangeview-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/indexset/rangeview-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/rangeview-swift.struct.json'
content_hash: 'sha256:87d1319c8a76ecbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# IndexSet.RangeView

<sub>Structure</sub>

A view of the contents of an IndexSet, organized by range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RangeView
```

## Overview

For example, if an IndexSet is composed of: `[1..<5]` and `[7..<10]` and `[13]` then calling `next()` on this view’s iterator will produce 3 ranges before returning nil.

## Relationships

- **Conforms To**: [BidirectionalCollection](../../swift/bidirectionalcollection.md), [Collection](../../swift/collection.md), [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [Sequence](../../swift/sequence.md)

## Topics

### Counting Indexes

- [count](count.md) — Returns the number of integers in `self`.
- [endIndex](rangeview-swift.struct/endindex.md) — The ending index in the range.
- [first](first.md) — The first integer in `self`, or nil if `self` is empty.
- [isEmpty](isempty.md) — Returns `true` if self contains no values.
- [last](last.md) — The last integer in `self`, or nil if `self` is empty.
- [startIndex](rangeview-swift.struct/startindex.md) — The beginning index in the range.

### Accessing Indexes

- [subscript(_:)](<rangeview-swift.struct/subscript(__)-5r66q.md>) — Accesses the items at the given range of indexes.
- [subscript(_:)](<rangeview-swift.struct/subscript(__)-8gh0x.md>) — Accesses the item at the given index.

### Finding Indexes

- [startIndex](rangeview-swift.struct/startindex.md) — The beginning index in the range.
- [endIndex](rangeview-swift.struct/endindex.md) — The ending index in the range.
- [index(after:)](<rangeview-swift.struct/index(after_).md>) — Returns the index in the range after the specified one.
- [index(before:)](<rangeview-swift.struct/index(before_).md>) — Returns the index in the range before the specified one.

### Iterating over Indexes

- [makeIterator()](<rangeview-swift.struct/makeiterator().md>) — Returns an iterator over the indexes of this range view.

### Testing for Inclusion in the Range

- [contains(_:)](<contains(__).md>) — Returns `true` if `self` contains `integer`.
- [index(after:)](<rangeview-swift.struct/index(after_).md>) — Returns the index in the range after the specified one.
- [index(before:)](<rangeview-swift.struct/index(before_).md>) — Returns the index in the range before the specified one.
- [makeIterator()](<rangeview-swift.struct/makeiterator().md>) — Returns an iterator over the indexes of this range view.

### Type Aliases

- [Index](rangeview-swift.struct/index.md) — An alias for the type of an index.

## See Also

### Getting a Range-Based View

- [rangeView(of:)](<rangeview(of_)-5xqe8.md>) — Returns a `Range`-based view of `self`.
- [rangeView](rangeview-swift.property.md) — Returns a `Range`-based view of the entire contents of `self`.
