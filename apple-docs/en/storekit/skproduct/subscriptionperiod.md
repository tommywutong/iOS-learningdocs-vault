---
title: subscriptionPeriod
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/subscriptionperiod
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/subscriptionperiod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/subscriptionperiod.json'
content_hash: 'sha256:b55a2350833e38a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# subscriptionPeriod

<sub>Instance Property</sub>

The period details for products that are subscriptions.

> [!warning] Deprecated
> Use Product.subscription.subscriptionPeriod.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var subscriptionPeriod: SKProductSubscriptionPeriod? { get }
```

## Discussion

This read-only property is `nil` if the product is not a subscription.

A subscription period is described in terms of a unit and the number of units that make up a single period.

## See Also

### Getting Subscription Information

- [subscriptionGroupIdentifier](subscriptiongroupidentifier.md) — The identifier of the subscription group to which the subscription belongs. _(deprecated)_
- [SKProductSubscriptionPeriod](../skproductsubscriptionperiod.md) — An object containing the subscription period duration information. _(deprecated)_
- [PeriodUnit](periodunit.md) — Values representing the duration of an interval, from a day up to a year. _(deprecated)_
