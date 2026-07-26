---
title: NSDateFormatString
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsdateformatstring
source_url: 'https://developer.apple.com/documentation/foundation/nsdateformatstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdateformatstring.json'
content_hash: 'sha256:833eaa221edb9af0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDateFormatString

<sub>Global Variable</sub>

Key for the format string that specifies how dates are printed using the date format specifiers.

> [!warning] Deprecated
> Use the appropriate API from [DateFormatter](dateformatter.md) instead—see [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i).

<sub>macOS</sub>

```objc
extern NSString * const NSDateFormatString;
```

## Discussion

The default is to use weekday names with full month names and full years, as in “Saturday, March 24, 2001.”

## See Also

### Date & Time Information

- [NSAMPMDesignation](nsampmdesignation.md) — Key for the value that specifies how the morning and afternoon designations are printed, affecting strings that use the `%p` format specifier. _(deprecated)_
- [NSDateTimeOrdering](nsdatetimeordering.md) — Key for the string that specifies how to use ambiguous numbers in date strings. _(deprecated)_
- [NSEarlierTimeDesignations](nsearliertimedesignations.md) — Key for an array of strings that denote a time in the past. _(deprecated)_
- [NSHourNameDesignations](nshournamedesignations.md) — Key for strings that identify the time of day. _(deprecated)_
- [NSLaterTimeDesignations](nslatertimedesignations.md) — Key for an array of strings that denote a time in the future. _(deprecated)_
- [NSMonthNameArray](nsmonthnamearray.md) — Key for the value that specifies the names for the months, affecting strings that use the `%B` format specifier. _(deprecated)_
- [NSNextDayDesignations](nsnextdaydesignations.md) — Key for an array of strings that denote the day after today. _(deprecated)_
- [NSNextNextDayDesignations](nsnextnextdaydesignations.md) — Key for an array of strings that denote the day after tomorrow. _(deprecated)_
- [NSPriorDayDesignations](nspriordaydesignations.md) — Key for an array of strings that denote the day before today. _(deprecated)_
- [NSShortDateFormatString](nsshortdateformatstring.md) — Key for a format string that specifies how dates are abbreviated. _(deprecated)_
- [NSShortWeekDayNameArray](nsshortweekdaynamearray.md) — Key for an array of strings that specify the abbreviations for the days of the week, affecting strings that use the %a format specifier. _(deprecated)_
- [NSShortMonthNameArray](nsshortmonthnamearray.md) — Key for an array of strings that specify the abbreviations for the months, affecting strings that use the `%b` format specifier. _(deprecated)_
- [NSShortTimeDateFormatString](nsshorttimedateformatstring.md) — Key for a format string that specifies how times and dates are abbreviated. _(deprecated)_
- [NSThisDayDesignations](nsthisdaydesignations.md) — Key for an array of strings that specify what this day is called. _(deprecated)_
- [NSTimeDateFormatString](nstimedateformatstring.md) — Key for the value that specifies how dates with times are printed, affecting strings that use the format specifiers `%c`, `%X`, or `%x`. _(deprecated)_
