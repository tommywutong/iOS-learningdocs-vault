---
title: 'localizedString(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/relativedatetimeformatter/localizedstring(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/relativedatetimeformatter/localizedstring(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/relativedatetimeformatter/localizedstring%28from%3A%29.json'
content_hash: 'sha256:4fdecd063637078b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RelativeDateTimeFormatter](../relativedatetimeformatter.md)

# localizedString(from:)

<sub>Instance Method</sub>

Formats a relative time represented by the specified date components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedString(from dateComponents: DateComponents) -> String
```

## Parameters

- `dateComponents` — The date components to format.

## Return Value

A string that represents the formatted relative time from date components.

## Discussion

The formatter interprets a negative component value as a date in the past.

```swift
let components = DateComponents(day: -2)
let formatter = RelativeDateTimeFormatter()
print(formatter.localizedString(from: components))
// Outputs:  2 days ago
```

This method formats the value of the least granular unit in the [NSDateComponents](../nsdatecomponents.md) object, and doesn’t provide a compound format of the date component.

> [!important] Important
> This method only supports year, month, week of month, day, hour, minute, and second components. The formatter ignores all other date components.

## See Also

### Converting Dates to Formatted Strings

- [- localizedStringForDate:relativeToDate:](<localizedstring(for_relativeto_).md>) — Formats the date interval from the reference date to the specified date using the formatter’s calendar.
- [- localizedStringFromTimeInterval:](<localizedstring(fromtimeinterval_).md>) — Formats the specified time interval using the formatter’s calendar.
- [- stringForObjectValue:](<string(for_).md>) — Creates a formatted string for a date relative to the current date and time.
