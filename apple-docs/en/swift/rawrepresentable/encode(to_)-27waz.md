---
title: 'encode(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rawrepresentable/encode(to:)-27waz'
source_url: 'https://developer.apple.com/documentation/swift/rawrepresentable/encode(to:)-27waz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawrepresentable/encode%28to%3A%29-27waz.json'
content_hash: 'sha256:21450cb563b31753'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawRepresentable](../rawrepresentable.md)

# encode(to:)

<sub>Instance Method</sub>

Encodes this value into the given encoder, when the type’s `RawValue` is `UInt32`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode(to encoder: any Encoder) throws
```

## Parameters

- `encoder` — The encoder to write data to.

## Discussion

This function throws an error if any values are invalid for the given encoder’s format.

## See Also

### Encoding a Value

- [encode(to:)](<encode(to_)-4evma.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `String`.
- [encode(to:)](<encode(to_)-5igsi.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Bool`.
- [encode(to:)](<encode(to_)-4tbh4.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Double`.
- [encode(to:)](<encode(to_)-21ma8.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Float`.
- [encode(to:)](<encode(to_)-8horh.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Int`.
- [encode(to:)](<encode(to_)-78oqu.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `UInt`.
- [encode(to:)](<encode(to_)-4pavm.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Int8`.
- [encode(to:)](<encode(to_)-86dqn.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Int16`.
- [encode(to:)](<encode(to_)-7dyeb.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Int32`.
- [encode(to:)](<encode(to_)-4gohs.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Int64`.
- [encode(to:)](<encode(to_)-9u5rt.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `UInt8`.
- [encode(to:)](<encode(to_)-cla3.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `UInt16`.
- [encode(to:)](<encode(to_)-16ame.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `UInt64`.
