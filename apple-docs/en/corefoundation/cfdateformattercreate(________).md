---
title: 'CFDateFormatterCreate(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdateformattercreate(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdateformattercreate(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdateformattercreate%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ccabd46f98e029e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateFormatterCreate(_:_:_:_:)

<sub>Function</sub>

Creates a new CFDateFormatter object, localized to the given locale, which will format dates to the given date and time styles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateFormatterCreate(_ allocator: CFAllocator!, _ locale: CFLocale!, _ dateStyle: CFDateFormatterStyle, _ timeStyle: CFDateFormatterStyle) -> CFDateFormatter!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `locale` — The locale to use for localization. If `NULL` uses the default system local. Use [CFLocaleCopyCurrent](<cflocalecopycurrent().md>) to specify the locale of the current user.

- `dateStyle` — The date style to use when formatting dates. See [Date Formatter Styles](date_formatter_styles.md) for possible values.

- `timeStyle` — The time style to use when formatting times. See [Date Formatter Styles](date_formatter_styles.md) for possible values.

## Return Value

A new date formatter, localized to the given locale, which will format dates to the given date and time styles. Returns `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

You can use `kCFDateFormatterNoStyle` to suppress output for the date or time. The following code fragment illustrates the creation and use of a date formatter that only outputs the date information (memory management is omitted for clarity).

```objc
CFLocaleRef locale = CFLocaleCreate(kCFAllocatorDefault, CFSTR("en_GB"));
 
CFDateFormatterRef formatter = CFDateFormatterCreate(
        kCFAllocatorDefault, locale, kCFDateFormatterMediumStyle, kCFDateFormatterNoStyle);
 
CFDateRef date = CFDateCreate(kCFAllocatorDefault, 123456);
CFStringRef dateAsString = CFDateFormatterCreateStringWithDate (
        kCFAllocatorDefault, formatter, date);
 
CFShow(dateAsString);
// outputs "2 Jan 2001"
```
