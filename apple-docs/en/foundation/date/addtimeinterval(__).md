---
title: 'addTimeInterval(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/addtimeinterval(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/addtimeinterval(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/addtimeinterval%28_%3A%29.json'
content_hash: 'sha256:dfef632fc716b642'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# addTimeInterval(_:)

<sub>Instance Method</sub>

Adds a time interval to this date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addTimeInterval(_ timeInterval: TimeInterval)
```

## Parameters

- `timeInterval` — The value to add, in seconds.

## Discussion

> [!warning] Warning
> This only adjusts an absolute value. If you wish to add calendrical concepts like hours, days, months then you must use a `Calendar`. That will take into account complexities like daylight saving time, months with different numbers of days, and more.

## See Also

### Adding or Subtracting a Time Interval

- [addingTimeInterval(_:)](<addingtimeinterval(__).md>) — Creates a new date value by adding a time interval to this date.
- [advanced(by:)](<advanced(by_).md>) — Returns a date offset the specified time interval from this date.
- [+(_:_:)](<+(____).md>) — Returns a date with a specified amount of time added to it.
- [+=(_:_:)](<+=(____).md>) — Adds a time interval to a date.
- [-(_:_:)](<-(____).md>) — Returns a `Date` with a specified amount of time subtracted from it.
- [-=(_:_:)](<-=(____).md>) — Subtract a `TimeInterval` from a `Date`.
