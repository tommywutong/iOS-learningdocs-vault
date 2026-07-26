---
title: 'canonicalLocaleIdentifier(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/canonicallocaleidentifier(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/canonicallocaleidentifier(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/canonicallocaleidentifier%28from%3A%29.json'
content_hash: 'sha256:30573cbe781c8ee1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# canonicalLocaleIdentifier(from:)

<sub>Type Method</sub>

Returns the canonical identifier for a given locale identification string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func canonicalLocaleIdentifier(from string: String) -> String
```

## Parameters

- `string` — A locale identification string.

## Return Value

The canonical identifier for an the locale identified by `string`.

## See Also

### Converting Between Identifiers

- [+ componentsFromLocaleIdentifier:](<components(fromlocaleidentifier_).md>) — Returns a dictionary that is the result of parsing a locale ID.
- [+ localeIdentifierFromComponents:](<localeidentifier(fromcomponents_).md>) — Returns a locale identifier from the components specified in a given dictionary.
- [+ canonicalLanguageIdentifierFromString:](<canonicallanguageidentifier(from_).md>) — Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [+ localeIdentifierFromWindowsLocaleCode:](<localeidentifier(fromwindowslocalecode_).md>) — Returns a locale identifier from a Windows locale code.
- [+ windowsLocaleCodeFromLocaleIdentifier:](<windowslocalecode(fromlocaleidentifier_).md>) — Returns a Window locale code from the locale identifier.
