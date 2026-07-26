---
title: 'string(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/iso8601dateformatter/string(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/iso8601dateformatter/string(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/iso8601dateformatter/string%28from%3A%29.json'
content_hash: 'sha256:7ffb3a51251cf974'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ISO8601DateFormatter](../iso8601dateformatter.md)

# string(from:)

<sub>Instance Method</sub>

Creates and returns an ISO 8601 formatted string representation of the specified date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(from date: Date) -> String
```

## Parameters

- `date` — The date to be represented.

## Return Value

A user-readable string representing the date.

## See Also

### Converting ISO 8601 Dates

- [- dateFromString:](<date(from_).md>) — Creates and returns a date object from the specified ISO 8601 formatted string representation.
- [+ stringFromDate:timeZone:formatOptions:](<string(from_timezone_formatoptions_).md>) — Creates a representation of the specified date with a given time zone and format options.
