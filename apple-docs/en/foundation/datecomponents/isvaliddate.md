---
title: isValidDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponents/isvaliddate
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/isvaliddate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/isvaliddate.json'
content_hash: 'sha256:cd131d0c50b0fefa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# isValidDate

<sub>Instance Property</sub>

Indicates whether the current combination of properties represents a date which exists in the current calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isValidDate: Bool { get }
```

## Discussion

This method is not appropriate for use on `DateComponents` values which are specifying relative quantities of calendar components.

Except for some trivial cases (e.g., ‘seconds’ should be 0 - 59 in any calendar), this method is not necessarily cheap.

If the time zone property is set in the `DateComponents`, it is used.

The calendar property must be set, or the result is always `false`.

## See Also

### Validating a Date

- [isValidDate(in:)](<isvaliddate(in_).md>) — Indicates whether the current combination of properties represents a date which exists in the specified calendar.
- [date](date.md) — The date calculated from the current components using the stored calendar.
