---
title: numberOfPeriods
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductdiscount/numberofperiods
source_url: 'https://developer.apple.com/documentation/storekit/skproductdiscount/numberofperiods'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductdiscount/numberofperiods.json'
content_hash: 'sha256:feaf97a9a0a982e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductDiscount](../skproductdiscount.md)

# numberOfPeriods

<sub>Instance Property</sub>

An integer that indicates the number of periods the product discount is available.

> [!warning] Deprecated
> Use Product.SubscriptionOffer.periodCount.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberOfPeriods: Int { get }
```

## Discussion

A product discount may be available for one or more periods. The period, defined in [subscriptionPeriod](subscriptionperiod.md), is a set number of days, weeks, months, or years.

The total length of time that a product discount is available is calculated by multiplying the [numberOfPeriods](numberofperiods.md) by the period.

Note that the discount period is independent of the product subscription period.

## See Also

### Getting the Discount Duration

- [subscriptionPeriod](subscriptionperiod.md) — An object that defines the period for the product discount. _(deprecated)_
