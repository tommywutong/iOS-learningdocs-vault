---
title: 'init(stringLiteral:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/localizedstringresource/init(stringliteral:)'
source_url: 'https://developer.apple.com/documentation/foundation/localizedstringresource/init(stringliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/localizedstringresource/init%28stringliteral%3A%29.json'
content_hash: 'sha256:7219aa97ecfd206d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LocalizedStringResource](../localizedstringresource.md)

# init(stringLiteral:)

<sub>Initializer</sub>

Creates a localized string resource from the specified string literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(stringLiteral value: String)
```

## Parameters

- `value` — The key to use when looking up a localized value.

## Discussion

This initializer uses the default values from `LocalizedStringResource/init(_:table:locale:bundle:comment:)` for the `table`, `locale`, `bundle`, and `comment`.

## See Also

### Creating a localized string resource from literal values

- [init(stringInterpolation:)](<init(stringinterpolation_).md>) — Creates a localized string resource from the given string interpolation.
