---
title: date
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdatecomponents/date
source_url: 'https://developer.apple.com/documentation/foundation/nsdatecomponents/date'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatecomponents/date.json'
content_hash: 'sha256:2b68fa1aa3432996'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateComponents](../nsdatecomponents.md)

# date

<sub>Instance Property</sub>

The date calculated from the current components using the stored calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var date: Date? { get }
```

## Discussion

Returns `nil` if the [calendar](calendar.md) property value of the receiver is `nil` or cannot convert the receiver into an [NSDate](../nsdate.md) object.

See [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Related Documentation

- [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i)

### Validating a Date

- [validDate](isvaliddate.md) — A Boolean value that indicates whether the current combination of properties represents a date which exists in the current calendar.
- [- isValidDateInCalendar:](<isvaliddate(in_).md>) — Returns a Boolean value that indicates whether the current combination of properties represents a date which exists in the specified calendar.
- [Undefined Components](../1430344-undefined-components.md) — Constants that denote that the value of a date component is undefined.
