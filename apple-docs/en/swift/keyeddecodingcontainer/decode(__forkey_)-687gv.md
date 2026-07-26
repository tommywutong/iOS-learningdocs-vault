---
title: 'decode(_:forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyeddecodingcontainer/decode(_:forkey:)-687gv'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainer/decode(_:forkey:)-687gv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainer/decode%28_%3Aforkey%3A%29-687gv.json'
content_hash: 'sha256:ef118870bbc3e9bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainer](../keyeddecodingcontainer.md)

# decode(_:forKey:)

<sub>Instance Method</sub>

Decodes a value of the given type for the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode(_ type: Double.Type, forKey key: KeyedDecodingContainer<K>.Key) throws -> Double
```

## Parameters

- `type` — The type of value to decode.

- `key` — The key that the decoded value is associated with.

## Return Value

A value of the requested type, if present for the given key and convertible to the requested type.

## Discussion

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

> [!danger] Throws
> `DecodingError.keyNotFound` if `self` does not have an entry for the given key.

> [!danger] Throws
> `DecodingError.valueNotFound` if `self` has a null entry for the given key.
