---
title: NSShortWeekDayNameArray
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsshortweekdaynamearray
source_url: 'https://developer.apple.com/documentation/foundation/nsshortweekdaynamearray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsshortweekdaynamearray.json'
content_hash: 'sha256:775c84b309ccd8b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSShortWeekDayNameArray

<sub>Global Variable</sub>

Key for an array of strings that specify the abbreviations for the days of the week, affecting strings that use the %a format specifier.

> [!warning] Deprecated
> Use [shortWeekdaySymbols](dateformatter/shortweekdaysymbols.md) or—if you are going to display these in the user interface by themselves—[shortStandaloneWeekdaySymbols](dateformatter/shortstandaloneweekdaysymbols.md) (`NSDateFormatter`) instead.

<sub>macOS</sub>

```objc
extern NSString * const NSShortWeekDayNameArray;
```

## Discussion

Sunday should be the first day of the week.

## See Also

### Date & Time Information

- [NSAMPMDesignation](nsampmdesignation.md) — Key for the value that specifies how the morning and afternoon designations are printed, affecting strings that use the `%p` format specifier. _(deprecated)_
- [NSDateFormatString](nsdateformatstring.md) — Key for the format string that specifies how dates are printed using the date format specifiers. _(deprecated)_
- [NSDateTimeOrdering](nsdatetimeordering.md) — Key for the string that specifies how to use ambiguous numbers in date strings. _(deprecated)_
- [NSEarlierTimeDesignations](nsearliertimedesignations.md) — Key for an array of strings that denote a time in the past. _(deprecated)_
- [NSHourNameDesignations](nshournamedesignations.md) — Key for strings that identify the time of day. _(deprecated)_
- [NSLaterTimeDesignations](nslatertimedesignations.md) — Key for an array of strings that denote a time in the future. _(deprecated)_
- [NSMonthNameArray](nsmonthnamearray.md) — Key for the value that specifies the names for the months, affecting strings that use the `%B` format specifier. _(deprecated)_
- [NSNextDayDesignations](nsnextdaydesignations.md) — Key for an array of strings that denote the day after today. _(deprecated)_
- [NSNextNextDayDesignations](nsnextnextdaydesignations.md) — Key for an array of strings that denote the day after tomorrow. _(deprecated)_
- [NSPriorDayDesignations](nspriordaydesignations.md) — Key for an array of strings that denote the day before today. _(deprecated)_
- [NSShortDateFormatString](nsshortdateformatstring.md) — Key for a format string that specifies how dates are abbreviated. _(deprecated)_
- [NSShortMonthNameArray](nsshortmonthnamearray.md) — Key for an array of strings that specify the abbreviations for the months, affecting strings that use the `%b` format specifier. _(deprecated)_
- [NSShortTimeDateFormatString](nsshorttimedateformatstring.md) — Key for a format string that specifies how times and dates are abbreviated. _(deprecated)_
- [NSThisDayDesignations](nsthisdaydesignations.md) — Key for an array of strings that specify what this day is called. _(deprecated)_
- [NSTimeDateFormatString](nstimedateformatstring.md) — Key for the value that specifies how dates with times are printed, affecting strings that use the format specifiers `%c`, `%X`, or `%x`. _(deprecated)_
