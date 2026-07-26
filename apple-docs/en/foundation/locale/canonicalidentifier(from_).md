---
title: 'canonicalIdentifier(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 8.0+（16.0 起废弃）, macOS 10.10+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+, watchOS 2.0+（9.0 起废弃）]
languages: [swift, swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/locale/canonicalidentifier(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/canonicalidentifier(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/canonicalidentifier%28from%3A%29.json'
content_hash: 'sha256:7b7ba68ffc010b0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# canonicalIdentifier(from:)

<sub>Type Method</sub>

Returns a canonical identifier from the given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func canonicalIdentifier(from string: String) -> String
```

## See Also

### Converting between identifiers

- [components(fromIdentifier:)](<components(fromidentifier_).md>) — Returns a dictionary that splits an identifier into its component pieces. _(deprecated)_
- [identifier(fromComponents:)](<identifier(fromcomponents_).md>) — Constructs an identifier from a dictionary of components.
- [identifier(_:from:)](<identifier(__from_).md>) — Returns the identifier conforming to the specified standard for the specified string.
- [IdentifierType](identifiertype.md) — A type that indicates the standard that defines a locale’s identifier.
- [canonicalLanguageIdentifier(from:)](<canonicallanguageidentifier(from_).md>) — Returns a canonical language identifier from the given string.
- [identifier(fromWindowsLocaleCode:)](<identifier(fromwindowslocalecode_).md>) — Returns the locale identifier from a given Windows locale code, or `nil` if it could not be converted.
- [windowsLocaleCode(fromIdentifier:)](<windowslocalecode(fromidentifier_).md>) — Returns the Windows locale code from a given identifier, or `nil` if it could not be converted.
