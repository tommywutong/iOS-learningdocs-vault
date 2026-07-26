---
title: 'advanced(by:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/advanced(by:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/advanced(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/advanced%28by%3A%29.json'
content_hash: 'sha256:95dd7b53b1f5478f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# advanced(by:)

<sub>Instance Method</sub>

Returns a date offset the specified time interval from this date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func advanced(by n: TimeInterval) -> Date
```

## Parameters

- `n` — The time interval offset.

## Return Value

A date offset the specified time interval from this date.

## See Also

### Adding or Subtracting a Time Interval

- [addTimeInterval(_:)](<addtimeinterval(__).md>) — Adds a time interval to this date.
- [addingTimeInterval(_:)](<addingtimeinterval(__).md>) — Creates a new date value by adding a time interval to this date.
- [+(_:_:)](<+(____).md>) — Returns a date with a specified amount of time added to it.
- [+=(_:_:)](<+=(____).md>) — Adds a time interval to a date.
- [-(_:_:)](<-(____).md>) — Returns a `Date` with a specified amount of time subtracted from it.
- [-=(_:_:)](<-=(____).md>) — Subtract a `TimeInterval` from a `Date`.
