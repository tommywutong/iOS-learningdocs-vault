---
title: subscriptionGroupIdentifier
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+（18.0 起废弃）, iPadOS 12.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14+（15.0 起废弃）, tvOS 12.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/subscriptiongroupidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/subscriptiongroupidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/subscriptiongroupidentifier.json'
content_hash: 'sha256:73e4099531811519'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# subscriptionGroupIdentifier

<sub>Instance Property</sub>

The identifier of the subscription group to which the subscription belongs.

> [!warning] Deprecated
> Use Product.subscription.subscriptionGroupID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var subscriptionGroupIdentifier: String? { get }
```

## Discussion

Auto-renewable subscriptions always belong to a subscription group. You create the subscription group identifiers in App Store Connect before you create and add an auto-renewable subscription. For more information about subscription groups, see [Offer auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev75708c031).

This property is `nil` if the [SKProduct](../skproduct.md) isn’t an auto-renewable subscription.

## See Also

### Getting Subscription Information

- [subscriptionPeriod](subscriptionperiod.md) — The period details for products that are subscriptions. _(deprecated)_
- [SKProductSubscriptionPeriod](../skproductsubscriptionperiod.md) — An object containing the subscription period duration information. _(deprecated)_
- [PeriodUnit](periodunit.md) — Values representing the duration of an interval, from a day up to a year. _(deprecated)_
