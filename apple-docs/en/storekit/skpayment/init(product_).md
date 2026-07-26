---
title: 'init(product:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpayment/init(product:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpayment/init(product:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpayment/init%28product%3A%29.json'
content_hash: 'sha256:cfcc8e05f40f0a88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPayment](../skpayment.md)

# init(product:)

<sub>Initializer</sub>

Returns a new payment for the specified product.

> [!warning] Deprecated
> Use Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(product: SKProduct)
```

## Parameters

- `product` — The product the user wishes to purchase.

## Return Value

A new payment object.

## Discussion

This [Object creation](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) uses the `productIdentifier` property obtained from the `product` parameter to create and return a new payment with that identifier. The quantity property defaults to `1`.

To create a [SKPayment](../skpayment.md) object with a quantity greater than `1`, create a `SKMutablePayment` object, adjust its `quantity` property and then add it to the payment queue.

```objc
SKMutablePayment *myPayment = [SKMutablePayment paymentWithProduct: myProduct];
myPayment.quantity = 2;
[[SKPaymentQueue defaultQueue] addPayment:myPayment];
```

## See Also

### Related Documentation

- [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
