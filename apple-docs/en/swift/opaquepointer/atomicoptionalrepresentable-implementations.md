---
title: AtomicOptionalRepresentable Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/opaquepointer/atomicoptionalrepresentable-implementations
source_url: 'https://developer.apple.com/documentation/swift/opaquepointer/atomicoptionalrepresentable-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/opaquepointer/atomicoptionalrepresentable-implementations.json'
content_hash: 'sha256:d253308d62b0f58c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [C Interoperability](../c-interoperability.md) · [OpaquePointer](../opaquepointer.md)

# AtomicOptionalRepresentable Implementations

<sub>API Collection</sub>

## Topics

### Type Aliases

- [AtomicOptionalRepresentation](atomicoptionalrepresentation.md) — The storage representation type that encodes to and decodes from `Optional<Self>` which is a suitable type when used in atomic operations on `Optional`.

### Type Methods

- [decodeAtomicOptionalRepresentation(_:)](<decodeatomicoptionalrepresentation(__).md>) — Recovers the logical atomic type `Self?` by destroying some `AtomicOptionalRepresentation` storage instance returned from an atomic operation on `Optional`.
- [encodeAtomicOptionalRepresentation(_:)](<encodeatomicoptionalrepresentation(__).md>) — Destroys a value of `Self` and prepares an `AtomicOptionalRepresentation` storage type to be used for atomic operations on `Optional`.
