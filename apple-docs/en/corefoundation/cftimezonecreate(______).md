---
title: 'CFTimeZoneCreate(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftimezonecreate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonecreate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonecreate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:96c5efac8b377b3c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneCreate(_:_:_:)

<sub>Function</sub>

Creates a time zone with a given name and data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneCreate(_ allocator: CFAllocator!, _ name: CFString!, _ data: CFData!) -> CFTimeZone!
```

## Parameters

- `allocator` — The allocator object to use to allocate memory for the new time zone. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `name` — The name of the time zone to create.

- `data` — The data to use to initialize the time zone. The contents of the data should be the same as that found within the time-zone files located at `/usr/share/zoneinfo`.

## Return Value

A time zone corresponding to `name` and `data`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

You typically do not call this function directly. Use the [CFTimeZoneCreateWithName](<cftimezonecreatewithname(______).md>) function to obtain a time zone given its name.

## See Also

### Creating a Time Zone

- [CFTimeZoneCreateWithName](<cftimezonecreatewithname(______).md>) — Returns the time zone object identified by a given name or abbreviation.
- [CFTimeZoneCreateWithTimeIntervalFromGMT](<cftimezonecreatewithtimeintervalfromgmt(____).md>) — Returns a time zone object for the specified time interval offset from Greenwich Mean Time (GMT).
