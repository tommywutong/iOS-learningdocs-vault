---
title: numberOfUnits
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductsubscriptionperiod/numberofunits
source_url: 'https://developer.apple.com/documentation/storekit/skproductsubscriptionperiod/numberofunits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductsubscriptionperiod/numberofunits.json'
content_hash: 'sha256:51fef5f3391c0275'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductSubscriptionPeriod](../skproductsubscriptionperiod.md)

# numberOfUnits

<sub>Instance Property</sub>

The number of units per subscription period.

> [!warning] Deprecated
> Use Product.SubscriptionPeriod.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberOfUnits: Int { get }
```

## Discussion

A subscription period duration is calculated by multiplying the number of units by the [unit](unit.md).

For example, if the number of units is `3`, and the unit is [SKProductPeriodUnitMonth](../skproduct/periodunit/month.md), the subscription period is 3 months.

## See Also

### Getting Subscription Period Details

- [unit](unit.md) — The increment of time that a subscription period is specified in. _(deprecated)_
- [PeriodUnit](../skproduct/periodunit.md) — Values representing the duration of an interval, from a day up to a year. _(deprecated)_
