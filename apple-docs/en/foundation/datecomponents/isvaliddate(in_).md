---
title: 'isValidDate(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/datecomponents/isvaliddate(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/isvaliddate(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/isvaliddate%28in%3A%29.json'
content_hash: 'sha256:24c124c8445122d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# isValidDate(in:)

<sub>Instance Method</sub>

Indicates whether the current combination of properties represents a date which exists in the specified calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isValidDate(in calendar: Calendar) -> Bool
```

## Discussion

This method is not appropriate for use on `DateComponents` values which are specifying relative quantities of calendar components.

Except for some trivial cases (e.g., ‘seconds’ should be 0 - 59 in any calendar), this method is not necessarily cheap.

If the time zone property is set in the `DateComponents`, it is used.

## See Also

### Validating a Date

- [isValidDate](isvaliddate.md) — Indicates whether the current combination of properties represents a date which exists in the current calendar.
- [date](date.md) — The date calculated from the current components using the stored calendar.
