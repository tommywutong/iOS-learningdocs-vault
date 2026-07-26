---
title: 'encodeAtomicOptionalRepresentation(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafepointer/encodeatomicoptionalrepresentation(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafepointer/encodeatomicoptionalrepresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafepointer/encodeatomicoptionalrepresentation%28_%3A%29.json'
content_hash: 'sha256:dbf69db1f4cec384'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafePointer](../unsafepointer.md)

# encodeAtomicOptionalRepresentation(_:)

<sub>Type Method</sub>

Destroys a value of `Self` and prepares an `AtomicOptionalRepresentation` storage type to be used for atomic operations on `Optional`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func encodeAtomicOptionalRepresentation(_ value: consuming UnsafePointer<Pointee>?) -> UnsafePointer<Pointee>.AtomicOptionalRepresentation
```

## Parameters

- `value` — An optional instance of `Self` that’s about to be destroyed to encode an instance of its `AtomicOptionalRepresentation`.

## Return Value

The newly encoded `AtomicOptionalRepresentation` storage.

## Discussion

> [!note] Note
> This is not an atomic operation. This simply encodes the logical type `Self` into its storage representation suitable for atomic operations, `AtomicOptionalRepresentation`.
