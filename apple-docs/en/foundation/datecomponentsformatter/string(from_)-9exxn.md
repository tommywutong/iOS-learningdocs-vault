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
doc_path: '/documentation/foundation/datecomponentsformatter/string(from:)-9exxn'
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/string(from:)-9exxn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/string%28from%3A%29-9exxn.json'
content_hash: 'sha256:44bf3981672df78a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# string(from:)

<sub>Instance Method</sub>

Returns a formatted string based on the specified date component information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(from components: DateComponents) -> String?
```

## Parameters

- `components` — A date components object containing the date and time information to format. The [allowedUnits](allowedunits.md) property determines which date components are actually used to generate the string. All other date components are ignored. This parameter must not be `nil`.

## Return Value

A formatted string representing the specified date information.

## Discussion

Use this method to format date information that is already broken down into the component day and time values.

## See Also

### Formatting Values

- [- stringForObjectValue:](<string(for_).md>) — Returns a formatted string based on the date information in the specified object.
- [- stringFromDate:toDate:](<string(from_to_).md>) — Returns a formatted string based on the time difference between two dates.
- [- stringFromTimeInterval:](<string(from_)-7sj4j.md>) — Returns a formatted string based on the specified number of seconds.
- [+ localizedStringFromDateComponents:unitsStyle:](<localizedstring(from_unitsstyle_).md>) — Returns a localized string based on the specified date components and style option.
