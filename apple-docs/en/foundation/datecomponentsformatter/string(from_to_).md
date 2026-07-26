---
title: 'string(from:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/datecomponentsformatter/string(from:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/string(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/string%28from%3Ato%3A%29.json'
content_hash: 'sha256:ea49b73641d6d853'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# string(from:to:)

<sub>Instance Method</sub>

Returns a formatted string based on the time difference between two dates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(from startDate: Date, to endDate: Date) -> String?
```

## Parameters

- `startDate` — The start time. This parameter must not be `nil`.

- `endDate` — The end time. This parameter must not be `nil`.

## Return Value

A formatted string representing the specified time information.

## Discussion

This method calculates the elapsed time between the `startDate` and `endDate` values and uses that information to generate the string. For example, if there is exactly one hour and ten minutes difference between the start and end dates, generating an abbreviated string would result in a string of “1h 10m”.

## See Also

### Formatting Values

- [- stringFromDateComponents:](<string(from_)-9exxn.md>) — Returns a formatted string based on the specified date component information.
- [- stringForObjectValue:](<string(for_).md>) — Returns a formatted string based on the date information in the specified object.
- [- stringFromTimeInterval:](<string(from_)-7sj4j.md>) — Returns a formatted string based on the specified number of seconds.
- [+ localizedStringFromDateComponents:unitsStyle:](<localizedstring(from_unitsstyle_).md>) — Returns a localized string based on the specified date components and style option.
