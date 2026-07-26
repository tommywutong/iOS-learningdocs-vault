---
title: productIdentifier
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skmutablepayment/productidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skmutablepayment/productidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skmutablepayment/productidentifier.json'
content_hash: 'sha256:be7b393ed5601573'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKMutablePayment](../skmutablepayment.md)

# productIdentifier

<sub>Instance Property</sub>

A string that identifies a product that can be purchased from within your app.

> [!warning] Deprecated
> Use Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var productIdentifier: String { get set }
```

## Discussion

The product identifier is a string previously agreed on between your app and the Apple App Store.

## See Also

### Related Documentation

- [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)

### Getting and Setting Attributes

- [quantity](quantity.md) — The number of items the user wants to purchase. _(deprecated)_
- [requestData](requestdata.md) — Reserved for future use. _(deprecated)_
- [applicationUsername](applicationusername.md) — A string that associates the transaction with a user account on your service. _(deprecated)_
