---
title: isPositive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/componentsformatstyle/ispositive
source_url: 'https://developer.apple.com/documentation/foundation/date/componentsformatstyle/ispositive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/componentsformatstyle/ispositive.json'
content_hash: 'sha256:0d93bd189d63fcec'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ComponentsFormatStyle](../componentsformatstyle.md)

# isPositive

<sub>Instance Property</sub>

Controls whether the format input is formatted as a positive or negative range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isPositive: Bool
```

## Discussion

When the range is formatted as a positive value, the returned string describes the time from `lowerBound` to `upperBound`. When `isPositive` is set to `false`, the returned string describes the time from `upperBound` to `lowerBound`.
