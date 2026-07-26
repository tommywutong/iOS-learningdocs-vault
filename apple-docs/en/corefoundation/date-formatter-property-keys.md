---
title: Date Formatter Property Keys
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/date-formatter-property-keys
source_url: 'https://developer.apple.com/documentation/corefoundation/date-formatter-property-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/date-formatter-property-keys.json'
content_hash: 'sha256:464d1e960276b6d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFDateFormatter](cfdateformatter.md)

# Date Formatter Property Keys

<sub>API Collection</sub>

Keys used in key-value pairs to discover and specify the value of date formatter properties—used in conjunction with [CFDateFormatterCopyProperty](<cfdateformattercopyproperty(____).md>) and [CFDateFormatterSetProperty](<cfdateformattersetproperty(______).md>).

## Overview

The values for these keys are all CFType objects. The specific types for each key are specified above.

## Topics

### Constants

- [kCFDateFormatterIsLenient](cfdateformatterkey/islenient.md) — Specifies the lenient property, a CFBoolean object where a true value indicates that the parsing of strings into date or absolute time values will be fuzzy.
- [kCFDateFormatterTimeZone](cfdateformatterkey/timezone.md) — Specifies the time zone property, a CFTimeZone object.
- [kCFDateFormatterCalendarName](cfdateformatterkey/calendarname.md) — Specifies the calendar name, a CFString object.
- [kCFDateFormatterDefaultFormat](cfdateformatterkey/defaultformat.md) — The original format string for the formatter (given the date & time style and locale specified at creation).
- [kCFDateFormatterTwoDigitStartDate](cfdateformatterkey/twodigitstartdate.md) — Specifies the property representing the date from which two-digit years start, a CFDate object.
- [kCFDateFormatterDefaultDate](cfdateformatterkey/defaultdate.md) — Specifies the default date property, a CFDate object.
- [kCFDateFormatterCalendar](cfdateformatterkey/calendar.md) — Specifies the calendar property, a CFCalendar object.
- [kCFDateFormatterEraSymbols](cfdateformatterkey/erasymbols.md) — Specifies the era symbols property, a CFArray of CFString objects.
- [kCFDateFormatterMonthSymbols](cfdateformatterkey/monthsymbols.md) — Specifies the month symbols property, a CFArray of CFString objects.
- [kCFDateFormatterShortMonthSymbols](cfdateformatterkey/shortmonthsymbols.md) — Specifies the short month symbols property, a CFArray of CFString objects.
- [kCFDateFormatterWeekdaySymbols](cfdateformatterkey/weekdaysymbols.md) — Specifies the weekday symbols property, a CFArray of CFString objects.
- [kCFDateFormatterShortWeekdaySymbols](cfdateformatterkey/shortweekdaysymbols.md) — Specifies the short weekday symbols property, a CFArray of CFString objects.
- [kCFDateFormatterAMSymbol](cfdateformatterkey/amsymbol.md) — Specifies the AM symbol property, a CFString object.
- [kCFDateFormatterPMSymbol](cfdateformatterkey/pmsymbol.md) — Specifies the PM symbol property, a CFString object.
- [kCFDateFormatterLongEraSymbols](cfdateformatterkey/longerasymbols.md) — Specifies the long era symbols property, a CFArray of CFString objects.
- [kCFDateFormatterVeryShortMonthSymbols](cfdateformatterkey/veryshortmonthsymbols.md) — Specifies the very short month symbols property, a CFArray of CFString objects.
- [kCFDateFormatterStandaloneMonthSymbols](cfdateformatterkey/standalonemonthsymbols.md) — Specifies the standalone month symbols property, a CFArray of CFString objects.
- [kCFDateFormatterShortStandaloneMonthSymbols](cfdateformatterkey/shortstandalonemonthsymbols.md) — Specifies the short standalone month symbols property, a CFArray of CFString objects.
- [kCFDateFormatterVeryShortStandaloneMonthSymbols](cfdateformatterkey/veryshortstandalonemonthsymbols.md) — Specifies the very short standalone month symbols property, a CFArray of CFString objects.
- [kCFDateFormatterVeryShortWeekdaySymbols](cfdateformatterkey/veryshortweekdaysymbols.md) — Specifies the very short weekday symbols property, a CFArray of CFString objects.
- [kCFDateFormatterStandaloneWeekdaySymbols](cfdateformatterkey/standaloneweekdaysymbols.md) — Specifies the standalone weekday symbols property, a CFArray of CFString objects.
- [kCFDateFormatterShortStandaloneWeekdaySymbols](cfdateformatterkey/shortstandaloneweekdaysymbols.md) — Specifies the short standalone weekday symbols property, a CFArray of CFString objects.
- [kCFDateFormatterVeryShortStandaloneWeekdaySymbols](cfdateformatterkey/veryshortstandaloneweekdaysymbols.md) — Specifies the very short standalone weekday symbols property, a CFArray of CFString objects.
- [kCFDateFormatterQuarterSymbols](cfdateformatterkey/quartersymbols.md) — Specifies the quarter symbols property, a CFArray of CFString objects.
- [kCFDateFormatterShortQuarterSymbols](cfdateformatterkey/shortquartersymbols.md) — Specifies the short quarter symbols property, a CFArray of CFString objects.
- [kCFDateFormatterStandaloneQuarterSymbols](cfdateformatterkey/standalonequartersymbols.md) — Specifies the standalone quarter symbols property, a CFArray of CFString objects.
- [kCFDateFormatterShortStandaloneQuarterSymbols](cfdateformatterkey/shortstandalonequartersymbols.md) — Specifies the short standalone quarter symbols property, a CFArray of CFString objects.
- [kCFDateFormatterGregorianStartDate](cfdateformatterkey/gregorianstartdate.md) — Specifies the Gregorian start date property, a CFDate object.
- [kCFDateFormatterDoesRelativeDateFormattingKey](cfdateformatterkey/doesrelativedateformattingkey.md) — Specifies the relative date formatting property, a CFBoolean object.

## See Also

### Constants

- [Date Formatter Styles](date_formatter_styles.md) — Predefined date and time format styles.
- [Calendar Names](calendar-names.md) — Calendar names used by CFDateFormatter.
