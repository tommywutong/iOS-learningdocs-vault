---
title: 'string(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/datecomponentsformatter/string(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/string(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/string%28for%3A%29.json'
content_hash: 'sha256:b4137f9b1dc84017'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponentsFormatter](../datecomponentsformatter.md)

# string(for:)

<sub>Instance Method</sub>

Returns a formatted string based on the date information in the specified object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(for obj: Any?) -> String?
```

## Parameters

- `obj` — An object containing the date and time information to format. The object in this parameter must be a [NSDateComponents](../nsdatecomponents.md) object; if it is not, the method raises an exception. This parameter must not be `nil`.

## Return Value

A formatted string representing the specified date information.

## Discussion

This method has the same behavior as the [- stringFromDateComponents:](<string(from_)-9exxn.md>) method.

## See Also

### Formatting Values

- [- stringFromDateComponents:](<string(from_)-9exxn.md>) — Returns a formatted string based on the specified date component information.
- [- stringFromDate:toDate:](<string(from_to_).md>) — Returns a formatted string based on the time difference between two dates.
- [- stringFromTimeInterval:](<string(from_)-7sj4j.md>) — Returns a formatted string based on the specified number of seconds.
- [+ localizedStringFromDateComponents:unitsStyle:](<localizedstring(from_unitsstyle_).md>) — Returns a localized string based on the specified date components and style option.
