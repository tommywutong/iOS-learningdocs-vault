---
title: TimeZone
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/timezone
source_url: 'https://developer.apple.com/documentation/foundation/timezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timezone.json'
content_hash: 'sha256:550eea4e62a9b5c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# TimeZone

<sub>Structure</sub>

Information about standard time conventions associated with a specific geopolitical region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TimeZone
```

## Overview

`TimeZone` defines the behavior of a time zone. Time zone values represent geopolitical regions. Consequently, these values have names for these regions. Time zone values also represent a temporal offset, either plus or minus, from Greenwich Mean Time (GMT) and an abbreviation (such as PST for Pacific Standard Time).

`TimeZone` provides two static functions to get time zone values: `current` and `autoupdatingCurrent`. The `autoupdatingCurrent` time zone automatically tracks updates made by the user.

Note that time zone database entries such as “America/Los_Angeles” are IDs, not names. An example of a time zone name is “Pacific Daylight Time”. Although many `TimeZone` functions include the word “name”, they refer to IDs.

Cocoa does not provide any API to change the time zone of the computer, or of other applications.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the Current Time Zone

- [autoupdatingCurrent](timezone/autoupdatingcurrent.md) — The time zone currently used by the system, automatically updating to the user’s current preference.
- [current](timezone/current.md) — The time zone currently used by the system.

### Creating a Time Zone

- [init(secondsFromGMT:)](<timezone/init(secondsfromgmt_).md>) — Returns a time zone initialized with a specific number of seconds from GMT.
- [knownTimeZoneIdentifiers](timezone/knowntimezoneidentifiers.md) — Returns an array of strings listing the identifier of all the time zones known to the system.
- [abbreviationDictionary](timezone/abbreviationdictionary.md) — Returns the mapping of abbreviations to time zone identifiers.

### Getting Time Zone Information

- [identifier](timezone/identifier.md) — The geopolitical region identifier that identifies the time zone.
- [abbreviation(for:)](<timezone/abbreviation(for_).md>) — Returns the abbreviation for the time zone at a given date.
- [secondsFromGMT(for:)](<timezone/secondsfromgmt(for_).md>) — The current difference in seconds between the time zone and Greenwich Mean Time.
- [timeZoneDataVersion](timezone/timezonedataversion.md) — Returns the time zone data version.

### Working with Daylight Savings

- [isDaylightSavingTime(for:)](<timezone/isdaylightsavingtime(for_).md>) — Returns a Boolean value that indicates whether the receiver uses daylight saving time at a given date.
- [daylightSavingTimeOffset(for:)](<timezone/daylightsavingtimeoffset(for_).md>) — Returns the daylight saving time offset for a given date.
- [nextDaylightSavingTimeTransition](timezone/nextdaylightsavingtimetransition.md) — The date of the next (after the current instant) daylight saving time transition for the time zone.
- [nextDaylightSavingTimeTransition(after:)](<timezone/nextdaylightsavingtimetransition(after_).md>) — Returns the next daylight saving time transition after a given date.

### Describing Time Zones

- [localizedName(for:locale:)](<timezone/localizedname(for_locale_).md>) — Returns the name of the receiver localized for a given locale.

### Working with notification messages

- [SystemTimeZoneDidChangeMessage](timezone/systemtimezonedidchangemessage.md) — A message the system sends when the system time zone changes.

### Using Reference Types

- [NSTimeZone](nstimezone.md) — Information about standard time conventions associated with a specific geopolitical region.

### Initializers

- [init(abbreviation:)](<timezone/init(abbreviation_).md>) — Returns a time zone identified by a given abbreviation.
- [init(identifier:)](<timezone/init(identifier_).md>) — Returns a time zone initialized with a given identifier.

### Type Aliases

- [NameStyle](timezone/namestyle.md)

### Type Properties

- [gmt](timezone/gmt.md)

## See Also

### Calendrical Calculations

- [DateComponents](datecomponents.md) — A date or time specified in terms of units (such as year, month, day, hour, and minute) to be evaluated in a calendar system and time zone.
- [Calendar](calendar.md) — A definition of the relationships between calendar units and absolute points in time, providing features for calculation and comparison of dates.
