---
title: 'codeOffer(referenceName:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchaseoption/codeoffer(referencename:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/codeoffer(referencename:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/codeoffer%28referencename%3A%29.json'
content_hash: 'sha256:6f18f6befa000188'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseOption](../purchaseoption.md)

# codeOffer(referenceName:)

<sub>Type Method</sub>

Sets an offer code for the transaction in the testing environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func codeOffer(referenceName: String) -> Product.PurchaseOption
```

## Parameters

- `referenceName` — The reference name of the offer code to apply to the transaction. You need to set up offer codes in your StoreKit configuration file.

## Discussion

Use this purchase option when you test your app in Xcode using [StoreKit Test](../../../storekittest.md) and call [buyProduct(identifier:options:)](<../../../storekittest/sktestsession/buyproduct(identifier_options_).md>).

Set up the offer codes to use in this call in your StoreKit configuration file. For more information, see [Setting up StoreKit Testing in Xcode](../../../xcode/setting-up-storekit-testing-in-xcode.md).

When you apply this option, the purchase transaction simulates a customer redeeming an offer code and includes the offer code you specify.

## See Also

### Setting options for StoreKit Testing in Xcode

- [purchaseDate(_:renewalBehavior:)](<purchasedate(__renewalbehavior_).md>) — Sets the purchase date for the transaction in the testing environment, and indicates the renewal behavior for an auto-renewable subscription.
- [SubscriptionRenewalBehavior](subscriptionrenewalbehavior.md) — Renewal options for auto-renewable subscriptions that you purchase in the testing environment.
- [promotionalOffer(id:)](<promotionaloffer(id_).md>) — Sets a promotional offer for the transaction in the testing environment.
