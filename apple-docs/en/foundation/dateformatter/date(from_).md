---
title: 'date(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dateformatter/date(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/date(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/date%28from%3A%29.json'
content_hash: 'sha256:bb45ddb5b28a8c05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# date(from:)

<sub>Instance Method</sub>

Returns a date representation of a specified string that the system interprets using the receiver’s current settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func date(from string: String) -> Date?
```

## Parameters

- `string` — The string to parse.

## Return Value

A date representation of `string`. If [- dateFromString:](<date(from_).md>) can’t parse the string, returns `nil`.

## Discussion

For more information about using [DateFormatter](../dateformatter.md) to convert a string to a date, see [Working With Fixed Format Date Representations](../dateformatter.md#Working-With-Fixed-Format-Date-Representations). For a sample code playground, see [Displaying Human-Friendly Content](../displaying-human-friendly-content.md).

## See Also

### Converting Objects

- [- stringFromDate:](<string(from_).md>) — Returns a string representation of a specified date that the system formats using the receiver’s current settings.
- [+ localizedStringFromDate:dateStyle:timeStyle:](<localizedstring(from_datestyle_timestyle_).md>) — Returns a string representation of a specified date, that the system formats for the current locale using the specified date and time styles.
- [- getObjectValue:forString:range:error:](<getobjectvalue(__for_range_).md>) — Returns by reference a date representation of a specified string and its date range, as well as a Boolean value that indicates whether the system can parse the string.
