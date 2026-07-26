---
title: 'windowsLocaleCode(fromLocaleIdentifier:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/windowslocalecode(fromlocaleidentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/windowslocalecode(fromlocaleidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/windowslocalecode%28fromlocaleidentifier%3A%29.json'
content_hash: 'sha256:62d81bc6bfb02ad4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# windowsLocaleCode(fromLocaleIdentifier:)

<sub>Type Method</sub>

Returns a Window locale code from the locale identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func windowsLocaleCode(fromLocaleIdentifier localeIdentifier: String) -> UInt32
```

## Parameters

- `localeIdentifier` — The locale identifier.

## Return Value

The Windows locale code.

## See Also

### Converting Between Identifiers

- [+ canonicalLocaleIdentifierFromString:](<canonicallocaleidentifier(from_).md>) — Returns the canonical identifier for a given locale identification string.
- [+ componentsFromLocaleIdentifier:](<components(fromlocaleidentifier_).md>) — Returns a dictionary that is the result of parsing a locale ID.
- [+ localeIdentifierFromComponents:](<localeidentifier(fromcomponents_).md>) — Returns a locale identifier from the components specified in a given dictionary.
- [+ canonicalLanguageIdentifierFromString:](<canonicallanguageidentifier(from_).md>) — Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [+ localeIdentifierFromWindowsLocaleCode:](<localeidentifier(fromwindowslocalecode_).md>) — Returns a locale identifier from a Windows locale code.
