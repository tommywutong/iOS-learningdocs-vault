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
doc_path: /documentation/storekit/skpayment/quantity
source_url: 'https://developer.apple.com/documentation/storekit/skpayment/quantity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpayment/quantity.json'
content_hash: 'sha256:20ee01f9c0704047'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPayment](../skpayment.md)

# quantity

<sub>Instance Property</sub>

The number of items the user wants to purchase.

> [!warning] Deprecated
> Create a Product.PurchaseOption.quantity to use in Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var quantity: Int { get }
```

## Discussion

The default value is 1, the minimum value is 1, and the maximum value is 10.

## See Also

### Getting Payment Details

- [productIdentifier](productidentifier.md) — A string used to identify a product that can be purchased from within your app. _(deprecated)_
- [requestData](requestdata.md) — Reserved for future use. _(deprecated)_
- [applicationUsername](applicationusername.md) — A string that associates the transaction with a user account on your service. _(deprecated)_
