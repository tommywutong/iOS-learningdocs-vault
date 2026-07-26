---
title: NSDate
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdate
source_url: 'https://developer.apple.com/documentation/foundation/nsdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate.json'
content_hash: 'sha256:56f853e7e9727aa8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDate

<sub>Class</sub>

A representation of a specific point in time, independent of any calendar or time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSDate
```

## Overview

In Swift, use this type when you need reference semantics or other Foundation-specific behavior.

[NSDate](nsdate.md) objects encapsulate a single point in time, independent of any particular calendrical system or time zone. Date objects are immutable, representing an invariant time interval relative to an absolute reference date (00:00:00 UTC on 1 January 2001).

The [NSDate](nsdate.md) class provides methods for comparing dates, calculating the time interval between two dates, and creating a new date from a time interval relative to another date. [NSDate](nsdate.md) objects can be used in conjunction with [DateFormatter](dateformatter.md) objects to create localized representations of dates and times, as well as with [NSCalendar](nscalendar.md) objects to perform calendar arithmetic.

[NSDate](nsdate.md) is _toll-free bridged_ with its Core Foundation counterpart, [CFDate](../corefoundation/cfdate.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [Date](date.md) structure, which bridges to the [NSDate](nsdate.md) class. For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

### Subclassing Notes

You might subclass [NSDate](nsdate.md) in order to make it easier to work with a particular calendrical system, or to work with date and time values with a finer temporal granularity.

#### Methods to Override and Other Requirements

If you want to subclass [NSDate](nsdate.md) to obtain behavior different than that provided by the private or public subclasses, you must:

- Declare a suitable instance variable to hold the date and time value (relative to an absolute reference date)
- Override the [timeIntervalSinceReferenceDate](nsdate/timeintervalsincereferencedate-swift.property.md) instance method to provide the correct date and time value based on your instance variable
- Override [- initWithTimeIntervalSinceReferenceDate:](<nsdate/init(timeintervalsincereferencedate_).md>), one of the designated initializer methods
- If creating a subclass that represents a calendrical system, define methods that partition past and future periods into the units of this calendar
- Implement the methods required by the [NSCopying](nscopying.md) and [NSCoding](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WritingSwiftClassesWithObjective-CBehavior.html#//apple_ref/doc/uid/TP40014216-CH5-ID152) protocols, because [NSDate](nsdate.md) adopts these protocols

#### Special Considerations

Your subclass may use a different reference date than the absolute reference date used by [NSDate](nsdate.md) (00:00:00 UTC on 1 January 2001). If it does, it must still use the absolute reference date in its implementations of the methods [timeIntervalSinceReferenceDate](nsdate/timeintervalsincereferencedate-swift.property.md) and [- initWithTimeIntervalSinceReferenceDate:](<nsdate/init(timeintervalsincereferencedate_).md>). That is, the reference date referred to in the titles of these methods is the absolute reference date. If you do not use the absolute reference date in these methods, comparisons between [NSDate](nsdate.md) objects of your subclass and `NSDate` objects of a private subclass will not work.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CKRecordValue](../cloudkit/ckrecordvalue-c.protocol.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a Date

- [- init](<nsdate/init().md>) — Returns a date object initialized to the current date and time.
- [- initWithTimeIntervalSinceNow:](<nsdate/init(timeintervalsincenow_).md>) — Returns a date object initialized relative to the current date and time by a given number of seconds.
- [- initWithTimeIntervalSinceReferenceDate:](<nsdate/init(timeintervalsincereferencedate_).md>) — Returns a date object initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [- initWithTimeIntervalSince1970:](<nsdate/init(timeintervalsince1970_).md>) — Returns a date object initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.
- [- initWithCoder:](<nsdate/init(coder_).md>) — Returns a date object initialized from data in the given unarchiver.

### Getting Temporal Boundaries

- [distantFuture](nsdate/distantfuture.md) — A date object representing a date in the distant future.
- [distantPast](nsdate/distantpast.md) — A date object representing a date in the distant past.

### Retrieving the Current Date

- [now](nsdate/now.md) — The current date and time, as of the time of access.

### Comparing Dates

- [- isEqualToDate:](<nsdate/isequal(to_).md>) — Returns a Boolean value that indicates whether a given object is a date that is exactly equal the receiver.
- [- earlierDate:](<nsdate/earlierdate(__).md>) — Returns the earlier of the receiver and another given date.
- [- laterDate:](<nsdate/laterdate(__).md>) — Returns the later of the receiver and another given date.
- [- compare:](<nsdate/compare(__).md>) — Indicates the temporal ordering of the receiver and another given date.

### Getting Time Intervals

- [- timeIntervalSinceDate:](<nsdate/timeintervalsince(__).md>) — Returns the interval between the receiver and another given date.
- [timeIntervalSinceNow](nsdate/timeintervalsincenow.md) — The interval between the date object and the current date and time.
- [timeIntervalSinceReferenceDate](nsdate/timeintervalsincereferencedate-swift.property.md) — The interval between the date object and 00:00:00 UTC on 1 January 2001.
- [timeIntervalSince1970](nsdate/timeintervalsince1970.md) — The interval between the date object and 00:00:00 UTC on 1 January 1970.
- [timeIntervalSinceReferenceDate](nsdate/timeintervalsincereferencedate-swift.type.property.md) — The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.
- [NSTimeIntervalSince1970](nstimeintervalsince1970.md) — The number of seconds from 1 January 1970 to the reference date, 1 January 2001.

### Adding Time Intervals

- [- dateByAddingTimeInterval:](<nsdate/addingtimeinterval(__).md>) — Returns a new date object that is set to a given number of seconds relative to the receiver.

### Describing Dates

- [description](nsdate/description.md) — A string representation of the date object.
- [- descriptionWithLocale:](<nsdate/description(with_).md>) — Returns a string representation of the date using the given locale.
- [customPlaygroundQuickLook](nsdate/customplaygroundquicklook.md) — A custom playground Quick Look for this object. _(deprecated)_

### Recognizing Notifications

- [NSSystemClockDidChangeNotification](nsnotification/name-swift.struct/nssystemclockdidchange.md) — A notification posted whenever the system clock is changed.

### Legacy Operations

- [+ dateWithNaturalLanguageString:](<nsdate/date(withnaturallanguagestring_).md>) — Creates and returns a date object set to the date and time specified by a given string. _(deprecated)_
- [+ dateWithNaturalLanguageString:locale:](<nsdate/date(withnaturallanguagestring_locale_).md>) — Creates and returns a date object set to the date and time specified by a given string. _(deprecated)_
- [+ dateWithString:](<nsdate/date(with_).md>) — Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`). _(deprecated)_
- [- initWithString:](<nsdate/init(string_).md>) — Returns a date object initialized with a date and time value specified by a given string in the international string representation format. _(deprecated)_
- [- addTimeInterval:](<nsdate/addtimeinterval(__).md>) — Returns a new date object that is set to a given number of seconds relative to the receiver. _(deprecated)_
- [- dateWithCalendarFormat:timeZone:](<nsdate/date(withcalendarformat_timezone_).md>) — Converts the receiver to a calendar date with a given format string and time zone. _(deprecated)_
- [- descriptionWithCalendarFormat:timeZone:locale:](<nsdate/description(withcalendarformat_timezone_locale_).md>) — Returns a string representation of the date formatted as specified by given conversion specifiers. _(deprecated)_

### Initializers

- [- initWithSRAbsoluteTime:](<nsdate/init(srabsolutetime_)-886t8.md>)
- [+ dateWithSRAbsoluteTime:](<nsdate/init(srabsolutetime_)-9wpl1.md>)
- [- initWithTimeInterval:sinceDate:](<nsdate/init(timeinterval_since_).md>) — Returns a date object initialized relative to another given date by a given number of seconds.

### Instance Properties

- [srAbsoluteTime](nsdate/srabsolutetime.md)

### Default Implementations

- [NSDate Implementations](nsdate/nsdate-implementations.md)
