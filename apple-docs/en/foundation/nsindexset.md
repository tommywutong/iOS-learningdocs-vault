---
title: NSIndexSet
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsindexset
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset.json'
content_hash: 'sha256:386b02326cd37976'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIndexSet

<sub>Class</sub>

An immutable collection of unique integer values that represent indexes in another collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSIndexSet
```

## Overview

In Swift, this type bridges to [IndexSet](indexset.md); use [NSIndexSet](nsindexset.md) when you need reference semantics or other Foundation-specific behavior.

The `NSIndexSet` class represents an immutable collection of unique unsigned integers, known as **indexes** because of the way they are used. This collection is referred to as an **index set**. Indexes must be in the range `0 .. NSNotFound - 1`.

You use index sets in your code to store indexes into some other data structure. For example, given an `NSArray` object, you could use an index set to identify a subset of objects in that array.

You should not use index sets to store an arbitrary collection of integer values because index sets store indexes as sorted ranges. This makes them more efficient than storing a collection of individual integers. It also means that each index value can only appear once in the index set.

The designated initializers of the `NSIndexSet` class are: [- initWithIndex:](<nsindexset/init(index_).md>), [- initWithIndexesInRange:](<nsindexset/init(indexesin_).md>), and [- initWithIndexSet:](<nsindexset/init(indexset_).md>).

You must not subclass the `NSIndexSet` class.

The mutable subclass of `NSIndexSet` is [NSMutableIndexSet](nsmutableindexset.md).

> [!important] Important
> The Swift overlay to the Foundation framework provides the [IndexSet](indexset.md) structure, which bridges to the [NSIndexSet](nsindexset.md) class and its mutable subclass, [NSMutableIndexSet](nsmutableindexset.md). For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSMutableIndexSet](nsmutableindexset.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sequence](../swift/sequence.md)

## Topics

### Creating Index Sets

- [- initWithIndex:](<nsindexset/init(index_).md>) — Initializes an allocated [NSIndexSet](nsindexset.md) object with an index.
- [- initWithIndexesInRange:](<nsindexset/init(indexesin_).md>) — Initializes an allocated [NSIndexSet](nsindexset.md) object with an index range.
- [- initWithIndexSet:](<nsindexset/init(indexset_).md>) — Initializes an allocated [NSIndexSet](nsindexset.md) object with an index set.

### Querying Index Sets

- [- containsIndex:](<nsindexset/contains(__)-bb19.md>) — Indicates whether the index set contains a specific index.
- [- containsIndexes:](<nsindexset/contains(__)-5j2kh.md>) — Indicates whether the receiving index set contains a superset of the indexes in another index set.
- [- containsIndexesInRange:](<nsindexset/contains(in_).md>) — Indicates whether the index set contains the indexes represented by an index range.
- [- intersectsIndexesInRange:](<nsindexset/intersects(in_).md>) — Indicates whether the index set contains any of the indexes in a range.
- [count](nsindexset/count.md) — The number of indexes in the index set.
- [- countOfIndexesInRange:](<nsindexset/countofindexes(in_).md>) — Returns the number of indexes in the index set that are members of a given range.
- [- indexPassingTest:](<nsindexset/index(passingtest_).md>) — Returns the index of the first object that passes the predicate Block test.
- [- indexesPassingTest:](<nsindexset/indexes(passingtest_).md>) — Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test.
- [- indexWithOptions:passingTest:](<nsindexset/index(options_passingtest_).md>) — Returns the index of the first object that passes the predicate Block test using the specified enumeration options.
- [- indexesWithOptions:passingTest:](<nsindexset/indexes(options_passingtest_).md>) — Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test using the specified enumeration options.
- [- indexInRange:options:passingTest:](<nsindexset/index(in_options_passingtest_).md>) — Returns the index of the first object in the specified range that passes the predicate Block test.
- [- indexesInRange:options:passingTest:](<nsindexset/indexes(in_options_passingtest_).md>) — Returns an `NSIndexSet` containing the receiving index set’s objects in the specified range that pass the Block test.

### Enumerating Index Set Content

- [- enumerateRangesInRange:options:usingBlock:](<nsindexset/enumerateranges(in_options_using_).md>) — Enumerates over the ranges in the range of objects using the block
- [- enumerateRangesUsingBlock:](<nsindexset/enumerateranges(__).md>) — Executes a given block using each object in the index set, in the specified ranges.
- [- enumerateRangesWithOptions:usingBlock:](<nsindexset/enumerateranges(options_using_).md>) — Executes a given block using each object in the index set, in the specified ranges.

### Comparing Index Sets

- [- isEqualToIndexSet:](<nsindexset/isequal(to_).md>) — Indicates whether the indexes in the receiving index set are the same indexes contained in another index set.

### Getting Indexes

- [firstIndex](nsindexset/firstindex.md) — The first index in the index set.
- [lastIndex](nsindexset/lastindex.md) — The last index in the index set.
- [- indexLessThanIndex:](<nsindexset/indexlessthanindex(__).md>) — Returns either the closest index in the index set that is less than a specific index or the not-found indicator.
- [- indexLessThanOrEqualToIndex:](<nsindexset/indexlessthanorequal(to_).md>) — Returns either the closest index in the index set that is less than or equal to a specific index or the not-found indicator.
- [- indexGreaterThanOrEqualToIndex:](<nsindexset/indexgreaterthanorequal(to_).md>) — Returns either the closest index in the index set that is greater than or equal to a specific index or the not-found indicator.
- [- indexGreaterThanIndex:](<nsindexset/indexgreaterthanindex(__).md>) — Returns either the closest index in the index set that is greater than a specific index or the not-found indicator.
- [- getIndexes:maxCount:inIndexRange:](<nsindexset/getindexes(__maxcount_inindexrange_).md>) — The index set fills an index buffer with the indexes contained both in the index set and in an index range, returning the number of indexes copied.

### Enumerating Indexes

- [- enumerateIndexesUsingBlock:](<nsindexset/enumerate(__).md>) — Executes a given Block using each object in the index set.
- [- enumerateIndexesWithOptions:usingBlock:](<nsindexset/enumerate(options_using_).md>) — Executes a given Block over the index set’s indexes, using the specified enumeration options.
- [- enumerateIndexesInRange:options:usingBlock:](<nsindexset/enumerate(in_options_using_).md>) — Executes a given Block using the indexes in the specified range, using the specified enumeration options.
- [makeIterator()](<nsindexset/makeiterator().md>) — Returns an _iterator_ over the elements of this _sequence_.
- [NSIndexSetIterator](nsindexsetiterator.md) — An iterator suitable for enumerating the elements of an index set.

### Initializers

- [init(coder:)](<nsindexset/init(coder_).md>)
- [init(indexesInRange:)](<nsindexset/init(indexesinrange_)-67dvw.md>)
- [init(indexesInRange:)](<nsindexset/init(indexesinrange_)-n2eh.md>)

### Default Implementations

- [Sequence Implementations](nsindexset/sequence-implementations.md)
