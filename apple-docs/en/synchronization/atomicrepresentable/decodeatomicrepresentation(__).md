---
title: 'decodeAtomicRepresentation(_:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/atomicrepresentable/decodeatomicrepresentation(_:)'
source_url: 'https://developer.apple.com/documentation/synchronization/atomicrepresentable/decodeatomicrepresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomicrepresentable/decodeatomicrepresentation%28_%3A%29.json'
content_hash: 'sha256:c92aebec18ac486f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [AtomicRepresentable](../atomicrepresentable.md)

# decodeAtomicRepresentation(_:)

<sub>Type Method</sub>

Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func decodeAtomicRepresentation(_ storage: consuming Self.AtomicRepresentation) -> Self
```

## Parameters

- `storage` — The storage representation for `Self` that’s used within atomic operations.

## Return Value

The newly decoded logical type `Self`.

## Discussion

> [!note] Note
> This is not an atomic operation. This simply decodes the storage representation used in atomic operations back into the logical type for normal use, `Self`.
