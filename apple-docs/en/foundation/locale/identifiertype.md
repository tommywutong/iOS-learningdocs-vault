---
title: Locale.IdentifierType
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/identifiertype
source_url: 'https://developer.apple.com/documentation/foundation/locale/identifiertype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/identifiertype.json'
content_hash: 'sha256:4f7a31dce914d8fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# Locale.IdentifierType

<sub>Enumeration</sub>

A type that indicates the standard that defines a locale’s identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum IdentifierType
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Standard Identifier Types

- [Locale.IdentifierType.icu](identifiertype/icu.md) — The type of identifiers that follow ICU (International Components for Unicode) conventions.
- [Locale.IdentifierType.cldr](identifiertype/cldr.md) — The type of identifiers that follow CLDR (Common Locale Data Repository) conventions.
- [Locale.IdentifierType.bcp47](identifiertype/bcp47.md) — The type of BCP 47 language identifiers.

## See Also

### Converting between identifiers

- [canonicalIdentifier(from:)](<canonicalidentifier(from_).md>) — Returns a canonical identifier from the given string.
- [components(fromIdentifier:)](<components(fromidentifier_).md>) — Returns a dictionary that splits an identifier into its component pieces. _(deprecated)_
- [identifier(fromComponents:)](<identifier(fromcomponents_).md>) — Constructs an identifier from a dictionary of components.
- [identifier(_:from:)](<identifier(__from_).md>) — Returns the identifier conforming to the specified standard for the specified string.
- [canonicalLanguageIdentifier(from:)](<canonicallanguageidentifier(from_).md>) — Returns a canonical language identifier from the given string.
- [identifier(fromWindowsLocaleCode:)](<identifier(fromwindowslocalecode_).md>) — Returns the locale identifier from a given Windows locale code, or `nil` if it could not be converted.
- [windowsLocaleCode(fromIdentifier:)](<windowslocalecode(fromidentifier_).md>) — Returns the Windows locale code from a given identifier, or `nil` if it could not be converted.
