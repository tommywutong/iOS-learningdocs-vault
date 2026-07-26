---
title: 'localizedString(fromTimeInterval:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/relativedatetimeformatter/localizedstring(fromtimeinterval:)'
source_url: 'https://developer.apple.com/documentation/foundation/relativedatetimeformatter/localizedstring(fromtimeinterval:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/relativedatetimeformatter/localizedstring%28fromtimeinterval%3A%29.json'
content_hash: 'sha256:2395c07cdb5f2c74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RelativeDateTimeFormatter](../relativedatetimeformatter.md)

# localizedString(fromTimeInterval:)

<sub>Instance Method</sub>

Formats the specified time interval using the formatter’s calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedString(fromTimeInterval timeInterval: TimeInterval) -> String
```

## Parameters

- `timeInterval` — The time interval to format.

## Return Value

A string that represents the formatted time interval.

## Discussion

The formatter interprets a negative time interval as a date in the past.

```swift
let formatter = RelativeDateTimeFormatter()
print(formatter.localizedString(fromTimeInterval: -120))
// Outputs:  2 minutes ago
```

## See Also

### Converting Dates to Formatted Strings

- [- localizedStringForDate:relativeToDate:](<localizedstring(for_relativeto_).md>) — Formats the date interval from the reference date to the specified date using the formatter’s calendar.
- [- localizedStringFromDateComponents:](<localizedstring(from_).md>) — Formats a relative time represented by the specified date components.
- [- stringForObjectValue:](<string(for_).md>) — Creates a formatted string for a date relative to the current date and time.
