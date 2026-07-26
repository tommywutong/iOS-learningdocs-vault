---
title: 'localizedString(for:relativeTo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/relativedatetimeformatter/localizedstring(for:relativeto:)'
source_url: 'https://developer.apple.com/documentation/foundation/relativedatetimeformatter/localizedstring(for:relativeto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/relativedatetimeformatter/localizedstring%28for%3Arelativeto%3A%29.json'
content_hash: 'sha256:eb840233c836d314'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RelativeDateTimeFormatter](../relativedatetimeformatter.md)

# localizedString(for:relativeTo:)

<sub>Instance Method</sub>

Formats the date interval from the reference date to the specified date using the formatter’s calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedString(for date: Date, relativeTo referenceDate: Date) -> String
```

## Parameters

- `date` — The end date of the interval to format.

- `referenceDate` — The start date of the interval to format.

## Return Value

A string that represents the date interval between two dates.

## Discussion

```swift
let tenMinutesAgo = Date(timeIntervalSinceNow: -600)
let twoMintuesAhead = Date(timeIntervalSinceNow: 120)
let formatter = RelativeDateTimeFormatter()
print(formatter.localizedString(for: tenMinutesAgo, relativeTo: twoMintuesAhead))
// Outputs: 12 minutes ago
```

## See Also

### Converting Dates to Formatted Strings

- [- localizedStringFromDateComponents:](<localizedstring(from_).md>) — Formats a relative time represented by the specified date components.
- [- localizedStringFromTimeInterval:](<localizedstring(fromtimeinterval_).md>) — Formats the specified time interval using the formatter’s calendar.
- [- stringForObjectValue:](<string(for_).md>) — Creates a formatted string for a date relative to the current date and time.
