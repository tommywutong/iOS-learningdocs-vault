---
title: 'identifier(fromComponents:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/identifier(fromcomponents:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/identifier(fromcomponents:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/identifier%28fromcomponents%3A%29.json'
content_hash: 'sha256:de90e4f161611b79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# identifier(fromComponents:)

<sub>Type Method</sub>

Constructs an identifier from a dictionary of components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func identifier(fromComponents components: [String : String]) -> String
```

## See Also

### Converting between identifiers

- [canonicalIdentifier(from:)](<canonicalidentifier(from_).md>) — Returns a canonical identifier from the given string.
- [components(fromIdentifier:)](<components(fromidentifier_).md>) — Returns a dictionary that splits an identifier into its component pieces. _(deprecated)_
- [identifier(_:from:)](<identifier(__from_).md>) — Returns the identifier conforming to the specified standard for the specified string.
- [IdentifierType](identifiertype.md) — A type that indicates the standard that defines a locale’s identifier.
- [canonicalLanguageIdentifier(from:)](<canonicallanguageidentifier(from_).md>) — Returns a canonical language identifier from the given string.
- [identifier(fromWindowsLocaleCode:)](<identifier(fromwindowslocalecode_).md>) — Returns the locale identifier from a given Windows locale code, or `nil` if it could not be converted.
- [windowsLocaleCode(fromIdentifier:)](<windowslocalecode(fromidentifier_).md>) — Returns the Windows locale code from a given identifier, or `nil` if it could not be converted.
