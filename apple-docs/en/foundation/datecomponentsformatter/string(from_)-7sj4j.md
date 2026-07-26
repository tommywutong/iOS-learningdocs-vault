---
title: 'string(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/datecomponentsformatter/string(from:)-7sj4j'
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/string(from:)-7sj4j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/string%28from%3A%29-7sj4j.json'
content_hash: 'sha256:7be7d94703fecf0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# string(from:)

<sub>Instance Method</sub>

Returns a formatted string based on the specified number of seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(from ti: TimeInterval) -> String?
```

## Parameters

- `ti` — The time interval, measured in seconds. The value must be a finite number. Negative numbers are treated as positive numbers when creating the string.

## Return Value

A formatted string representing the specified time interval.

## Discussion

This method formats the specified number of seconds into the appropriate units. For example, if the formatter allows the display of minutes and seconds, creating an abbreviated string for the value 70 seconds results in the string “1m 10s”.

## See Also

### Formatting Values

- [- stringFromDateComponents:](<string(from_)-9exxn.md>) — Returns a formatted string based on the specified date component information.
- [- stringForObjectValue:](<string(for_).md>) — Returns a formatted string based on the date information in the specified object.
- [- stringFromDate:toDate:](<string(from_to_).md>) — Returns a formatted string based on the time difference between two dates.
- [+ localizedStringFromDateComponents:unitsStyle:](<localizedstring(from_unitsstyle_).md>) — Returns a localized string based on the specified date components and style option.
