---
title: 'CFTimeZoneSetAbbreviationDictionary(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftimezonesetabbreviationdictionary(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonesetabbreviationdictionary(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonesetabbreviationdictionary%28_%3A%29.json'
content_hash: 'sha256:1e02ac196ac18c63'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneSetAbbreviationDictionary(_:)

<sub>Function</sub>

Sets the abbreviation dictionary to a given dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneSetAbbreviationDictionary(_ dict: CFDictionary!)
```

## Parameters

- `dict` — A dictionary containing key-value pairs for looking up time zone names given their abbreviations. The keys should be CFString objects containing the abbreviations; the values should be CFString objects containing their corresponding geopolitical region names.

## See Also

### System and Default Time Zones and Information

- [CFTimeZoneCopyAbbreviationDictionary](<cftimezonecopyabbreviationdictionary().md>) — Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
- [CFTimeZoneCopyAbbreviation](<cftimezonecopyabbreviation(____).md>) — Returns the abbreviation of a time zone at a specified date.
- [CFTimeZoneCopyDefault](<cftimezonecopydefault().md>) — Returns the default time zone set for your application.
- [CFTimeZoneCopySystem](<cftimezonecopysystem().md>) — Returns the time zone currently used by the system.
- [CFTimeZoneSetDefault](<cftimezonesetdefault(__).md>) — Sets the default time zone for your application the given time zone.
- [CFTimeZoneCopyKnownNames](<cftimezonecopyknownnames().md>) — Returns an array of strings containing the names of all the time zones known to the system.
- [CFTimeZoneResetSystem](<cftimezoneresetsystem().md>) — Clears the previously determined system time zone, if any.
