---
title: 'rounding(accordingToBehavior:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumber/rounding(accordingtobehavior:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/rounding(accordingtobehavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/rounding%28accordingtobehavior%3A%29.json'
content_hash: 'sha256:133ff9ba3a5c517a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# rounding(accordingToBehavior:)

<sub>Instance Method</sub>

Returns a rounded version of the decimal number using the specified rounding behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rounding(accordingToBehavior behavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber
```

## Discussion

For a description of the different ways of rounding, see the [roundingMode](../numberformatter/roundingmode-swift.property.md) method in the [NSDecimalNumberBehaviors](../nsdecimalnumberbehaviors.md) protocol specification.
