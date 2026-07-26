---
title: String.LocalizationValue.Placeholder.uint
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/localizationvalue/placeholder/uint
source_url: 'https://developer.apple.com/documentation/swift/string/localizationvalue/placeholder/uint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/localizationvalue/placeholder/uint.json'
content_hash: 'sha256:13dc9e75022e2373'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [String](../../../string.md) · [LocalizationValue](../../localizationvalue.md) · [Placeholder](../placeholder.md)

# String.LocalizationValue.Placeholder.uint

<sub>Case</sub>

The unsigned integer type, as used for replacement values with the localized string placeholder syntax.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case uint
```

## Discussion

To insert an unsigned integer into a placeholder, use the syntax `\(placeholder: .uint)`.

The various `String(localized:)` initializers apply a locale-appropriate `FormatStyle` to the numeric value, based on the `locale:` parameter or the `LocalizedStringResource`.

## See Also

### Placeholder types

- [String.LocalizationValue.Placeholder.int](int.md) — The signed integer type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.float](float.md) — The single-precision floating-point type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.double](double.md) — The double-precision floating-point type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.object](object.md) — The object type, as used for replacement values with the localized string placeholder syntax.
