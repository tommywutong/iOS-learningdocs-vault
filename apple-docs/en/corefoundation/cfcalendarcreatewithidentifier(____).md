---
title: 'CFCalendarCreateWithIdentifier(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendarcreatewithidentifier(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendarcreatewithidentifier(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendarcreatewithidentifier%28_%3A_%3A%29.json'
content_hash: 'sha256:9104743f7f607079'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarCreateWithIdentifier(_:_:)

<sub>Function</sub>

Returns a calendar object for the calendar identified by a calendar identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarCreateWithIdentifier(_ allocator: CFAllocator!, _ identifier: CFCalendarIdentifier!) -> CFCalendar!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `identifier` — A calendar identifier. Calendar identifier constants are given in [CFLocale](cflocale.md).

## Return Value

A calendar object for the calendar identified by `ident`. If the identifier is unknown (if, for example, it is either an unrecognized string, or the calendar is not supported by the current version of the operating system), returns `NULL`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Calendar

- [CFCalendarCopyCurrent](<cfcalendarcopycurrent().md>) — Returns a copy of the logical calendar for the current user.
