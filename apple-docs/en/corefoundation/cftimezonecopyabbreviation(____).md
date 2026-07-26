---
title: 'CFTimeZoneCopyAbbreviation(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftimezonecopyabbreviation(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonecopyabbreviation(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonecopyabbreviation%28_%3A_%3A%29.json'
content_hash: 'sha256:fe1a0138c820a481'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneCopyAbbreviation(_:_:)

<sub>Function</sub>

Returns the abbreviation of a time zone at a specified date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneCopyAbbreviation(_ tz: CFTimeZone!, _ at: CFAbsoluteTime) -> CFString!
```

## Parameters

- `tz` — The time zone to use.

- `at` — The absolute time at which to obtain the abbreviation.

## Return Value

A string containing the time zone abbreviation of `at`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Note that the abbreviation may be different at different dates. For example, during daylight savings time the US/Eastern time zone has an abbreviation of “EDT.” At other times, its abbreviation is “EST.”

## See Also

### System and Default Time Zones and Information

- [CFTimeZoneCopyAbbreviationDictionary](<cftimezonecopyabbreviationdictionary().md>) — Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
- [CFTimeZoneCopyDefault](<cftimezonecopydefault().md>) — Returns the default time zone set for your application.
- [CFTimeZoneCopySystem](<cftimezonecopysystem().md>) — Returns the time zone currently used by the system.
- [CFTimeZoneSetDefault](<cftimezonesetdefault(__).md>) — Sets the default time zone for your application the given time zone.
- [CFTimeZoneCopyKnownNames](<cftimezonecopyknownnames().md>) — Returns an array of strings containing the names of all the time zones known to the system.
- [CFTimeZoneResetSystem](<cftimezoneresetsystem().md>) — Clears the previously determined system time zone, if any.
- [CFTimeZoneSetAbbreviationDictionary](<cftimezonesetabbreviationdictionary(__).md>) — Sets the abbreviation dictionary to a given dictionary.
