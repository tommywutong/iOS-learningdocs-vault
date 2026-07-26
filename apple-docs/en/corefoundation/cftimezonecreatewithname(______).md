---
title: 'CFTimeZoneCreateWithName(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftimezonecreatewithname(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonecreatewithname(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonecreatewithname%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d2ba67725a05efa2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneCreateWithName(_:_:_:)

<sub>Function</sub>

Returns the time zone object identified by a given name or abbreviation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneCreateWithName(_ allocator: CFAllocator!, _ name: CFString!, _ tryAbbrev: Bool) -> CFTimeZone!
```

## Parameters

- `allocator` — The allocator object to use to allocate memory for the new time zone. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `name` — The name or abbreviation of the time zone to obtain. The name may be in any of the formats understood by the system, for example “EST”, “Etc/GMT-2”, “America/Argentina/Buenos_Aires”, “Europe/Monaco”, “US/Pacific”, or “posixrules”. For a complete list of system names, you can see the output of  [CFTimeZoneCopyKnownNames](<cftimezonecopyknownnames().md>).

- `tryAbbrev` — If `false`, assumes `name` is not an abbreviation and searches the time zone information directory for a matching name. If `true`, tries to resolve `name` using the abbreviation dictionary first before searching the information dictionary.

## Return Value

A time zone corresponding to `name`, or `NULL` if no match was found. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Time Zone

- [CFTimeZoneCreateWithTimeIntervalFromGMT](<cftimezonecreatewithtimeintervalfromgmt(____).md>) — Returns a time zone object for the specified time interval offset from Greenwich Mean Time (GMT).
- [CFTimeZoneCreate](<cftimezonecreate(______).md>) — Creates a time zone with a given name and data.
