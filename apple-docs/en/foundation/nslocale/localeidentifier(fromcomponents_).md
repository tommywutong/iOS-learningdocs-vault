---
title: 'localeIdentifier(fromComponents:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/localeidentifier(fromcomponents:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/localeidentifier(fromcomponents:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/localeidentifier%28fromcomponents%3A%29.json'
content_hash: 'sha256:5b58d10ae891eb4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# localeIdentifier(fromComponents:)

<sub>Type Method</sub>

Returns a locale identifier from the components specified in a given dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func localeIdentifier(fromComponents dict: [String : String]) -> String
```

## Parameters

- `dict` — A dictionary containing components that specify a locale. For possible values, see `NSLocale Component Keys`.

## Return Value

A locale identifier created from the components specified in `dict`.

## Discussion

This reverses the actions of [+ componentsFromLocaleIdentifier:](<components(fromlocaleidentifier_).md>), so for example the dictionary `{NSLocaleLanguageCode="en", NSLocaleCountryCode="US", NSLocaleCalendar=NSJapaneseCalendar}` becomes `"en_US@calendar=japanese"`.

## See Also

### Related Documentation

- [ISOLanguageCodes](isolanguagecodes.md) — The list of known language codes.

### Converting Between Identifiers

- [+ canonicalLocaleIdentifierFromString:](<canonicallocaleidentifier(from_).md>) — Returns the canonical identifier for a given locale identification string.
- [+ componentsFromLocaleIdentifier:](<components(fromlocaleidentifier_).md>) — Returns a dictionary that is the result of parsing a locale ID.
- [+ canonicalLanguageIdentifierFromString:](<canonicallanguageidentifier(from_).md>) — Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [+ localeIdentifierFromWindowsLocaleCode:](<localeidentifier(fromwindowslocalecode_).md>) — Returns a locale identifier from a Windows locale code.
- [+ windowsLocaleCodeFromLocaleIdentifier:](<windowslocalecode(fromlocaleidentifier_).md>) — Returns a Window locale code from the locale identifier.
