---
title: applicationUsername
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（18.0 起废弃）, iPadOS 7.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.9+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpayment/applicationusername
source_url: 'https://developer.apple.com/documentation/storekit/skpayment/applicationusername'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpayment/applicationusername.json'
content_hash: 'sha256:142aa382544c7906'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPayment](../skpayment.md)

# applicationUsername

<sub>Instance Property</sub>

A string that associates the transaction with a user account on your service.

> [!warning] Deprecated
> Create a Product.PurchaseOption.appAccountToken to use in Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var applicationUsername: String? { get }
```

## Discussion

For more information on how to set and use this property, see [applicationUsername](../skmutablepayment/applicationusername.md).

## See Also

### Getting Payment Details

- [productIdentifier](productidentifier.md) — A string used to identify a product that can be purchased from within your app. _(deprecated)_
- [quantity](quantity.md) — The number of items the user wants to purchase. _(deprecated)_
- [requestData](requestdata.md) — Reserved for future use. _(deprecated)_
