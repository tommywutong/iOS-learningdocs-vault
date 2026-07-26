---
title: Managed Buffers
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/managed-buffers
source_url: 'https://developer.apple.com/documentation/swift/managed-buffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managed-buffers.json'
content_hash: 'sha256:aba950ded852a0ab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md) · [Collections](collections.md)

# Managed Buffers

<sub>API Collection</sub>

Build your own buffer-backed collection types.

## Topics

### Buffer Implementation

- [ManagedBuffer](managedbuffer.md) — A class whose instances contain a property of type `Header` and raw storage for an array of `Element`, whose size is determined at instance creation.
- [ManagedBufferPointer](managedbufferpointer.md) — Contains a buffer object, and provides access to an instance of `Header` and contiguous storage for an arbitrary number of `Element` instances stored in that buffer.

### Uniqueness Checking

- [isKnownUniquelyReferenced(_:)](<isknownuniquelyreferenced(__)-98zpp.md>) — Returns a Boolean value indicating whether the given object is known to have a single strong reference.
- [isKnownUniquelyReferenced(_:)](<isknownuniquelyreferenced(__)-5kvtu.md>) — Returns a Boolean value indicating whether the given object is known to have a single strong reference.

## See Also

### Advanced Collection Topics

- [Sequence and Collection Protocols](sequence-and-collection-protocols.md) — Write generic code that works with any collection, or build your own collection types.
- [Supporting Types](supporting-types.md) — Use wrappers, indices, and iterators in operations like slicing, flattening, and reversing a collection.
