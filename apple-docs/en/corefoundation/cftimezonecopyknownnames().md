---
title: CFTimeZoneCopyKnownNames()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftimezonecopyknownnames()
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezonecopyknownnames()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezonecopyknownnames%28%29.json'
content_hash: 'sha256:107e23acf86da3b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZoneCopyKnownNames()

<sub>Function</sub>

Returns an array of strings containing the names of all the time zones known to the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTimeZoneCopyKnownNames() -> CFArray!
```

## Return Value

An array containing CFString objects representing all the known time zone names. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### System and Default Time Zones and Information

- [CFTimeZoneCopyAbbreviationDictionary](<cftimezonecopyabbreviationdictionary().md>) — Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
- [CFTimeZoneCopyAbbreviation](<cftimezonecopyabbreviation(____).md>) — Returns the abbreviation of a time zone at a specified date.
- [CFTimeZoneCopyDefault](<cftimezonecopydefault().md>) — Returns the default time zone set for your application.
- [CFTimeZoneCopySystem](<cftimezonecopysystem().md>) — Returns the time zone currently used by the system.
- [CFTimeZoneSetDefault](<cftimezonesetdefault(__).md>) — Sets the default time zone for your application the given time zone.
- [CFTimeZoneResetSystem](<cftimezoneresetsystem().md>) — Clears the previously determined system time zone, if any.
- [CFTimeZoneSetAbbreviationDictionary](<cftimezonesetabbreviationdictionary(__).md>) — Sets the abbreviation dictionary to a given dictionary.
