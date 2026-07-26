---
title: Collections
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collections
source_url: 'https://developer.apple.com/documentation/swift/collections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collections.json'
content_hash: 'sha256:1fdf42d889c08598'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md)

# Collections

<sub>API Collection</sub>

Store and organize data using arrays, dictionaries, sets, and other data structures.

## Topics

### Arrays and Dictionaries

- [Array](array.md) — An ordered, random-access collection.
- [Dictionary](dictionary.md) — A collection whose elements are key-value pairs.
- [InlineArray](inlinearray.md) — A fixed-size array.

### Sets

- [Set](set.md) — An unordered collection of unique elements.
- [OptionSet](optionset.md) — A type that presents a mathematical set interface to a bit set.

### Ranges

- [..\<(_:_:)](<comparable/'.._(____).md>) — Returns a half-open range that contains its lower bound but not its upper bound.
- [Range](range.md) — A half-open interval from a lower bound up to, but not including, an upper bound.
- [RangeSet](rangeset.md) — A set of values of any comparable type, represented by ranges.
- [...(_:_:)](<comparable/'...(____).md>) — Returns a closed range that contains both of its bounds.
- [ClosedRange](closedrange.md) — An interval from a lower bound up to, and including, an upper bound.

### Strides

- [stride(from:to:by:)](<stride(from_to_by_).md>) — Returns a sequence from a starting value to, but not including, an end value, stepping by the specified amount.
- [stride(from:through:by:)](<stride(from_through_by_).md>) — Returns a sequence from a starting value toward, and possibly including, an end value, stepping by the specified amount.

### Special-Use Collections

- [repeatElement(_:count:)](<repeatelement(__count_).md>) — Creates a collection containing the specified number of the given element.
- [CollectionOfOne](collectionofone.md) — A collection containing a single element.
- [EmptyCollection](emptycollection.md) — A collection whose element type is `Element` but that is always empty.
- [KeyValuePairs](keyvaluepairs.md) — A lightweight collection of key-value pairs.
- [DictionaryLiteral](dictionaryliteral.md)

### Dynamic Sequences

- [sequence(first:next:)](<sequence(first_next_).md>) — Returns a sequence formed from `first` and repeated lazy applications of `next`.
- [sequence(state:next:)](<sequence(state_next_).md>) — Returns a sequence formed from repeated lazy applications of `next` to a mutable `state`.

### Joint Iteration

- [zip(_:_:)](<zip(____).md>) — Creates a sequence of pairs built out of two underlying sequences.

### Advanced Collection Topics

- [Sequence and Collection Protocols](sequence-and-collection-protocols.md) — Write generic code that works with any collection, or build your own collection types.
- [Supporting Types](supporting-types.md) — Use wrappers, indices, and iterators in operations like slicing, flattening, and reversing a collection.
- [Managed Buffers](managed-buffers.md) — Build your own buffer-backed collection types.

## See Also

### Values and Collections

- [Numbers and Basic Values](numbers-and-basic-values.md) — Model data with numbers, Boolean values, and other fundamental types.
- [Strings and Text](strings-and-text.md) — Work with text using Unicode-safe strings.
- [Time](time-and-duration.md) — Measure how long an operation takes and determine schedules in the future.
