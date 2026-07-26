---
title: CFTimeZone
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftimezone
source_url: 'https://developer.apple.com/documentation/corefoundation/cftimezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftimezone.json'
content_hash: 'sha256:dfc3e3e0a7eb20fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTimeZone

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFTimeZone
```

## Overview

CFTimeZone defines the behavior of time zone objects. Time zone objects represent geopolitical regions. Consequently, these objects have names for these regions. Time zone objects also represent a temporal offset, either plus or minus, from Greenwich Mean Time (GMT) and an abbreviation (such as PST for Pacific Standard Time).

CFTimeZone provides several functions to create time zone objects: [CFTimeZoneCreateWithName](<cftimezonecreatewithname(______).md>) and [CFTimeZoneCreateWithTimeIntervalFromGMT](<cftimezonecreatewithtimeintervalfromgmt(____).md>). CFTimeZone also permits you to set the default time zone within your application using the [CFTimeZoneSetDefault](<cftimezonesetdefault(__).md>) function. You can access this default time zone at any time with the [CFTimeZoneCopyDefault](<cftimezonecopydefault().md>) function.

CFTimeZone is “toll-free bridged” with its Cocoa Foundation counterpart, [NSTimeZone](../foundation/nstimezone.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSTimeZone *` parameter, you can pass in a `CFTimeZoneRef`, and in a function where you see a `CFTimeZoneRef` parameter, you can pass in an NSTimeZone instance. This fact also applies to concrete subclasses of NSTimeZone. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Time Zone

- [CFTimeZoneCreateWithName](<cftimezonecreatewithname(______).md>) — Returns the time zone object identified by a given name or abbreviation.
- [CFTimeZoneCreateWithTimeIntervalFromGMT](<cftimezonecreatewithtimeintervalfromgmt(____).md>) — Returns a time zone object for the specified time interval offset from Greenwich Mean Time (GMT).
- [CFTimeZoneCreate](<cftimezonecreate(______).md>) — Creates a time zone with a given name and data.

### System and Default Time Zones and Information

- [CFTimeZoneCopyAbbreviationDictionary](<cftimezonecopyabbreviationdictionary().md>) — Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
- [CFTimeZoneCopyAbbreviation](<cftimezonecopyabbreviation(____).md>) — Returns the abbreviation of a time zone at a specified date.
- [CFTimeZoneCopyDefault](<cftimezonecopydefault().md>) — Returns the default time zone set for your application.
- [CFTimeZoneCopySystem](<cftimezonecopysystem().md>) — Returns the time zone currently used by the system.
- [CFTimeZoneSetDefault](<cftimezonesetdefault(__).md>) — Sets the default time zone for your application the given time zone.
- [CFTimeZoneCopyKnownNames](<cftimezonecopyknownnames().md>) — Returns an array of strings containing the names of all the time zones known to the system.
- [CFTimeZoneResetSystem](<cftimezoneresetsystem().md>) — Clears the previously determined system time zone, if any.
- [CFTimeZoneSetAbbreviationDictionary](<cftimezonesetabbreviationdictionary(__).md>) — Sets the abbreviation dictionary to a given dictionary.

### Getting Information About Time Zones

- [CFTimeZoneGetName](<cftimezonegetname(__).md>) — Returns the geopolitical region name that identifies a given time zone.
- [CFTimeZoneCopyLocalizedName](<cftimezonecopylocalizedname(______).md>) — Returns the localized name of a given time zone.
- [CFTimeZoneGetSecondsFromGMT](<cftimezonegetsecondsfromgmt(____).md>) — Returns the difference in seconds between the receiver and Greenwich Mean Time (GMT) at the specified date.
- [CFTimeZoneGetData](<cftimezonegetdata(__).md>) — Returns the data that stores the information used by a time zone.

### Getting Daylight Savings Time Information

- [CFTimeZoneIsDaylightSavingTime](<cftimezoneisdaylightsavingtime(____).md>) — Returns whether or not a time zone is in daylight savings time at a specified date.
- [CFTimeZoneGetDaylightSavingTimeOffset](<cftimezonegetdaylightsavingtimeoffset(____).md>) — Returns the daylight saving time offset for a time zone at a given time.
- [CFTimeZoneGetNextDaylightSavingTimeTransition](<cftimezonegetnextdaylightsavingtimetransition(____).md>) — Returns the time in a given time zone of the next daylight saving time transition after a given time.

### Getting the CFTimeZone Type ID

- [CFTimeZoneGetTypeID](<cftimezonegettypeid().md>) — Returns the type identifier for the CFTimeZone opaque type.

### Data Types

- [CFTimeZoneNameStyle](cftimezonenamestyle.md) — Index type for constants used to specify styles of time zone names.

### Constants

- [Notification Name](notification-name.md) — Name of the notification posted when the time zone changes.
- [Time Zone Name Styles](time_zone_name_styles.md) — Constants to specify styles for time zone names.

## See Also

### Related Documentation

- [Date and Time Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDatesAndTimes/CFDatesAndTimes.html#//apple_ref/doc/uid/10000125i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
