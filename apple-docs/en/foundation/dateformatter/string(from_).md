---
title: 'string(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dateformatter/string(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/string(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/string%28from%3A%29.json'
content_hash: 'sha256:d3936ac37e50e25f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# string(from:)

<sub>Instance Method</sub>

Returns a string representation of a specified date that the system formats using the receiver’s current settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(from date: Date) -> String
```

## Parameters

- `date` — The date to format.

## Return Value

A string representation of `date`.

## Discussion

For more information about using [DateFormatter](../dateformatter.md) to produce a string representation of a date, see [Working With User-Visible Representations of Dates and Times](../dateformatter.md#Working-With-User-Visible-Representations-of-Dates-and-Times). For a sample code playground, see [Displaying Human-Friendly Content](../displaying-human-friendly-content.md).

## See Also

### Converting Objects

- [- dateFromString:](<date(from_).md>) — Returns a date representation of a specified string that the system interprets using the receiver’s current settings.
- [+ localizedStringFromDate:dateStyle:timeStyle:](<localizedstring(from_datestyle_timestyle_).md>) — Returns a string representation of a specified date, that the system formats for the current locale using the specified date and time styles.
- [- getObjectValue:forString:range:error:](<getobjectvalue(__for_range_).md>) — Returns by reference a date representation of a specified string and its date range, as well as a Boolean value that indicates whether the system can parse the string.
