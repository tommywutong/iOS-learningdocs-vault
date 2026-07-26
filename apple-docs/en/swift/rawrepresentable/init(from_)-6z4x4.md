---
title: 'init(from:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rawrepresentable/init(from:)-6z4x4'
source_url: 'https://developer.apple.com/documentation/swift/rawrepresentable/init(from:)-6z4x4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawrepresentable/init%28from%3A%29-6z4x4.json'
content_hash: 'sha256:0ea068cb9416ffbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawRepresentable](../rawrepresentable.md)

# init(from:)

<sub>Initializer</sub>

Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt16`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(from decoder: any Decoder) throws
```

## Parameters

- `decoder` — The decoder to read data from.

## Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## See Also

### Decoding a Value

- [init(from:)](<init(from_)-5auil.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `String`.
- [init(from:)](<init(from_)-5ar5m.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Bool`.
- [init(from:)](<init(from_)-417i8.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Double`.
- [init(from:)](<init(from_)-9u9tp.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Float`.
- [init(from:)](<init(from_)-4ibll.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int`.
- [init(from:)](<init(from_)-3hvw1.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt`.
- [init(from:)](<init(from_)-5ktev.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int8`.
- [init(from:)](<init(from_)-2hvc0.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int16`.
- [init(from:)](<init(from_)-114vz.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int32`.
- [init(from:)](<init(from_)-29lhi.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int64`.
- [init(from:)](<init(from_)-94955.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt8`.
- [init(from:)](<init(from_)-3arr3.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt32`.
- [init(from:)](<init(from_)-812cy.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt64`.
