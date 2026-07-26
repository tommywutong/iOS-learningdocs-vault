---
title: isValidDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdatecomponents/isvaliddate
source_url: 'https://developer.apple.com/documentation/foundation/nsdatecomponents/isvaliddate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatecomponents/isvaliddate.json'
content_hash: 'sha256:b5ea396f20859b2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateComponents](../nsdatecomponents.md)

# isValidDate

<sub>Instance Property</sub>

A Boolean value that indicates whether the current combination of properties represents a date which exists in the current calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isValidDate: Bool { get }
```

## Discussion

If the [timeZone](timezone.md) property is set on the receiver, the time zone property value is used. If the [calendar](calendar.md) property is not set on the receiver, `nil` is returned.

## See Also

### Validating a Date

- [- isValidDateInCalendar:](<isvaliddate(in_).md>) — Returns a Boolean value that indicates whether the current combination of properties represents a date which exists in the specified calendar.
- [date](date.md) — The date calculated from the current components using the stored calendar.
- [Undefined Components](../1430344-undefined-components.md) — Constants that denote that the value of a date component is undefined.
