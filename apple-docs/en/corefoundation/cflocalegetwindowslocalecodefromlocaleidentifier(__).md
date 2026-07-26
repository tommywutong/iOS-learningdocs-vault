---
title: 'CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cflocalegetwindowslocalecodefromlocaleidentifier(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalegetwindowslocalecodefromlocaleidentifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalegetwindowslocalecodefromlocaleidentifier%28_%3A%29.json'
content_hash: 'sha256:f1e14d736efbb914'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(_:)

<sub>Function</sub>

Returns a Windows locale code from the locale identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier(_ localeIdentifier: CFLocaleIdentifier!) -> UInt32
```

## Parameters

- `localeIdentifier` — The locale identifier.

## Return Value

The Windows locale code.

## See Also

### Getting and Creating Locale Identifiers

- [CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes](<cflocalecreatecanonicallocaleidentifierfromscriptmanagercodes(______).md>) — Returns a canonical locale identifier from given language and region codes.
- [CFLocaleCreateCanonicalLanguageIdentifierFromString](<cflocalecreatecanonicallanguageidentifierfromstring(____).md>) — Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier
- [CFLocaleCreateCanonicalLocaleIdentifierFromString](<cflocalecreatecanonicallocaleidentifierfromstring(____).md>) — Returns a canonical locale identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [CFLocaleCreateComponentsFromLocaleIdentifier](<cflocalecreatecomponentsfromlocaleidentifier(____).md>) — Returns a dictionary containing the result from parsing a locale ID consisting of language, script, country or region, variant, and keyword/value pairs.
- [CFLocaleCreateLocaleIdentifierFromComponents](<cflocalecreatelocaleidentifierfromcomponents(____).md>) — Returns a locale identifier consisting of language, script, country or region, variant, and keyword/value pairs derived from a dictionary containing the source information.
- [CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode](<cflocalecreatelocaleidentifierfromwindowslocalecode(____).md>) — Returns a locale identifier from a Windows locale code.
