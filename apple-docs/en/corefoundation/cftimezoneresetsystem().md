---
title: CFTimeZoneResetSystem()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftimezoneresetsystem()
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezoneresetsystem()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezoneresetsystem%28%29.json'
content_hash: 'sha256:ce733fa3c402cfba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneResetSystem()

<sub>Function</sub>

Clears the previously determined system time zone, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneResetSystem()
```

## Discussion

If the default time zone is set to the same value as the system time zone or has not been explicitly set, this function clears it as well.

Subsequent calls to [CFTimeZoneCopySystem](<cftimezonecopysystem().md>) will attempt to re-determine the system time zone.

## See Also

### System and Default Time Zones and Information

- [CFTimeZoneCopyAbbreviationDictionary](<cftimezonecopyabbreviationdictionary().md>) — Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
- [CFTimeZoneCopyAbbreviation](<cftimezonecopyabbreviation(____).md>) — Returns the abbreviation of a time zone at a specified date.
- [CFTimeZoneCopyDefault](<cftimezonecopydefault().md>) — Returns the default time zone set for your application.
- [CFTimeZoneCopySystem](<cftimezonecopysystem().md>) — Returns the time zone currently used by the system.
- [CFTimeZoneSetDefault](<cftimezonesetdefault(__).md>) — Sets the default time zone for your application the given time zone.
- [CFTimeZoneCopyKnownNames](<cftimezonecopyknownnames().md>) — Returns an array of strings containing the names of all the time zones known to the system.
- [CFTimeZoneSetAbbreviationDictionary](<cftimezonesetabbreviationdictionary(__).md>) — Sets the abbreviation dictionary to a given dictionary.
