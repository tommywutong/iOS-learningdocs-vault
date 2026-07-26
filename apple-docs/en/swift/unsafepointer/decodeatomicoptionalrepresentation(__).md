---
title: 'decodeAtomicOptionalRepresentation(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafepointer/decodeatomicoptionalrepresentation(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafepointer/decodeatomicoptionalrepresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafepointer/decodeatomicoptionalrepresentation%28_%3A%29.json'
content_hash: 'sha256:f4a05c32ed1706fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafePointer](../unsafepointer.md)

# decodeAtomicOptionalRepresentation(_:)

<sub>Type Method</sub>

Recovers the logical atomic type `Self?` by destroying some `AtomicOptionalRepresentation` storage instance returned from an atomic operation on `Optional`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func decodeAtomicOptionalRepresentation(_ representation: consuming UnsafePointer<Pointee>.AtomicOptionalRepresentation) -> UnsafePointer<Pointee>?
```

## Parameters

- `representation` — The optional storage representation for `Self?` that’s used within atomic operations on `Optional`.

## Return Value

The newly decoded logical type `Self?`.

## Discussion

> [!note] Note
> This is not an atomic operation. This simply decodes the storage representation used in atomic operations on `Optional` back into the logical type for normal use, `Self?`.
