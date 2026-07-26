---
title: 'value(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/datecomponents/value(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/value(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/value%28for%3A%29.json'
content_hash: 'sha256:47f98ca731de98d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# value(for:)

<sub>Instance Method</sub>

Returns the value of one of the properties, using an enumeration value instead of a property name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(for component: Calendar.Component) -> Int?
```

## Discussion

The calendar and timeZone and isLeapMonth property values cannot be retrieved by this method.

## See Also

### Accessing Calendar Components

- [setValue(_:for:)](<setvalue(__for_).md>) — Set the value of one of the properties, using an enumeration value instead of a property name.
- [Component](../calendar/component.md) — An enumeration for the various components of a calendar date.
