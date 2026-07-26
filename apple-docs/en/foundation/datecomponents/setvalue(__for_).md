---
title: 'setValue(_:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/datecomponents/setvalue(_:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/setvalue(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/setvalue%28_%3Afor%3A%29.json'
content_hash: 'sha256:ccdee8e12b265425'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# setValue(_:for:)

<sub>Instance Method</sub>

Set the value of one of the properties, using an enumeration value instead of a property name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func setValue(_ value: Int?, for component: Calendar.Component)
```

## Discussion

The calendar and timeZone and isLeapMonth properties cannot be set by this method.

## See Also

### Accessing Calendar Components

- [value(for:)](<value(for_).md>) — Returns the value of one of the properties, using an enumeration value instead of a property name.
- [Component](../calendar/component.md) — An enumeration for the various components of a calendar date.
