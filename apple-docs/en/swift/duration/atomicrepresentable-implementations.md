---
title: AtomicRepresentable Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/atomicrepresentable-implementations
source_url: 'https://developer.apple.com/documentation/swift/duration/atomicrepresentable-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/atomicrepresentable-implementations.json'
content_hash: 'sha256:5ce7214b8eb9dfbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Time](../time-and-duration.md) · [Duration](../duration.md)

# AtomicRepresentable Implementations

<sub>API Collection</sub>

## Topics

### Type Aliases

- [AtomicRepresentation](atomicrepresentation.md) — The storage representation type that `Self` encodes to and decodes from which is a suitable type when used in atomic operations.

### Type Methods

- [decodeAtomicRepresentation(_:)](<decodeatomicrepresentation(__).md>) — Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.
- [encodeAtomicRepresentation(_:)](<encodeatomicrepresentation(__).md>) — Destroys a value of `Self` and prepares an `AtomicRepresentation` storage type to be used for atomic operations.
