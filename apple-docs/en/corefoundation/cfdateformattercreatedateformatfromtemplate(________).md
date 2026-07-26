---
title: 'CFDateFormatterCreateDateFormatFromTemplate(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdateformattercreatedateformatfromtemplate(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdateformattercreatedateformatfromtemplate(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdateformattercreatedateformatfromtemplate%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:3ce79dd468195a5e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateFormatterCreateDateFormatFromTemplate(_:_:_:_:)

<sub>Function</sub>

Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateFormatterCreateDateFormatFromTemplate(_ allocator: CFAllocator!, _ tmplate: CFString!, _ options: CFOptionFlags, _ locale: CFLocale!) -> CFString!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `tmplate` — A string containing date format patterns (such as “MM” or “h”). For full details, see [Unicode Technical Standard #35](http://www.unicode.org/reports/tr35/tr35-31/tr35-dates.html#Date_Format_Patterns).

- `options` — No options are currently defined—pass `0`.

- `locale` — The locale for which the template is required.

## Return Value

A localized date format string representing the date format components given in `template`, arranged appropriately for the locale specified by `locale`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The returned string may not contain exactly those components given in `template`, but may—for example—have locale-specific adjustments applied.

## Discussion

Different locales have different conventions for the ordering of date components. You use this method to get an appropriate format string for a given set of components for a specified locale (typically you use the current locale—see [CFLocaleCopyCurrent](<cflocalecopycurrent().md>)).

The following example shows the difference between the date formats for British and American English:

```objc
CFStringRef dateComponents = CFSTR("yMMMMd");
 
CFLocaleRef usLocale = CFLocaleCreate(NULL, CFSTR("en_US"));
CFStringRef usDateFormatString =
    CFDateFormatterCreateDateFormatFromTemplate(NULL, dateComponents, 0, usLocale);
// Date format for English (United States): MMMM d, y
 
CFLocaleRef gbLocale = CFLocaleCreate(NULL, CFSTR("en_GB"));
CFStringRef gbDateFormatString =
    CFDateFormatterCreateDateFormatFromTemplate(NULL, dateComponents, 0, gbLocale);
// Date format for English (United Kingdom): d MMMM y
```

## See Also

### Creating Strings From Data

- [CFDateFormatterCreateStringWithAbsoluteTime](<cfdateformattercreatestringwithabsolutetime(______).md>) — Returns a string representation of the given absolute time using the specified date formatter.
- [CFDateFormatterCreateStringWithDate](<cfdateformattercreatestringwithdate(______).md>) — Returns a string representation of the given date using the specified date formatter.
