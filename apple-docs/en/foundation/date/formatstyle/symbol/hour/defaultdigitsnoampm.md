---
title: defaultDigitsNoAMPM
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/hour/defaultdigitsnoampm
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/defaultdigitsnoampm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/hour/defaultdigitsnoampm.json'
content_hash: 'sha256:125e866edf32b986'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Hour](../hour.md)

# defaultDigitsNoAMPM

<sub>Type Property</sub>

Custom format style portraying the minimum number of digits that represents the numeric hour.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var defaultDigitsNoAMPM: Date.FormatStyle.Symbol.Hour { get }
```

## Discussion

This style doesn’t include the day period symbol (a.m. or p.m.). For example, `1`, `11`.

## See Also

### Modifying an Hour

- [twoDigitsNoAMPM](twodigitsnoampm.md) — Custom format style portraying the numeric hour using two digits. _(deprecated)_
- [conversationalDefaultDigits(amPM:)](<conversationaldefaultdigits(ampm_).md>) — Custom format style portraying the minimum number of digits that represents the hour and locale-dependent conversational day period formats.
- [conversationalTwoDigits(amPM:)](<conversationaltwodigits(ampm_).md>) — Custom format style portraying two digits that represent the hour and locale-dependent conversational day period formats.
- [defaultDigits(amPM:)](<defaultdigits(ampm_).md>) — Custom format style portraying the minimum number of digits that represents the hour and locale-dependent day period formats.
- [twoDigits(amPM:)](<twodigits(ampm_).md>) — Custom format style portraying two digits that represent the hour and locale-dependent day period formats.
