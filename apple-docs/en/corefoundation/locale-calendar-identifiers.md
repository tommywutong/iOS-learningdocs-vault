---
title: Locale Calendar Identifiers
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/locale-calendar-identifiers
source_url: 'https://developer.apple.com/documentation/corefoundation/locale-calendar-identifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/locale-calendar-identifiers.json'
content_hash: 'sha256:3e1e53b8315ff505'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFLocale](cflocale.md)

# Locale Calendar Identifiers

<sub>API Collection</sub>

Predefined locale keys used to get calendar values—values for `kCFLocaleCalendarIdentifier`.

## Overview

Locale objects use key-value pairs to store property values. Use the [CFLocaleGetValue](<cflocalegetvalue(____).md>) function to get the value of a specific property listed above.

## Topics

### Constants

- [kCFGregorianCalendar](cfcalendaridentifier/gregoriancalendar.md) — The name of the calendar currently supported by the [kCFDateFormatterCalendarName](cfdateformatterkey/calendarname.md) property.
- [kCFBuddhistCalendar](cfcalendaridentifier/buddhistcalendar.md) — Specifies the Buddhist calendar.
- [kCFChineseCalendar](cfcalendaridentifier/chinesecalendar.md) — Specifies the Chinese calendar.
- [kCFHebrewCalendar](cfcalendaridentifier/hebrewcalendar.md) — Specifies the Hebrew calendar.
- [kCFIslamicCalendar](cfcalendaridentifier/islamiccalendar.md) — Specifies the Islamic calendar.
- [kCFIslamicCivilCalendar](cfcalendaridentifier/islamiccivilcalendar.md) — Specifies the Islamic tabular calendar with Friday (civil) origin.
- [kCFIslamicTabularCalendar](cfcalendaridentifier/islamictabularcalendar.md) — Specifies the Islamic tabular calendar with Thursday (astronomical) origin.
- [kCFIslamicUmmAlQuraCalendar](cfcalendaridentifier/islamicummalquracalendar.md) — Specifies the Islamic Umm Al Qura calendar.
- [kCFJapaneseCalendar](cfcalendaridentifier/japanesecalendar.md) — Specifies the Japanese calendar.
- [kCFRepublicOfChinaCalendar](cfcalendaridentifier/republicofchinacalendar.md) — Specifies the calendar for the Republic of China.
- [kCFPersianCalendar](cfcalendaridentifier/persiancalendar.md) — Specifies the Persian calendar.
- [kCFIndianCalendar](cfcalendaridentifier/indiancalendar.md) — Specifies the Indian calendar.
- [kCFISO8601Calendar](cfcalendaridentifier/cfiso8601calendar.md) — Specifies the ISO 8601 calendar.

## See Also

### Constants

- [CFLocaleLanguageDirection](cflocalelanguagedirection.md) — These constants describe the text direction for a language. They are returned by the functions [CFLocaleGetLanguageCharacterDirection](<cflocalegetlanguagecharacterdirection(__).md>) and [CFLocaleGetLanguageLineDirection](<cflocalegetlanguagelinedirection(__).md>).
- [Locale Property Keys](locale-property-keys.md) — Predefined locale keys used to get property values.
- [Locale Change Notification](locale-change-notification.md) — Identifier for notification sent if the current locale changes.
