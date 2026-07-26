---
title: 'identifier(_:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/identifier(_:from:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/identifier(_:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/identifier%28_%3Afrom%3A%29.json'
content_hash: 'sha256:974d2d9ac0c5c43e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# identifier(_:from:)

<sub>Type Method</sub>

Returns the identifier conforming to the specified standard for the specified string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func identifier(_ type: Locale.IdentifierType, from string: String) -> String
```

## Parameters

- `type` — The identifier type used by `string`, such as [Locale.IdentifierType.icu](identifiertype/icu.md) or [Locale.IdentifierType.bcp47](identifiertype/bcp47.md).

- `string` — An identifier string that complies with the standard indicated by `type`.

## Return Value

A locale identifier.

## See Also

### Converting between identifiers

- [canonicalIdentifier(from:)](<canonicalidentifier(from_).md>) — Returns a canonical identifier from the given string.
- [components(fromIdentifier:)](<components(fromidentifier_).md>) — Returns a dictionary that splits an identifier into its component pieces. _(deprecated)_
- [identifier(fromComponents:)](<identifier(fromcomponents_).md>) — Constructs an identifier from a dictionary of components.
- [IdentifierType](identifiertype.md) — A type that indicates the standard that defines a locale’s identifier.
- [canonicalLanguageIdentifier(from:)](<canonicallanguageidentifier(from_).md>) — Returns a canonical language identifier from the given string.
- [identifier(fromWindowsLocaleCode:)](<identifier(fromwindowslocalecode_).md>) — Returns the locale identifier from a given Windows locale code, or `nil` if it could not be converted.
- [windowsLocaleCode(fromIdentifier:)](<windowslocalecode(fromidentifier_).md>) — Returns the Windows locale code from a given identifier, or `nil` if it could not be converted.
