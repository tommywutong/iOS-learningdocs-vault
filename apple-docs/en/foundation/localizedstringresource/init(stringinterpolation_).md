---
title: 'init(stringInterpolation:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/localizedstringresource/init(stringinterpolation:)'
source_url: 'https://developer.apple.com/documentation/foundation/localizedstringresource/init(stringinterpolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/localizedstringresource/init%28stringinterpolation%3A%29.json'
content_hash: 'sha256:95d5319ea3bbcaa8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LocalizedStringResource](../localizedstringresource.md)

# init(stringInterpolation:)

<sub>Initializer</sub>

Creates a localized string resource from the given string interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(stringInterpolation: String.LocalizationValue.StringInterpolation)
```

## Parameters

- `stringInterpolation` — The key to use when looking up a localized value, created from a string interpolation.

## Discussion

To create a localized string key from a string interpolation, use the `\()` string interpolation syntax. Swift matches the parameter types in the expression to one of the `appendInterpolation` methods in `LocalizedStringResource/StringInterpolation`.

This initializer uses the default values from `LocalizedStringResource/init(_:table:locale:bundle:comment:)` for the `table`, `locale`, `bundle`, and `comment`.

## See Also

### Creating a localized string resource from literal values

- [init(stringLiteral:)](<init(stringliteral_).md>) — Creates a localized string resource from the specified string literal.
