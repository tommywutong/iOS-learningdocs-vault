---
title: 'purchaseDate(_:renewalBehavior:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchaseoption/purchasedate(_:renewalbehavior:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/purchasedate(_:renewalbehavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/purchasedate%28_%3Arenewalbehavior%3A%29.json'
content_hash: 'sha256:19166cb382704edb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseOption](../purchaseoption.md)

# purchaseDate(_:renewalBehavior:)

<sub>Type Method</sub>

Sets the purchase date for the transaction in the testing environment, and indicates the renewal behavior for an auto-renewable subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func purchaseDate(_ date: Date, renewalBehavior: Product.PurchaseOption.SubscriptionRenewalBehavior = .renewUntilNow) -> Product.PurchaseOption
```

## Parameters

- `date` — The purchase date for the transaction. Specify a date in the past or the current moment. Dates in the future aren’t valid.

- `renewalBehavior` — The renewal behavior for the auto-renewable subscription in this transaction, whether it renews continuously from the purchase date, or it cancels after the first period. By default, the subscription renews.

## Discussion

Use this purchase option when you test your app in Xcode using [StoreKit Test](../../../storekittest.md) and call [buyProduct(identifier:options:)](<../../../storekittest/sktestsession/buyproduct(identifier_options_).md>).

Use this purchase option to create useful transactions for your test cases. For example, use a date in the past with the default `renewalBehavior` to generate a full history of subscription renewals to test. Or, use a date in the past with the [Product.PurchaseOption.SubscriptionRenewalBehavior.cancelImmediately](subscriptionrenewalbehavior/cancelimmediately.md) behavior to simulate an account of a customer who canceled their subscription.

## See Also

### Setting options for StoreKit Testing in Xcode

- [SubscriptionRenewalBehavior](subscriptionrenewalbehavior.md) — Renewal options for auto-renewable subscriptions that you purchase in the testing environment.
- [codeOffer(referenceName:)](<codeoffer(referencename_).md>) — Sets an offer code for the transaction in the testing environment.
- [promotionalOffer(id:)](<promotionaloffer(id_).md>) — Sets a promotional offer for the transaction in the testing environment.
