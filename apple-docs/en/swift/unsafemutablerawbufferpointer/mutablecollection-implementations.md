---
title: MutableCollection Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafemutablerawbufferpointer/mutablecollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/mutablecollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/mutablecollection-implementations.json'
content_hash: 'sha256:3c6c315723539bb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Manual Memory Management](../manual-memory-management.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# MutableCollection Implementations

<sub>API Collection</sub>

## Topics

### Instance Methods

- [moveSubranges(_:to:)](<movesubranges(__to_).md>) — Moves the elements in the given subranges to just before the element at the specified index.
- [partition(by:)](<partition(by_)-33su4.md>) — Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [partition(by:)](<partition(by_)-90pny.md>) — Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [reverse()](<reverse().md>) — Reverses the elements of the collection in place.
- [shuffle()](<shuffle().md>) — Shuffles the collection in place.
- [shuffle(using:)](<shuffle(using_).md>) — Shuffles the collection in place, using the given generator as a source for randomness.
- [sort()](<sort().md>) — Sorts the collection in place.
- [sort(by:)](<sort(by_).md>) — Sorts the collection in place, using the given predicate as the comparison between elements.
- [swapAt(_:_:)](<swapat(____).md>) — Exchanges the byte values at the specified indices in this buffer’s memory.
- [withContiguousMutableStorageIfAvailable(_:)](<withcontiguousmutablestorageifavailable(__).md>) — Executes a closure on the collection’s contiguous storage.

### Subscripts

- [subscript(_:)](<subscript(__)-3g42.md>) — Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](<subscript(__)-3i1y.md>) — Accesses a contiguous subrange of the collection’s elements. _(deprecated)_
- [subscript(_:)](<subscript(__)-3kwnc.md>)
- [subscript(_:)](<subscript(__)-3pmfu.md>)
- [subscript(_:)](<subscript(__)-9v9lo.md>) _(deprecated)_
- [subscript(_:)](<subscript(__)-u791.md>) — Accesses the byte at the given offset in the memory region as a `UInt8` value.
- [subscript(_:)](<subscript(__)-znv7.md>) — Accesses the bytes in the specified memory region.
