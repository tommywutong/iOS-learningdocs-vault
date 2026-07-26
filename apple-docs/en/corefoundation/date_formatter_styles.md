---
title: Date Formatter Styles
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/date_formatter_styles
source_url: 'https://developer.apple.com/documentation/corefoundation/date_formatter_styles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/date_formatter_styles.json'
content_hash: 'sha256:7b589ebfb7fbc8d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFDateFormatter](cfdateformatter.md)

# Date Formatter Styles

<sub>API Collection</sub>

Predefined date and time format styles.

## Overview

The format for these date and time styles is not exact because they depend on the locale, user preference settings, and the operating system version. Do not use these constants if you want an exact format, for example if you are parsing an external data file which contains date information in a fixed format. There are several different “lengths” of the formats:

- “long” era names, for example “Anno Domini” instead of “AD”
- “very short” names for months and weekdays; for example, “F” instead of “Friday”
- “standalone” names for months and weekdays (for some locales or languages, a month name displayed in isolation needs to be written differently than a month name within a displayed date)
- names of quarters; for example, “Q2” for a short quarter name

## Topics

### Constants

- [kCFDateFormatterNoStyle](cfdateformatterstyle/nostyle.md) — Specifies no output.
- [kCFDateFormatterShortStyle](cfdateformatterstyle/shortstyle.md) — Specifies a short style, typically numeric only, such as “11/23/37” or “3:30pm”.
- [kCFDateFormatterMediumStyle](cfdateformatterstyle/mediumstyle.md) — Specifies a medium style, typically with abbreviated text, such as “Nov 23, 1937”.
- [kCFDateFormatterLongStyle](cfdateformatterstyle/longstyle.md) — Specifies a long style, typically with full text, such as “November 23, 1937” or “3:30:32pm”.
- [kCFDateFormatterFullStyle](cfdateformatterstyle/fullstyle.md) — Specifies a full style with complete details, such as “Tuesday, April 12, 1952 AD” or “3:30:42pm PST”.

## See Also

### Constants

- [Date Formatter Property Keys](date-formatter-property-keys.md) — Keys used in key-value pairs to discover and specify the value of date formatter properties—used in conjunction with [CFDateFormatterCopyProperty](<cfdateformattercopyproperty(____).md>) and [CFDateFormatterSetProperty](<cfdateformattersetproperty(______).md>).
- [Calendar Names](calendar-names.md) — Calendar names used by CFDateFormatter.
