---
title: NSCalendar.Options
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscalendar/options
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/options.json'
content_hash: 'sha256:51ffaaa149530457'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# NSCalendar.Options

<sub>Structure</sub>

The options for arithmetic operations involving calendars.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Options
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<options/init(rawvalue_).md>)

### Constants

- [NSCalendarWrapComponents](options/wrapcomponents.md) — Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.
- [NSCalendarMatchStrictly](options/matchstrictly.md) — Specifies that the operation should travel as far forward or backward as necessary looking for a match.
- [NSCalendarSearchBackwards](options/searchbackwards.md) — Specifies that the operation should travel backwards to find the previous match before the given date.
- [NSCalendarMatchPreviousTimePreservingSmallerUnits](options/matchprevioustimepreservingsmallerunits.md) — Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the _previous_ existing value of the missing unit and preserves the lower units’ values.
- [NSCalendarMatchNextTimePreservingSmallerUnits](options/matchnexttimepreservingsmallerunits.md) — Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the _next_ existing value of the missing unit and preserves the lower units’ values.
- [NSCalendarMatchNextTime](options/matchnexttime.md) — Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the _next_ existing value of the missing unit and _does not_ preserve the lower units’ values.
- [NSCalendarMatchFirst](options/matchfirst.md) — Specifies that, if there are two or more matching times, the operation should return the first occurrence.
- [NSCalendarMatchLast](options/matchlast.md) — Specifies that, if there are two or more matching times, the operation should return the last occurrence.
- [NSWrapCalendarComponents](../nswrapcalendarcomponents.md) — Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented. _(deprecated)_

## See Also

### Scanning Dates

- [- startOfDayForDate:](<startofday(for_).md>) — Returns the first moment of a given date as a date instance.
- [- enumerateDatesStartingAfterDate:matchingComponents:options:usingBlock:](<enumeratedates(startingafter_matching_options_using_).md>) — Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
- [- nextDateAfterDate:matchingComponents:options:](<nextdate(after_matching_options_).md>) — Returns the next date after a given date matching the given components.
- [- nextDateAfterDate:matchingHour:minute:second:options:](<nextdate(after_matchinghour_minute_second_options_).md>) — Returns the next date after a given date that matches the given hour, minute, and second, component values.
- [- nextDateAfterDate:matchingUnit:value:options:](<nextdate(after_matching_value_options_).md>) — Returns the next date after a given date matching the given calendar unit value.
- [NSWrapCalendarComponents](../nswrapcalendarcomponents-api.md) — A legacy constant used to control overflow in date calculations.
