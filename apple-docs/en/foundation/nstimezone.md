---
title: NSTimeZone
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone.json'
content_hash: 'sha256:1beda9811946b348'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSTimeZone

<sub>Class</sub>

Information about standard time conventions associated with a specific geopolitical region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSTimeZone
```

## Overview

In Swift, this type bridges to [TimeZone](timezone.md); use [NSTimeZone](nstimezone.md) when you need reference semantics or other Foundation-specific behavior.

Time zones represent the standard time policies for a geopolitical region. Time zones have identifiers like “America/Los_Angeles” and can also be identified by abbreviations, such as PST for Pacific Standard Time. You can create time zone objects by ID with [- initWithName:](<nstimezone/init(name_).md>) and by abbreviation with [+ timeZoneWithAbbreviation:](<nstimezone/init(abbreviation_).md>).

> [!note] Note
> Time zone database entries such as “America/Los_Angeles” are IDs, not names. An example of a time zone name is “Pacific Daylight Time”. Although many [NSTimeZone](nstimezone.md) symbols include the word “name”, they actually refer to IDs.

Time zones can also represent a temporal offset—either plus or minus—from Greenwich Mean Time (GMT). For example, the temporal offset of Pacific Standard Time is 8 hours behind Greenwich Mean Time (GMT-8). You can create time zone objects with a temporal offset by using [+ timeZoneForSecondsFromGMT:](<nstimezone/init(forsecondsfromgmt_).md>).

You typically work with system time zones rather than creating time zones by identifier or by offset. The [systemTimeZone](nstimezone/system.md) class property returns the time zone currently used by the system, if known. This value is cached once the property is accessed and doesn’t reflect any system time zone changes until you call the [+ resetSystemTimeZone](<nstimezone/resetsystemtimezone().md>) method. The [localTimeZone](nstimezone/local.md) class property returns an autoupdating proxy object that always returns the current time zone used by the system. You can also set the [defaultTimeZone](nstimezone/default.md) class property to make your app run as if it were in a different time zone than the system.

> [!tip] Tip
> You can’t use [NSTimeZone](nstimezone.md) APIs to change the time zone of the device or of other apps.

[NSTimeZone](nstimezone.md) is _toll-free bridged_ with its Core Foundation counterpart, [CFTimeZone](../corefoundation/cftimezone.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [TimeZone](timezone.md) structure, which bridges to the [NSTimeZone](nstimezone.md) class. For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Working with System Time Zones

- [localTimeZone](nstimezone/local.md) — An object that tracks the current system time zone.
- [systemTimeZone](nstimezone/system.md) — The time zone currently used by the system.
- [+ resetSystemTimeZone](<nstimezone/resetsystemtimezone().md>) — Clears any time zone value cached for the [systemTimeZone](nstimezone/system.md) property.
- [defaultTimeZone](nstimezone/default.md) — The default time zone for the current app.

### Creating Time Zones

- [- initWithName:](<nstimezone/init(name_).md>) — Returns a time zone initialized with a given identifier.
- [- initWithName:data:](<nstimezone/init(name_data_).md>) — Initializes a time zone with a given identifier and time zone data.
- [+ timeZoneWithAbbreviation:](<nstimezone/init(abbreviation_).md>) — Returns the time zone object identified by a given abbreviation.
- [+ timeZoneForSecondsFromGMT:](<nstimezone/init(forsecondsfromgmt_).md>) — Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.
- [knownTimeZoneNames](nstimezone/knowntimezonenames.md) — Returns an array of strings listing the IDs of all the time zones known to the system.
- [abbreviationDictionary](nstimezone/abbreviationdictionary.md) — Returns a dictionary holding the mappings of time zone abbreviations to time zone names.

### Getting Time Zone Information

- [name](nstimezone/name.md) — The geopolitical region ID that identifies the receiver.
- [abbreviation](nstimezone/abbreviation.md) — The abbreviation for the receiver, such as “EDT” (Eastern Daylight Time).
- [- abbreviationForDate:](<nstimezone/abbreviation(for_).md>) — Returns the abbreviation for the receiver at a given date.
- [secondsFromGMT](nstimezone/secondsfromgmt.md) — The current difference in seconds between the receiver and Greenwich Mean Time.
- [- secondsFromGMTForDate:](<nstimezone/secondsfromgmt(for_).md>) — Returns the difference in seconds between the receiver and Greenwich Mean Time at a given date.
- [data](nstimezone/data.md) — The data that stores the information used by the receiver.
- [timeZoneDataVersion](nstimezone/timezonedataversion.md) — Returns the time zone data version.
- [NameStyle](nstimezone/namestyle.md) — Constants you use to specify a style when presenting time zone names.

### Working with Daylight Savings

- [daylightSavingTime](nstimezone/isdaylightsavingtime.md) — A Boolean value that indicates whether the receiver is currently using daylight saving time.
- [- isDaylightSavingTimeForDate:](<nstimezone/isdaylightsavingtime(for_).md>) — Indicates whether the receiver uses daylight saving time on a given date.
- [daylightSavingTimeOffset](nstimezone/daylightsavingtimeoffset.md) — The current daylight saving time offset of the receiver.
- [- daylightSavingTimeOffsetForDate:](<nstimezone/daylightsavingtimeoffset(for_).md>) — Returns the daylight saving time offset for a given date.
- [nextDaylightSavingTimeTransition](nstimezone/nextdaylightsavingtimetransition.md) — The date of the next daylight saving time transition for the receiver.
- [- nextDaylightSavingTimeTransitionAfterDate:](<nstimezone/nextdaylightsavingtimetransition(after_).md>) — Returns the next daylight saving time transition after a given date.

### Comparing Time Zones

- [- isEqualToTimeZone:](<nstimezone/isequal(to_).md>) — Indicates whether the receiver has the same name and data as the specified time zone.

### Describing Time Zones

- [- localizedName:locale:](<nstimezone/localizedname(__locale_).md>) — Returns the localized name of the time zone.
- [description](nstimezone/description.md) — A textual description of the time zone including the name, abbreviation, offset from GMT, and whether or not daylight saving time is currently in effect.

### Recognizing Notifications

- [NSSystemTimeZoneDidChangeNotification](nsnotification/name-swift.struct/nssystemtimezonedidchange.md) — A notification posted when the time zone changes.

### Initializers

- [init(coder:)](<nstimezone/init(coder_).md>)
