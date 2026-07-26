---
title: CFCalendarCopyCurrent()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfcalendarcopycurrent()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendarcopycurrent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendarcopycurrent%28%29.json'
content_hash: 'sha256:3b7a7cf907a80af8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarCopyCurrent()

<sub>Function</sub>

Returns a copy of the logical calendar for the current user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarCopyCurrent() -> CFCalendar!
```

## Return Value

The logical calendar for the current user that is formed from the settings for the current user’s chosen system locale overlaid with any custom settings the user has specified in System Preferences. This function may return a retained cached object, not a new object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Settings you get from this calendar do not change if user defaults change so that your operations are consistent.

Typically you perform some operations on the returned object and then release it. The returned object may be cached, so you do not need to hold on to it indefinitely.

## See Also

### Creating a Calendar

- [CFCalendarCreateWithIdentifier](<cfcalendarcreatewithidentifier(____).md>) — Returns a calendar object for the calendar identified by a calendar identifier.
