---
title: String.LocalizationValue.Placeholder.object
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/localizationvalue/placeholder/object
source_url: 'https://developer.apple.com/documentation/swift/string/localizationvalue/placeholder/object'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/localizationvalue/placeholder/object.json'
content_hash: 'sha256:61756b1f5a924146'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [String](../../../string.md) · [LocalizationValue](../../localizationvalue.md) · [Placeholder](../placeholder.md)

# String.LocalizationValue.Placeholder.object

<sub>Case</sub>

The object type, as used for replacement values with the localized string placeholder syntax.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case object
```

## Discussion

To insert a object into a placeholder, use the syntax `\(placeholder: .object)`.

[LocalizationValue](../../localizationvalue.md) supports interpolating `NSObject` instances and Foundation types that bridge to `NSObject` types.

## See Also

### Placeholder types

- [String.LocalizationValue.Placeholder.int](int.md) — The signed integer type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.uint](uint.md) — The unsigned integer type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.float](float.md) — The single-precision floating-point type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.double](double.md) — The double-precision floating-point type, as used for replacement values with the localized string placeholder syntax.
