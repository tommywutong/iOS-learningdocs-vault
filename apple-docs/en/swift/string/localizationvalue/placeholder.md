---
title: String.LocalizationValue.Placeholder
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/localizationvalue/placeholder
source_url: 'https://developer.apple.com/documentation/swift/string/localizationvalue/placeholder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/localizationvalue/placeholder.json'
content_hash: 'sha256:c3d468d87b40190d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [LocalizationValue](../localizationvalue.md)

# String.LocalizationValue.Placeholder

<sub>Enumeration</sub>

An enumeration of types that can appear as a placeholder in a string interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Placeholder
```

## Overview

Foundation uses this type when you create a string with the `\(placeholder: type)` syntax and supply an array of replacement values in a `String.LocalizationOptions`. Placeholders work with [String](../../string.md) initializers that take an `options:` parameter:

- [init(localized:options:table:bundle:locale:comment:)](<../init(localized_options_table_bundle_locale_comment_).md>)
- [init(localized:options:)](<../init(localized_options_).md>)
- [init(localized:defaultValue:options:table:bundle:locale:comment:)](<../init(localized_defaultvalue_options_table_bundle_locale_comment_).md>)

You only use this type directly when specifying one of its enumeration cases in the placeholder syntax, like `\(placeholder: .int)`.

## Relationships

- **Conforms To**: [Decodable](../../decodable.md), [Encodable](../../encodable.md), [Equatable](../../equatable.md), [Hashable](../../hashable.md), [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Placeholder types

- [String.LocalizationValue.Placeholder.int](placeholder/int.md) — The signed integer type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.uint](placeholder/uint.md) — The unsigned integer type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.float](placeholder/float.md) — The single-precision floating-point type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.double](placeholder/double.md) — The double-precision floating-point type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.object](placeholder/object.md) — The object type, as used for replacement values with the localized string placeholder syntax.
