---
title: 'conversationalTwoDigits(amPM:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/symbol/hour/conversationaltwodigits(ampm:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/conversationaltwodigits(ampm:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/hour/conversationaltwodigits%28ampm%3A%29.json'
content_hash: 'sha256:4e1fd47318a94cf5'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Hour](../hour.md)

# conversationalTwoDigits(amPM:)

<sub>Type Method</sub>

Custom format style portraying two digits that represent the hour and locale-dependent conversational day period formats.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func conversationalTwoDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour
```

## Parameters

- `amPM` — Specifies the format of the day period representation.

## Return Value

An hour format style customized according to the specified day period format style and the given locale.

## Discussion

This style pads the hour with a leading zero if necessary. This style may include the day period symbol (a.m. or p.m.), depending on locale, and can include conversational period formats. For example, `07a` (`narrow`), `07AM` (`abbreviated`), `07A.M.` (`wide`).

## See Also

### Modifying an Hour

- [defaultDigitsNoAMPM](defaultdigitsnoampm.md) — Custom format style portraying the minimum number of digits that represents the numeric hour. _(deprecated)_
- [twoDigitsNoAMPM](twodigitsnoampm.md) — Custom format style portraying the numeric hour using two digits. _(deprecated)_
- [conversationalDefaultDigits(amPM:)](<conversationaldefaultdigits(ampm_).md>) — Custom format style portraying the minimum number of digits that represents the hour and locale-dependent conversational day period formats.
- [defaultDigits(amPM:)](<defaultdigits(ampm_).md>) — Custom format style portraying the minimum number of digits that represents the hour and locale-dependent day period formats.
- [twoDigits(amPM:)](<twodigits(ampm_).md>) — Custom format style portraying two digits that represent the hour and locale-dependent day period formats.
