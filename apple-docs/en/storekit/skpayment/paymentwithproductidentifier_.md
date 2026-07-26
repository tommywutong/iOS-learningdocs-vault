---
title: 'paymentWithProductIdentifier:'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+（5.0 起废弃）, iPadOS 3.0+（5.0 起废弃）, Mac Catalyst 13.1+（13.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpayment/paymentwithproductidentifier:'
source_url: 'https://developer.apple.com/documentation/storekit/skpayment/paymentwithproductidentifier:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpayment/paymentwithproductidentifier%3A.json'
content_hash: 'sha256:5c41e4f8ef31b182'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPayment](../skpayment.md)

# paymentWithProductIdentifier:

<sub>Type Method</sub>

Returns a new payment with the specified product identifier.

> [!warning] Deprecated
> Use [+ paymentWithProduct:](<init(product_).md>) instead, passing a product returned from [SKProductsRequest](../skproductsrequest.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (id) paymentWithProductIdentifier:(NSString *) identifier;
```

## Parameters

- `identifier` — A string that identifies the item to be purchased.

## Return Value

A new payment object.

## Discussion

The product identifier is a string previously agreed on between your application and the Apple App Store. The quantity property defaults to `1`.

To create a [SKPayment](../skpayment.md) object with a quantity greater than `1`, create a `SKMutablePayment` object, adjust its [quantity](../skmutablepayment/quantity.md) property and then add it to the payment queue:

```objc
SKMutablePayment *myPayment = [SKMutablePayment paymentWithProductIdentifier: myIdentifier];
myPayment.quantity = 2;
[[SKPaymentQueue defaultQueue] addPayment:myPayment];
```

## See Also

### Creating Payments

- [+ paymentWithProduct:](<init(product_).md>) — Returns a new payment for the specified product. _(deprecated)_
