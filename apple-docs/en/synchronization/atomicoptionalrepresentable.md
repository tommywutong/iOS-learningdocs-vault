---
title: AtomicOptionalRepresentable
framework: Synchronization
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/synchronization/atomicoptionalrepresentable
source_url: 'https://developer.apple.com/documentation/synchronization/atomicoptionalrepresentable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomicoptionalrepresentable.json'
content_hash: 'sha256:42264bc39705383f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Synchronization](../synchronization.md)

# AtomicOptionalRepresentable

<sub>Protocol</sub>

An atomic value that also supports atomic operations when wrapped in an `Optional`. Atomic optional representable types come with a standalone atomic representation for their optional-wrapped variants.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AtomicOptionalRepresentable : AtomicRepresentable
```

## Relationships

- **Inherits From**: [AtomicRepresentable](atomicrepresentable.md)

- **Conforming Types**: [ObjectIdentifier](../swift/objectidentifier.md), [OpaquePointer](../swift/opaquepointer.md), [Unmanaged](../swift/unmanaged.md), [UnsafeMutablePointer](../swift/unsafemutablepointer.md), [UnsafeMutableRawPointer](../swift/unsafemutablerawpointer.md), [UnsafePointer](../swift/unsafepointer.md), [UnsafeRawPointer](../swift/unsaferawpointer.md)

## Topics

### Associated Types

- [AtomicOptionalRepresentation](atomicoptionalrepresentable/atomicoptionalrepresentation.md) — The storage representation type that encodes to and decodes from `Optional<Self>` which is a suitable type when used in atomic operations on `Optional`.

### Type Methods

- [decodeAtomicOptionalRepresentation(_:)](<atomicoptionalrepresentable/decodeatomicoptionalrepresentation(__).md>) — Recovers the logical atomic type `Self?` by destroying some `AtomicOptionalRepresentation` storage instance returned from an atomic operation on `Optional`.
- [encodeAtomicOptionalRepresentation(_:)](<atomicoptionalrepresentable/encodeatomicoptionalrepresentation(__).md>) — Destroys a value of `Self` and prepares an `AtomicOptionalRepresentation` storage type to be used for atomic operations on `Optional`.

## See Also

### Atomic Values

- [Atomic](atomic.md) — An atomic value.
- [AtomicLazyReference](atomiclazyreference.md) — A lazily initializable atomic strong reference.
- [WordPair](wordpair.md) — A pair of two word sized `UInt`s.
- [AtomicRepresentable](atomicrepresentable.md) — A type that supports atomic operations through a separate atomic storage representation.
