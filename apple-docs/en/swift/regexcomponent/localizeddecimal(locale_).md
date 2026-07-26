---
title: 'localizedDecimal(locale:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regexcomponent/localizeddecimal(locale:)'
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/localizeddecimal(locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/localizeddecimal%28locale%3A%29.json'
content_hash: 'sha256:3eb86ece71027b57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# localizedDecimal(locale:)

<sub>Type Method</sub>

Creates a regex component that matches a localized decimal string, capturing it as a Foundation decimal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func localizedDecimal(locale: Locale) -> Self
```

## Parameters

- `locale` — The locale that specifies formatting conventions to use when matching decimal strings.

## Return Value

A `RegexComponent` that matches localized decimal substrings as Foundation [Decimal](../../foundation/decimal.md) instances.

## Discussion

This method matches decimal substrings in accordance with the provided locale. For example, the value `1234567890.1234` formats as `1,234,567,890.1234` in the `en_US` locale, as `1 234 567 890,1234` in the `FR` locale, and as `1234567890.1234` in the `JP` locale. Because of this, the regex needs to know what locale convention to match against.

The following example creates a [Regex](../regex.md) that matches a date and time followed by whitespace and a decimal formatted in the `en_US` locale. It then matches this regex against a source string containing a date with this format, some whitespace, and a decimal value.

```swift
let enUSLocale = Locale(languageCode: .english, languageRegion: .unitedStates)
let source = "7/31/2022, 5:15:12 AM  1,234,567,890.1234"
let matcher = Regex {
    One(.dateTime(date: .numeric,
                  time: .standard,
                  locale: enUSLocale,
                  timeZone: TimeZone(identifier: "PST")!))
    OneOrMore(.horizontalWhitespace)
    Capture {
        One(.localizedDecimal(locale: enUSLocale))
    }
}
guard let match = source.firstMatch(of: matcher) else { return }
let decimal = match.1 // decimal == 1234567890.1234
```

## See Also

### Matching numeric formats

- [localizedInteger(locale:)](<localizedinteger(locale_).md>) — Creates a regex component that matches a localized numeric string, capturing it as an integer value.
- [localizedDouble(locale:)](<localizeddouble(locale_).md>) — Creates a regex component that matches a localized numeric string, capturing it as a double-precision floating-point value.
- [localizedCurrency(code:locale:)](<localizedcurrency(code_locale_).md>) — Creates a regex component that matches a localized currency string, capturing it as a decimal value.
- [localizedIntegerCurrency(code:locale:)](<localizedintegercurrency(code_locale_).md>) — Creates a regex component that matches a localized currency string, capturing it as an integer value.
- [localizedIntegerPercentage(locale:)](<localizedintegerpercentage(locale_).md>) — Creates a regex component that matches a localized percentage string, capturing it as a double-precision floating-point value.
- [localizedDoublePercentage(locale:)](<localizeddoublepercentage(locale_).md>) — Creates a regex component that matches a localized percentage string, capturing it as a double-precision floating-point value.
