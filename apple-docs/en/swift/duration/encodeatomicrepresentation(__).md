---
title: 'encodeAtomicRepresentation(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/encodeatomicrepresentation(_:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/encodeatomicrepresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/encodeatomicrepresentation%28_%3A%29.json'
content_hash: 'sha256:651bd014890d3253'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Duration](../duration.md)

# encodeAtomicRepresentation(_:)

<sub>Type Method</sub>

Destroys a value of `Self` and prepares an `AtomicRepresentation` storage type to be used for atomic operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func encodeAtomicRepresentation(_ value: consuming Duration) -> Duration.AtomicRepresentation
```

## Parameters

- `value` — A valid instance of `Self` that’s about to be destroyed to encode an instance of its `AtomicRepresentation`.

## Return Value

The newly encoded `AtomicRepresentation` storage.

## Discussion

> [!note] Note
> This is not an atomic operation. This simply encodes the logical type `Self` into its storage representation suitable for atomic operations, `AtomicRepresentation`.
