---
title: '<(_:_:)'
framework: Foundation
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/_(_:_:)-7pou4'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/_(_:_:)-7pou4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/_%28_%3A_%3A%29-7pou4.json'
content_hash: 'sha256:35b61ae28d886bff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Measurement](../measurement.md)

# \<(_:_:)

<sub>Operator</sub>

Compare two measurements of the same `Unit`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func < <LeftHandSideType, RightHandSideType>(lhs: Measurement<LeftHandSideType>, rhs: Measurement<RightHandSideType>) -> Bool where LeftHandSideType : Unit, RightHandSideType : Unit
```

## Return Value

`true` if the measurements can be compared and the `lhs` is less than the `rhs` converted value.
