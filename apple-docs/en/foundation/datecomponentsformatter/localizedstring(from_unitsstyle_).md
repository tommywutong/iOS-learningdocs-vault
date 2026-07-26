---
title: 'localizedString(from:unitsStyle:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/datecomponentsformatter/localizedstring(from:unitsstyle:)'
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/localizedstring(from:unitsstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/localizedstring%28from%3Aunitsstyle%3A%29.json'
content_hash: 'sha256:bb557a62ab9f7186'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# localizedString(from:unitsStyle:)

<sub>Type Method</sub>

Returns a localized string based on the specified date components and style option.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func localizedString(from components: DateComponents, unitsStyle: DateComponentsFormatter.UnitsStyle) -> String?
```

## Parameters

- `components` — The value to format.

- `unitsStyle` — The style for the resulting units. Use this parameter to specify whether you want to the resulting string to use an abbreviated or more spelled out format.

## Return Value

A string containing the localized date and time information.

## Discussion

Use this convenience method to format a string using the default formatter values, with the exception of the `unitsStyle` value.

## See Also

### Formatting Values

- [- stringFromDateComponents:](<string(from_)-9exxn.md>) — Returns a formatted string based on the specified date component information.
- [- stringForObjectValue:](<string(for_).md>) — Returns a formatted string based on the date information in the specified object.
- [- stringFromDate:toDate:](<string(from_to_).md>) — Returns a formatted string based on the time difference between two dates.
- [- stringFromTimeInterval:](<string(from_)-7sj4j.md>) — Returns a formatted string based on the specified number of seconds.
