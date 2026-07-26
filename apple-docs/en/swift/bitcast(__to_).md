---
title: 'bitCast(_:to:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/bitcast(_:to:)'
source_url: 'https://developer.apple.com/documentation/swift/bitcast(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bitcast%28_%3Ato%3A%29.json'
content_hash: 'sha256:cf13ea2cee76d8a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# bitCast(_:to:)

<sub>Function</sub>

Returns the bits of the given instance, interpreted as having the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func bitCast<T, U>(_ original: T, to type: U.Type) -> U where T : ConvertibleToBytes, U : ConvertibleFromBytes
```

## Parameters

- `original` — The instance to cast to `type`.

- `type` — The type to cast `original` to.

## Return Value

A new instance of type `U`, cast from `original`.

## Discussion

`T` and `U` must have the same-sized memory representation. If they don’t, this function will trap.

## See Also

### Safe Access to Raw Bytes

- [FullyInhabited](fullyinhabited.md) — A protocol for types whose memory can safely be written as or read from raw bytes.
- [ConvertibleFromBytes](convertiblefrombytes.md) — A protocol for types whose memory can safely be populated from raw bytes, resulting in a valid instance.
- [ConvertibleToBytes](convertibletobytes.md) — A protocol for types whose memory can safely be read as individual raw bytes.
- [ByteOrder](byteorder.md) — A byte ordering in memory. _(beta)_
