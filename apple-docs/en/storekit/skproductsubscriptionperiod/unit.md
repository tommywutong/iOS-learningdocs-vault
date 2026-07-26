---
title: unit
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductsubscriptionperiod/unit
source_url: 'https://developer.apple.com/documentation/storekit/skproductsubscriptionperiod/unit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductsubscriptionperiod/unit.json'
content_hash: 'sha256:700f843b833ead6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductSubscriptionPeriod](../skproductsubscriptionperiod.md)

# unit

<sub>Instance Property</sub>

The increment of time that a subscription period is specified in.

> [!warning] Deprecated
> Use Product.SubscriptionPeriod.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unit: SKProduct.PeriodUnit { get }
```

## Discussion

The units used to specify a subscription period include day, week, month, and year, as defined in [PeriodUnit](../skproduct/periodunit.md).

To calculate the duration of one subscription period, multiply the [unit](unit.md) by the number of units ([numberOfUnits](numberofunits.md)).

## See Also

### Getting Subscription Period Details

- [numberOfUnits](numberofunits.md) — The number of units per subscription period. _(deprecated)_
- [PeriodUnit](../skproduct/periodunit.md) — Values representing the duration of an interval, from a day up to a year. _(deprecated)_
