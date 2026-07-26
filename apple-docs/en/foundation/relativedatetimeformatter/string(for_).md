---
title: 'string(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/relativedatetimeformatter/string(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/relativedatetimeformatter/string(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/relativedatetimeformatter/string%28for%3A%29.json'
content_hash: 'sha256:d17155711b8e2813'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RelativeDateTimeFormatter](../relativedatetimeformatter.md)

# string(for:)

<sub>Instance Method</sub>

Creates a formatted string for a date relative to the current date and time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(for obj: Any?) -> String?
```

## Parameters

- `obj` — A date object to format.

## Return Value

A string that represents the date interval between a date and the current date and time, or `nil` if obj isn’t an instance of [NSDate](../nsdate.md).

## Discussion

To determine the relative interval, the formatter uses [date](../nsdate/date.md) as the reference date.

## See Also

### Converting Dates to Formatted Strings

- [- localizedStringForDate:relativeToDate:](<localizedstring(for_relativeto_).md>) — Formats the date interval from the reference date to the specified date using the formatter’s calendar.
- [- localizedStringFromDateComponents:](<localizedstring(from_).md>) — Formats a relative time represented by the specified date components.
- [- localizedStringFromTimeInterval:](<localizedstring(fromtimeinterval_).md>) — Formats the specified time interval using the formatter’s calendar.
