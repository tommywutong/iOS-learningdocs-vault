---
title: 'localeIdentifier(fromWindowsLocaleCode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/localeidentifier(fromwindowslocalecode:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/localeidentifier(fromwindowslocalecode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/localeidentifier%28fromwindowslocalecode%3A%29.json'
content_hash: 'sha256:e35850944c7ebc2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# localeIdentifier(fromWindowsLocaleCode:)

<sub>Type Method</sub>

Returns a locale identifier from a Windows locale code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func localeIdentifier(fromWindowsLocaleCode lcid: UInt32) -> String?
```

## Parameters

- `lcid` — The Windows locale code.

## Return Value

The locale identifier.

## See Also

### Converting Between Identifiers

- [+ canonicalLocaleIdentifierFromString:](<canonicallocaleidentifier(from_).md>) — Returns the canonical identifier for a given locale identification string.
- [+ componentsFromLocaleIdentifier:](<components(fromlocaleidentifier_).md>) — Returns a dictionary that is the result of parsing a locale ID.
- [+ localeIdentifierFromComponents:](<localeidentifier(fromcomponents_).md>) — Returns a locale identifier from the components specified in a given dictionary.
- [+ canonicalLanguageIdentifierFromString:](<canonicallanguageidentifier(from_).md>) — Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [+ windowsLocaleCodeFromLocaleIdentifier:](<windowslocalecode(fromlocaleidentifier_).md>) — Returns a Window locale code from the locale identifier.
