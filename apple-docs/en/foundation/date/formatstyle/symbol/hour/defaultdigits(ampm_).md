---
title: 'defaultDigits(amPM:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/symbol/hour/defaultdigits(ampm:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/defaultdigits(ampm:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/hour/defaultdigits%28ampm%3A%29.json'
content_hash: 'sha256:daa50cc9911c1de8'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Hour](../hour.md)

# defaultDigits(amPM:)

<sub>Type Method</sub>

Custom format style portraying the minimum number of digits that represents the hour and locale-dependent day period formats.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func defaultDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour
```

## Parameters

- `amPM` — Specifies the format of the day period representation.

## Return Value

An hour format style customized according to the specified day period format style and the given locale.

## Discussion

This style may include the day period symbol (a.m. or p.m.), depending on locale. For example, `7a` (`narrow`), `7AM` (`abbreviated`), `7A.M.` (`wide`).

## See Also

### Modifying an Hour

- [defaultDigitsNoAMPM](defaultdigitsnoampm.md) — Custom format style portraying the minimum number of digits that represents the numeric hour. _(deprecated)_
- [twoDigitsNoAMPM](twodigitsnoampm.md) — Custom format style portraying the numeric hour using two digits. _(deprecated)_
- [conversationalDefaultDigits(amPM:)](<conversationaldefaultdigits(ampm_).md>) — Custom format style portraying the minimum number of digits that represents the hour and locale-dependent conversational day period formats.
- [conversationalTwoDigits(amPM:)](<conversationaltwodigits(ampm_).md>) — Custom format style portraying two digits that represent the hour and locale-dependent conversational day period formats.
- [twoDigits(amPM:)](<twodigits(ampm_).md>) — Custom format style portraying two digits that represent the hour and locale-dependent day period formats.
