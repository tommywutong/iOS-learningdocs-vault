---
title: 'CFTimeZoneCreateWithTimeIntervalFromGMT(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftimezonecreatewithtimeintervalfromgmt(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonecreatewithtimeintervalfromgmt(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonecreatewithtimeintervalfromgmt%28_%3A_%3A%29.json'
content_hash: 'sha256:706f21da997e9180'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneCreateWithTimeIntervalFromGMT(_:_:)

<sub>Function</sub>

Returns a time zone object for the specified time interval offset from Greenwich Mean Time (GMT).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneCreateWithTimeIntervalFromGMT(_ allocator: CFAllocator!, _ ti: CFTimeInterval) -> CFTimeZone!
```

## Parameters

- `allocator` — The allocator object to use to allocate memory for the new time zone. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `ti` — The offset, from GMT, of the new time zone.

## Return Value

A new time zone whose offset from GMT is given by the interval `ti`. The name of the new time zone is GMT +/- the offset, in hours and minutes. Time zones created with this function never have daylight savings, and the offset is constant no matter what the date. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Time Zone

- [CFTimeZoneCreateWithName](<cftimezonecreatewithname(______).md>) — Returns the time zone object identified by a given name or abbreviation.
- [CFTimeZoneCreate](<cftimezonecreate(______).md>) — Creates a time zone with a given name and data.
