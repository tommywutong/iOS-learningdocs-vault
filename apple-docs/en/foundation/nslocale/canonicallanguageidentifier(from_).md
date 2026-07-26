---
title: 'canonicalLanguageIdentifier(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/canonicallanguageidentifier(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/canonicallanguageidentifier(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/canonicallanguageidentifier%28from%3A%29.json'
content_hash: 'sha256:7eee35e3ab4c3a7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# canonicalLanguageIdentifier(from:)

<sub>Type Method</sub>

Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func canonicalLanguageIdentifier(from string: String) -> String
```

## Parameters

- `string` — A string representation of an arbitrary locale identifier.

## Return Value

A string that represents the canonical language identifier for the specified arbitrary locale identifier.

## See Also

### Converting Between Identifiers

- [+ canonicalLocaleIdentifierFromString:](<canonicallocaleidentifier(from_).md>) — Returns the canonical identifier for a given locale identification string.
- [+ componentsFromLocaleIdentifier:](<components(fromlocaleidentifier_).md>) — Returns a dictionary that is the result of parsing a locale ID.
- [+ localeIdentifierFromComponents:](<localeidentifier(fromcomponents_).md>) — Returns a locale identifier from the components specified in a given dictionary.
- [+ localeIdentifierFromWindowsLocaleCode:](<localeidentifier(fromwindowslocalecode_).md>) — Returns a locale identifier from a Windows locale code.
- [+ windowsLocaleCodeFromLocaleIdentifier:](<windowslocalecode(fromlocaleidentifier_).md>) — Returns a Window locale code from the locale identifier.
