---
title: 'decodeIfPresent(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyeddecodingcontainer/decodeifpresent(_:)-o708'
source_url: 'https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decodeifpresent(_:)-o708'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyeddecodingcontainer/decodeifpresent%28_%3A%29-o708.json'
content_hash: 'sha256:366a568088ad0ebc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedDecodingContainer](../unkeyeddecodingcontainer.md)

# decodeIfPresent(_:)

<sub>Instance Method</sub>

Decodes a value of the given type, if present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func decodeIfPresent(_ type: Int128.Type) throws -> Int128?
```

## Parameters

- `type` — The type of value to decode.

## Return Value

A decoded value of the requested type, or `nil` if the value is a null value, or if there are no more elements to decode.

## Discussion

This method returns `nil` if the container has no elements left to decode, or if the value is null. The difference between these states can be distinguished by checking `isAtEnd`.

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.
