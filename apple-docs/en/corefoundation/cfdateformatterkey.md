---
title: CFDateFormatterKey
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdateformatterkey
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdateformatterkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdateformatterkey.json'
content_hash: 'sha256:f66aa768965ad2ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateFormatterKey

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFDateFormatterKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [kCFDateFormatterAMSymbol](cfdateformatterkey/amsymbol.md) — Specifies the AM symbol property, a CFString object.
- [kCFDateFormatterCalendar](cfdateformatterkey/calendar.md) — Specifies the calendar property, a CFCalendar object.
- [kCFDateFormatterCalendarName](cfdateformatterkey/calendarname.md) — Specifies the calendar name, a CFString object.
- [kCFDateFormatterDefaultDate](cfdateformatterkey/defaultdate.md) — Specifies the default date property, a CFDate object.
- [kCFDateFormatterDefaultFormat](cfdateformatterkey/defaultformat.md) — The original format string for the formatter (given the date & time style and locale specified at creation).
- [kCFDateFormatterDoesRelativeDateFormattingKey](cfdateformatterkey/doesrelativedateformattingkey.md) — Specifies the relative date formatting property, a CFBoolean object.
- [kCFDateFormatterEraSymbols](cfdateformatterkey/erasymbols.md) — Specifies the era symbols property, a CFArray of CFString objects.
- [kCFDateFormatterGregorianStartDate](cfdateformatterkey/gregorianstartdate.md) — Specifies the Gregorian start date property, a CFDate object.
- [kCFDateFormatterIsLenient](cfdateformatterkey/islenient.md) — Specifies the lenient property, a CFBoolean object where a true value indicates that the parsing of strings into date or absolute time values will be fuzzy.
- [kCFDateFormatterLongEraSymbols](cfdateformatterkey/longerasymbols.md) — Specifies the long era symbols property, a CFArray of CFString objects.
- [kCFDateFormatterMonthSymbols](cfdateformatterkey/monthsymbols.md) — Specifies the month symbols property, a CFArray of CFString objects.
- [kCFDateFormatterPMSymbol](cfdateformatterkey/pmsymbol.md) — Specifies the PM symbol property, a CFString object.
- [kCFDateFormatterQuarterSymbols](cfdateformatterkey/quartersymbols.md) — Specifies the quarter symbols property, a CFArray of CFString objects.
- [kCFDateFormatterShortMonthSymbols](cfdateformatterkey/shortmonthsymbols.md) — Specifies the short month symbols property, a CFArray of CFString objects.
- [kCFDateFormatterShortQuarterSymbols](cfdateformatterkey/shortquartersymbols.md) — Specifies the short quarter symbols property, a CFArray of CFString objects.
- [kCFDateFormatterShortStandaloneMonthSymbols](cfdateformatterkey/shortstandalonemonthsymbols.md) — Specifies the short standalone month symbols property, a CFArray of CFString objects.
- [kCFDateFormatterShortStandaloneQuarterSymbols](cfdateformatterkey/shortstandalonequartersymbols.md) — Specifies the short standalone quarter symbols property, a CFArray of CFString objects.
- [kCFDateFormatterShortStandaloneWeekdaySymbols](cfdateformatterkey/shortstandaloneweekdaysymbols.md) — Specifies the short standalone weekday symbols property, a CFArray of CFString objects.
- [kCFDateFormatterShortWeekdaySymbols](cfdateformatterkey/shortweekdaysymbols.md) — Specifies the short weekday symbols property, a CFArray of CFString objects.
- [kCFDateFormatterStandaloneMonthSymbols](cfdateformatterkey/standalonemonthsymbols.md) — Specifies the standalone month symbols property, a CFArray of CFString objects.
- [kCFDateFormatterStandaloneQuarterSymbols](cfdateformatterkey/standalonequartersymbols.md) — Specifies the standalone quarter symbols property, a CFArray of CFString objects.
- [kCFDateFormatterStandaloneWeekdaySymbols](cfdateformatterkey/standaloneweekdaysymbols.md) — Specifies the standalone weekday symbols property, a CFArray of CFString objects.
- [kCFDateFormatterTimeZone](cfdateformatterkey/timezone.md) — Specifies the time zone property, a CFTimeZone object.
- [kCFDateFormatterTwoDigitStartDate](cfdateformatterkey/twodigitstartdate.md) — Specifies the property representing the date from which two-digit years start, a CFDate object.
- [kCFDateFormatterVeryShortMonthSymbols](cfdateformatterkey/veryshortmonthsymbols.md) — Specifies the very short month symbols property, a CFArray of CFString objects.
- [kCFDateFormatterVeryShortStandaloneMonthSymbols](cfdateformatterkey/veryshortstandalonemonthsymbols.md) — Specifies the very short standalone month symbols property, a CFArray of CFString objects.
- [kCFDateFormatterVeryShortStandaloneWeekdaySymbols](cfdateformatterkey/veryshortstandaloneweekdaysymbols.md) — Specifies the very short standalone weekday symbols property, a CFArray of CFString objects.
- [kCFDateFormatterVeryShortWeekdaySymbols](cfdateformatterkey/veryshortweekdaysymbols.md) — Specifies the very short weekday symbols property, a CFArray of CFString objects.
- [kCFDateFormatterWeekdaySymbols](cfdateformatterkey/weekdaysymbols.md) — Specifies the weekday symbols property, a CFArray of CFString objects.

### Initializers

- [init(rawValue:)](<cfdateformatterkey/init(rawvalue_).md>)

## See Also

### Data Types

- [CFAllocatorTypeID](cfallocatortypeid.md)
- [CFCalendarIdentifier](cfcalendaridentifier.md)
- [CFErrorDomain](cferrordomain.md)
- [CFLocaleIdentifier](cflocaleidentifier.md)
- [CFLocaleKey](cflocalekey.md)
- [CFNotificationName](cfnotificationname.md)
- [CFNumberFormatterKey](cfnumberformatterkey.md)
- [CFRunLoopMode](cfrunloopmode.md)
- [CFStreamPropertyKey](cfstreampropertykey.md)
- [CFTypeRef](cftyperef.md) — An untyped “generic” reference to any Core Foundation object.
