---
title: unit
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptionperiod/unit-swift.property
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionperiod/unit-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionperiod/unit-swift.property.json'
content_hash: 'sha256:43daf4fa555aca2c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionPeriod](../subscriptionperiod.md)

# unit

<sub>Instance Property</sub>

The increment of time for the subscription period.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let unit: Product.SubscriptionPeriod.Unit
```

## Discussion

The units used to specify a subscription period include day, week, month, and year, as defined in [Unit](unit-swift.enum.md).

To calculate the duration of one subscription period, multiply the [unit](unit-swift.property.md) by the number of units ([value](value.md)).

## See Also

### Getting the subscription period

- [value](value.md) — The number of period units.
- [Unit](unit-swift.enum.md) — Units of time that describe subscription periods.
