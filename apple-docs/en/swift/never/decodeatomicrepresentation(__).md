---
title: 'decodeAtomicRepresentation(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/never/decodeatomicrepresentation(_:)'
source_url: 'https://developer.apple.com/documentation/swift/never/decodeatomicrepresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/never/decodeatomicrepresentation%28_%3A%29.json'
content_hash: 'sha256:e1e657137fd777d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Never](../never.md)

# decodeAtomicRepresentation(_:)

<sub>Type Method</sub>

Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func decodeAtomicRepresentation(_ representation: consuming Never) -> Never
```

## Return Value

The newly decoded logical type `Self`.

## Discussion

> [!note] Note
> This is not an atomic operation. This simply decodes the storage representation used in atomic operations back into the logical type for normal use, `Self`.
