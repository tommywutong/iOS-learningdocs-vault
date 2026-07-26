---
title: 'decodeAtomicOptionalRepresentation(_:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/atomicoptionalrepresentable/decodeatomicoptionalrepresentation(_:)'
source_url: 'https://developer.apple.com/documentation/synchronization/atomicoptionalrepresentable/decodeatomicoptionalrepresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomicoptionalrepresentable/decodeatomicoptionalrepresentation%28_%3A%29.json'
content_hash: 'sha256:7971a5d96e24a40d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [AtomicOptionalRepresentable](../atomicoptionalrepresentable.md)

# decodeAtomicOptionalRepresentation(_:)

<sub>Type Method</sub>

Recovers the logical atomic type `Self?` by destroying some `AtomicOptionalRepresentation` storage instance returned from an atomic operation on `Optional`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func decodeAtomicOptionalRepresentation(_ representation: consuming Self.AtomicOptionalRepresentation) -> Self?
```

## Parameters

- `representation` — The optional storage representation for `Self?` that’s used within atomic operations on `Optional`.

## Return Value

The newly decoded logical type `Self?`.

## Discussion

> [!note] Note
> This is not an atomic operation. This simply decodes the storage representation used in atomic operations on `Optional` back into the logical type for normal use, `Self?`.
