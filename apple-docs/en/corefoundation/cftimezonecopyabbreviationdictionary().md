---
title: CFTimeZoneCopyAbbreviationDictionary()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftimezonecopyabbreviationdictionary()
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonecopyabbreviationdictionary()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonecopyabbreviationdictionary%28%29.json'
content_hash: 'sha256:6eec7b8b824bcc14'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneCopyAbbreviationDictionary()

<sub>Function</sub>

Returns a dictionary holding the mappings of time zone abbreviations to time zone names.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneCopyAbbreviationDictionary() -> CFDictionary!
```

## Return Value

A dictionary containing the mappings of time zone abbreviations to time zone names. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

More than one time zone may have the same abbreviation. For example, US/Pacific and Canada/Pacific both use the abbreviation “PST.” In these cases this function chooses a single name to map the abbreviation to.

## See Also

### System and Default Time Zones and Information

- [CFTimeZoneCopyAbbreviation](<cftimezonecopyabbreviation(____).md>) — Returns the abbreviation of a time zone at a specified date.
- [CFTimeZoneCopyDefault](<cftimezonecopydefault().md>) — Returns the default time zone set for your application.
- [CFTimeZoneCopySystem](<cftimezonecopysystem().md>) — Returns the time zone currently used by the system.
- [CFTimeZoneSetDefault](<cftimezonesetdefault(__).md>) — Sets the default time zone for your application the given time zone.
- [CFTimeZoneCopyKnownNames](<cftimezonecopyknownnames().md>) — Returns an array of strings containing the names of all the time zones known to the system.
- [CFTimeZoneResetSystem](<cftimezoneresetsystem().md>) — Clears the previously determined system time zone, if any.
- [CFTimeZoneSetAbbreviationDictionary](<cftimezonesetabbreviationdictionary(__).md>) — Sets the abbreviation dictionary to a given dictionary.
