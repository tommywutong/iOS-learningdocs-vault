---
title: value
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptionperiod/value
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionperiod/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionperiod/value.json'
content_hash: 'sha256:f9f9c88e24d6bb56'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionPeriod](../subscriptionperiod.md)

# value

<sub>Instance Property</sub>

The number of period units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let value: Int
```

## Discussion

Use the value and the unit together to determine the subscription period. For example, if the [unit](unit-swift.property.md) is [Product.SubscriptionPeriod.Unit.month](unit-swift.enum/month.md), and the [value](value.md) is `3`, the subscription period is three months.

## See Also

### Getting the subscription period

- [unit](unit-swift.property.md) — The increment of time for the subscription period.
- [Unit](unit-swift.enum.md) — Units of time that describe subscription periods.
