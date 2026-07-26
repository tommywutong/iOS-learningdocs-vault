---
title: availableLocaleIdentifiers
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslocale/availablelocaleidentifiers
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/availablelocaleidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/availablelocaleidentifiers.json'
content_hash: 'sha256:b42c1f63cabbc6f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# availableLocaleIdentifiers

<sub>Type Property</sub>

The list of locale identifiers available on the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var availableLocaleIdentifiers: [String] { get }
```

## Discussion

A locale identifier starts with a language code, often includes a region code, and occasionally includes a script designator.  See [Locale IDs](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html#//apple_ref/doc/uid/10000171i-CH15-SW9) for more information about the structure of a locale identifier.

Use [- localizedStringForLocaleIdentifier:](<localizedstring(forlocaleidentifier_).md>) to obtain a human readable description of any of the locale identifiers in this list.

## See Also

### Related Documentation

- [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i)

### Getting Known Identifiers and Codes

- [ISOCountryCodes](isocountrycodes.md) — The list of known country or region codes.
- [ISOLanguageCodes](isolanguagecodes.md) — The list of known language codes.
- [ISOCurrencyCodes](isocurrencycodes.md) — The list of known currency codes.
- [commonISOCurrencyCodes](commonisocurrencycodes.md) — A list of commonly encountered currency codes.
