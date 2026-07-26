---
title: 'CFTimeZoneSetDefault(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftimezonesetdefault(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonesetdefault(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonesetdefault%28_%3A%29.json'
content_hash: 'sha256:a5fe5f0a1d3a5b3e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneSetDefault(_:)

<sub>Function</sub>

Sets the default time zone for your application the given time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneSetDefault(_ tz: CFTimeZone!)
```

## Parameters

- `tz` — The time zone to use as default.

## Discussion

There can be only one default time zone, so by setting a new default time zone, you lose the previous one.

## See Also

### System and Default Time Zones and Information

- [CFTimeZoneCopyAbbreviationDictionary](<cftimezonecopyabbreviationdictionary().md>) — Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
- [CFTimeZoneCopyAbbreviation](<cftimezonecopyabbreviation(____).md>) — Returns the abbreviation of a time zone at a specified date.
- [CFTimeZoneCopyDefault](<cftimezonecopydefault().md>) — Returns the default time zone set for your application.
- [CFTimeZoneCopySystem](<cftimezonecopysystem().md>) — Returns the time zone currently used by the system.
- [CFTimeZoneCopyKnownNames](<cftimezonecopyknownnames().md>) — Returns an array of strings containing the names of all the time zones known to the system.
- [CFTimeZoneResetSystem](<cftimezoneresetsystem().md>) — Clears the previously determined system time zone, if any.
- [CFTimeZoneSetAbbreviationDictionary](<cftimezonesetabbreviationdictionary(__).md>) — Sets the abbreviation dictionary to a given dictionary.
