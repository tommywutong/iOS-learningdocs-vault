---
title: 'purchase(options:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchase(options:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchase(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchase%28options%3A%29.json'
content_hash: 'sha256:36e44d4872195081'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# purchase(options:)

<sub>Instance Method</sub>

Initiates a purchase for the product with the App Store and displays the confirmation sheet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
@MainActor func purchase(options: Set<Product.PurchaseOption> = []) async throws -> Product.PurchaseResult
```

## Parameters

- `options` — A set of options you can associate with the purchase.

## Return Value

Returns a [PurchaseResult](purchaseresult.md).

## Discussion

StoreKit provides several APIs you can use to enable customers to initiate a purchase. Before using [purchase(options:)](<purchase(options_).md>) consider the following APIs and choose the one that best suits your app’s implementation:

- Use [PurchaseAction](../purchaseaction.md) for apps that use [SwiftUI](../../swiftui.md) on any platform, including multi-scene apps for visionOS.
- Use [purchase(confirmIn:options:)](<purchase(confirmin_options_)-6dj6y.md>) for apps that use [UIKit](../../uikit.md).
- Use [purchase(confirmIn:options:)](<purchase(confirmin_options_)-8eai6.md>) for apps that run on macOS and use [AppKit](../../appkit.md).
- Use [purchase(options:)](<purchase(options_).md>) for apps that runs on watchOS.

> [!important] Important
> If you use StoreKit views such as [ProductView](../productview.md), [StoreView](../storeview.md), or [SubscriptionStoreView](../subscriptionstoreview.md) you don’t need to call any other API to initiate a purchase. StoreKit manages the purchase action automatically, including presenting the purchase confirmation UI. For more information, see [StoreKit views](../storekit-views.md).

### Use the purchase API

Call the [purchase(options:)](<purchase(options_).md>) method when a customer initiates a purchase, either within your app or after selecting a promoted in-app purchase on the App Store. This method brings up the system-confirmation sheet. The user can confirm to complete the transaction or cancel it.

Include the purchase options to provide additional information about the purchase, such as:

- [appAccountToken(_:)](<purchaseoption/appaccounttoken(__).md>) to associate the purchase with the resulting transaction
- [promotionalOffer(offerID:keyID:nonce:signature:timestamp:)](<purchaseoption/promotionaloffer(offerid_keyid_nonce_signature_timestamp_).md>), if the customer is redeeming a promotional offer for an auto-renewable subscription
- [quantity(_:)](<purchaseoption/quantity(__).md>), if the customer is purchasing more than one of the product

The following example illustrates calling [purchase(options:)](<purchase(options_).md>) using the `options` parameter to provide an app account token:

```swift
let appAccountToken = <# Generate an app account token. #>
let purchaseResult = try await product.purchase(options: [
    .appAccountToken(appAccountToken)
])
```

If you’re testing your app in the sandbox environment, test an Ask to Buy scenario by setting the [simulatesAskToBuyInSandbox(_:)](<purchaseoption/simulatesasktobuyinsandbox(__).md>) purchase option to `true`. For more information about Ask to Buy, see [Approve what kids buy with Ask to Buy](https://support.apple.com/en-us/HT201089).

This method may throw a [PurchaseError](purchaseerror.md) or [StoreKitError](../storekiterror.md).

For more information about purchases that users initiate on the App Store, see [Promoting In-App Purchases](../promoting-in-app-purchases.md).

## See Also

### Purchase requests and results

- [PurchaseAction](../purchaseaction.md) — An action that starts an In-App Purchase.
- [PurchaseResult](purchaseresult.md) — The result of a purchase.
