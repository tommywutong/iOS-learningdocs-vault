---
title: subscriptionPeriod
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductdiscount/subscriptionperiod
source_url: 'https://developer.apple.com/documentation/storekit/skproductdiscount/subscriptionperiod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductdiscount/subscriptionperiod.json'
content_hash: 'sha256:3776b79369c586f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductDiscount](../skproductdiscount.md)

# subscriptionPeriod

<sub>Instance Property</sub>

An object that defines the period for the product discount.

> [!warning] Deprecated
> Use Product.SubscriptionOffer.period.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var subscriptionPeriod: SKProductSubscriptionPeriod { get }
```

## Discussion

This object represents the duration of a single subscription period. A period is described as a number of units, where a unit can be a [SKProductPeriodUnitDay](../skproduct/periodunit/day.md), [SKProductPeriodUnitMonth](../skproduct/periodunit/month.md), [SKProductPeriodUnitWeek](../skproduct/periodunit/week.md), or [SKProductPeriodUnitYear](../skproduct/periodunit/year.md).

To calculate the total amount of time that the discount price is available to the user, multiply the [subscriptionPeriod](subscriptionperiod.md) by [numberOfPeriods](numberofperiods.md).

> [!note] Note
> The subscription period for the discount is independent of the product’s regular subscription period, and does not have to match in units or duration.

## See Also

### Getting the Discount Duration

- [numberOfPeriods](numberofperiods.md) — An integer that indicates the number of periods the product discount is available. _(deprecated)_
