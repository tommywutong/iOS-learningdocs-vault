---
title: IndexSet
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/indexset
source_url: 'https://developer.apple.com/documentation/foundation/indexset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset.json'
content_hash: 'sha256:a143dc2d4106e91c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# IndexSet

<sub>Structure</sub>

A collection of unique integer values that represent the indexes of elements in another collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct IndexSet
```

## Overview

The range of valid integer values is `0...Int.max-1`. Anything outside this range is an error.

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Hashable](../swift/hashable.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Creating an Index Set

- [init()](<indexset/init().md>) — Initializes an empty index set.
- [init(integer:)](<indexset/init(integer_).md>) — Initializes an index set with a single integer.
- [init(integersIn:)](<indexset/init(integersin_)-40cz3.md>) — Initializes an index set with a range of integers.

### Counting Items in a Set

- [count(in:)](<indexset/count(in_)-v622.md>) — Returns the count of integers in `self` that intersect `range`.

### Accessing Elements

- [subscript(_:)](<indexset/subscript(__).md>) — Accesses one element in the index set.

### Combining Index Sets

- [formIntersection(_:)](<indexset/formintersection(__).md>) — Intersects the `IndexSet` with `other`.
- [formSymmetricDifference(_:)](<indexset/formsymmetricdifference(__).md>) — Exclusive or the `IndexSet` with `other`.
- [formUnion(_:)](<indexset/formunion(__).md>) — Union the `IndexSet` with `other`.
- [intersection(_:)](<indexset/intersection(__).md>) — Intersects the `IndexSet` with `other`.
- [symmetricDifference(_:)](<indexset/symmetricdifference(__).md>) — Exclusive or the `IndexSet` with `other`.
- [union(_:)](<indexset/union(__).md>) — Union the `IndexSet` with `other`.

### Inserting Elements

- [insert(_:)](<indexset/insert(__).md>) — Insert an integer into the `IndexSet`.
- [insert(integersIn:)](<indexset/insert(integersin_)-28eld.md>) — Insert a range of integers into the `IndexSet`.
- [update(with:)](<indexset/update(with_).md>) — Insert an integer into the `IndexSet`.

### Removing Elements

- [remove(_:)](<indexset/remove(__).md>) — Remove an integer from the `IndexSet`.
- [remove(integersIn:)](<indexset/remove(integersin_)-7dhfw.md>) — Remove a range of integers from the `IndexSet`.
- [remove(integersIn:)](<indexset/remove(integersin_)-54370.md>) — Remove a range of integers from the `IndexSet`.
- [removeAll()](<indexset/removeall().md>) — Remove all values from the `IndexSet`.

### Testing Set Membership

- [contains(_:)](<indexset/contains(__).md>) — Returns `true` if `self` contains `integer`.
- [contains(integersIn:)](<indexset/contains(integersin_)-9frtv.md>) — Returns `true` if `self` contains all of the integers in `indexSet`.
- [contains(integersIn:)](<indexset/contains(integersin_)-sma8.md>) — Returns `true` if `self` contains all of the integers in `range`.
- [intersects(integersIn:)](<indexset/intersects(integersin_)-3sdmv.md>) — Returns `true` if `self` intersects any of the integers in `range`.

### Manipulating Indexes

- [startIndex](indexset/startindex.md) — The beginning index in the set.
- [endIndex](indexset/endindex.md) — The ending index in the set.
- [index(after:)](<indexset/index(after_).md>) — Returns the index that follows the given index in the set.
- [index(before:)](<indexset/index(before_).md>) — Returns the index that precedes the given index in the set.
- [formIndex(after:)](<indexset/formindex(after_).md>) — Modifies the given index to refer to the item after the one it currently refers to.
- [formIndex(before:)](<indexset/formindex(before_).md>) — Modifies the given index to refer to the item before the one it currently refers to.
- [indexRange(in:)](<indexset/indexrange(in_)-539lz.md>) — Return a `Range<IndexSet.Index>` which can be used to subscript the index set.

### Finding Elements

- [integerLessThanOrEqualTo(_:)](<indexset/integerlessthanorequalto(__).md>) — Returns an integer contained in `self` which is less than or equal to `integer`, or `nil` if a result could not be found.
- [integerGreaterThan(_:)](<indexset/integergreaterthan(__).md>) — Returns an integer contained in `self` which is greater than `integer`, or `nil` if a result could not be found.
- [integerGreaterThanOrEqualTo(_:)](<indexset/integergreaterthanorequalto(__).md>) — Returns an integer contained in `self` which is greater than or equal to `integer`, or `nil` if a result could not be found.
- [integerLessThan(_:)](<indexset/integerlessthan(__).md>) — Returns an integer contained in `self` which is less than `integer`, or `nil` if a result could not be found.

### Selecting Elements

- [filteredIndexSet(in:includeInteger:)](<indexset/filteredindexset(in_includeinteger_)-6cdvc.md>) — Returns an IndexSet filtered according to the result of `includeInteger`.
- [filteredIndexSet(in:includeInteger:)](<indexset/filteredindexset(in_includeinteger_)-9dn86.md>) — Returns an IndexSet filtered according to the result of `includeInteger`.
- [filteredIndexSet(includeInteger:)](<indexset/filteredindexset(includeinteger_).md>) — Returns an IndexSet filtered according to the result of `includeInteger`.

### Iterating Over Elements

- [makeIterator()](<indexset/makeiterator().md>) — Returns an iterator over the elements of this sequence.

### Shifting Index Groups

- [shift(startingAt:by:)](<indexset/shift(startingat_by_).md>) — For a positive delta, shifts the indexes in [index, INT_MAX] to the right, thereby inserting an “empty space” [index, delta], for a negative delta, shifts the indexes in [index, INT_MAX] to the left, thereby deleting the indexes in the range [index - delta, delta].

### Getting a Range-Based View

- [rangeView(of:)](<indexset/rangeview(of_)-5xqe8.md>) — Returns a `Range`-based view of `self`.
- [rangeView](indexset/rangeview-swift.property.md) — Returns a `Range`-based view of the entire contents of `self`.
- [RangeView](indexset/rangeview-swift.struct.md) — A view of the contents of an IndexSet, organized by range.

### Using Reference Types

- [NSIndexSet](nsindexset.md) — An immutable collection of unique integer values that represent indexes in another collection.
- [NSMutableIndexSet](nsmutableindexset.md) — A mutable collection of unique integer values that represent indexes in another collection.

### Structures

- [Index](indexset/index.md) — The mechanism for accessing the integers stored in an IndexSet.

### Initializers

- [init(integersIn:)](<indexset/init(integersin_)-2zs95.md>) — Initialize an `IndexSet` with a range of integers.
- [init(integersIn:)](<indexset/init(integersin_)-54nqd.md>)

### Instance Properties

- [count](indexset/count.md) — Returns the number of integers in `self`.
- [first](indexset/first.md) — The first integer in `self`, or nil if `self` is empty.
- [isEmpty](indexset/isempty.md) — Returns `true` if self contains no values.
- [last](indexset/last.md) — The last integer in `self`, or nil if `self` is empty.

### Instance Methods

- [contains(integersIn:)](<indexset/contains(integersin_)-4k1o8.md>) — Returns `true` if `self` contains all of the integers in `range`.
- [count(in:)](<indexset/count(in_)-7irji.md>) — Returns the count of integers in `self` that intersect `range`.
- [indexRange(in:)](<indexset/indexrange(in_)-6057o.md>) — Return a `Range<IndexSet.Index>` which can be used to subscript the index set.
- [insert(integersIn:)](<indexset/insert(integersin_)-9wcrp.md>) — Insert a range of integers into the `IndexSet`.
- [intersects(integersIn:)](<indexset/intersects(integersin_)-9cq7w.md>) — Returns `true` if `self` intersects any of the integers in `range`.
- [rangeView(of:)](<indexset/rangeview(of_)-4jdy1.md>) — Returns a `Range`-based view of `self`.

### Type Aliases

- [Element](indexset/element.md) — An alias for the type that an index set holds.

## See Also

### Indexes

- [IndexPath](indexpath.md) — A list of indexes that together represent the path to a specific location in a tree of nested arrays.
