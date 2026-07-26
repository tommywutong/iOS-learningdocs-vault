---
title: offer
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 16.4+, macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/purchaseintent/offer
source_url: 'https://developer.apple.com/documentation/storekit/purchaseintent/offer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/purchaseintent/offer.json'
content_hash: 'sha256:e543d79d46a7e77b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [PurchaseIntent](../purchaseintent.md)

# offer

<sub>Instance Property</sub>

The subscription offer that the customer redeems outside of your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
let offer: Product.SubscriptionOffer?
```

## Discussion

The system populates this value if the customer redeems a [winBack](../product/subscriptionoffer/offertype/winback.md) offer type outside of your app. Add this offer to the purchase options. For more information and a code example, see the [Handle win-back offers redeemed outside of your app](../supporting-win-back-offers-in-your-app.md#Handle-win-back-offers-redeemed-outside-of-your-app) section of  [Supporting win-back offers in your app](../supporting-win-back-offers-in-your-app.md).
