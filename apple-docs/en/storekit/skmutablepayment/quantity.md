---
title: quantity
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skmutablepayment/quantity
source_url: 'https://developer.apple.com/documentation/storekit/skmutablepayment/quantity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skmutablepayment/quantity.json'
content_hash: 'sha256:20d753f5f830b481'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKMutablePayment](../skmutablepayment.md)

# quantity

<sub>Instance Property</sub>

The number of items the user wants to purchase.

> [!warning] Deprecated
> Create a Product.PurchaseOption.quantity to use in Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var quantity: Int { get set }
```

## Discussion

The quantity property must be greater than `0`.

## See Also

### Getting and Setting Attributes

- [productIdentifier](productidentifier.md) — A string that identifies a product that can be purchased from within your app. _(deprecated)_
- [requestData](requestdata.md) — Reserved for future use. _(deprecated)_
- [applicationUsername](applicationusername.md) — A string that associates the transaction with a user account on your service. _(deprecated)_
