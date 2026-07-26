---
title: 'CFCalendarGetIdentifier(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcalendargetidentifier(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendargetidentifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendargetidentifier%28_%3A%29.json'
content_hash: 'sha256:b7b7c05bf7081f47'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarGetIdentifier(_:)

<sub>Function</sub>

Returns the given calendar’s identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCalendarGetIdentifier(_ calendar: CFCalendar!) -> CFCalendarIdentifier!
```

## Parameters

- `calendar` — The calendar to examine.

## Return Value

A string representation of `calendar`’s identifier. Calendar identifier constants can be found in [CFLocale](cflocale.md). Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).
