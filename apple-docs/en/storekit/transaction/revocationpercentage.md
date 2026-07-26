---
title: revocationPercentage
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/revocationpercentage
source_url: 'https://developer.apple.com/documentation/storekit/transaction/revocationpercentage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/revocationpercentage.json'
content_hash: 'sha256:f1f938ed829eabaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# revocationPercentage

<sub>Instance Property</sub>

The percentage of the transaction amount that the App Store has refunded or revoked, expressed as a decimal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 26.4, macOS 26.4, tvOS 26.4, watchOS 26.4, visionOS 26.4)
var revocationPercentage: Decimal? { get }
```

## Discussion

This property indicates the rounded percentage of the purchase amount that the App Store has refunded or revoked.

The value is present only for transactions with a non-reversed refund. Valid values range from 0.0 to 100.0:

- For auto-renewable subscriptions: 0.0-100.0% based on time remaining in the subscription period
- For consumables, non-consumables, and non-renewing subscriptions: 0.0-100.0% based on consumption data

If the purchase had a quantity greater than 1, this percentage applies to the full quantity. For example, if 1 of 3 items was refunded, the value would be approximately 33.333. The following table shows several examples of revocation percentages, and their milliunit equivalents:

| Percentage | Integer equivalent, in milliunits |
|---|---|
| 67.932% | 67932 |
| 0.015% | 15 |
| 40% | 40000 |
| 100% | 100000 |

> [!note] Note
> This property is not present for Advanced Commerce transactions, which use [amount](advancedcommerceinfo-swift.struct/refund/amount.md) instead.
