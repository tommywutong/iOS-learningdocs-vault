---
title: 'components(fromLocaleIdentifier:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/components(fromlocaleidentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/components(fromlocaleidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/components%28fromlocaleidentifier%3A%29.json'
content_hash: 'sha256:c6214ed5e7874ca6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# components(fromLocaleIdentifier:)

<sub>Type Method</sub>

Returns a dictionary that is the result of parsing a locale ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func components(fromLocaleIdentifier string: String) -> [String : String]
```

## Parameters

- `string` — A locale ID, consisting of language, script, country, variant, and keyword/value pairs, for example, `"en_US@calendar=japanese"`.

## Return Value

A dictionary that is the result of parsing `string` as a locale ID. The keys are the constant NSString constants corresponding to the locale ID components, and the values correspond to constants where available. For possible values, see [Key](key.md).

## Discussion

For example, the locale identifier `"en_US@calendar=japanese"` yields a dictionary with three entries:

- [NSLocaleLanguageCode](key/languagecode.md) = `en`
- [NSLocaleCountryCode](key/countrycode.md) = `US`
- [NSLocaleCalendar](key/calendar.md) = [NSJapaneseCalendar](../nsjapanesecalendar.md)

## See Also

### Converting Between Identifiers

- [+ canonicalLocaleIdentifierFromString:](<canonicallocaleidentifier(from_).md>) — Returns the canonical identifier for a given locale identification string.
- [+ localeIdentifierFromComponents:](<localeidentifier(fromcomponents_).md>) — Returns a locale identifier from the components specified in a given dictionary.
- [+ canonicalLanguageIdentifierFromString:](<canonicallanguageidentifier(from_).md>) — Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [+ localeIdentifierFromWindowsLocaleCode:](<localeidentifier(fromwindowslocalecode_).md>) — Returns a locale identifier from a Windows locale code.
- [+ windowsLocaleCodeFromLocaleIdentifier:](<windowslocalecode(fromlocaleidentifier_).md>) — Returns a Window locale code from the locale identifier.
