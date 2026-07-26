---
title: Unicode.UTF8.ValidationError.Kind.RawValue
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/utf8/validationerror/kind-swift.struct/rawvalue-swift.typealias
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf8/validationerror/kind-swift.struct/rawvalue-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf8/validationerror/kind-swift.struct/rawvalue-swift.typealias.json'
content_hash: 'sha256:b0fa079eacc6c426'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Swift](../../../../../swift.md) · [Unicode](../../../../unicode.md) · [UTF8](../../../utf8.md) · [ValidationError](../../validationerror.md) · [Kind](../kind-swift.struct.md)

# Unicode.UTF8.ValidationError.Kind.RawValue

<sub>Type Alias</sub>

The raw type that can be used to represent all values of the conforming type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias RawValue = UInt8
```

## Discussion

Every distinct value of the conforming type has a corresponding unique value of the `RawValue` type, but there may be values of the `RawValue` type that don’t have a corresponding value of the conforming type.
