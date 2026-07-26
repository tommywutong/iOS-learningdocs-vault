---
title: 'purchase(confirmIn:options:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchase(confirmin:options:)-6dj6y'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchase(confirmin:options:)-6dj6y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchase%28confirmin%3Aoptions%3A%29-6dj6y.json'
content_hash: 'sha256:bb1402a3fc78823f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# purchase(confirmIn:options:)

<sub>Instance Method</sub>

Initiates a purchase for the product with the App Store and displays the confirmation sheet.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func purchase(confirmIn scene: some UIScene, options: Set<Product.PurchaseOption> = []) async throws -> Product.PurchaseResult
```

## Parameters

- `scene` — The [UIScene](../../uikit/uiscene.md) the system uses to show the purchase confirmation UI.

- `options` — A set of options ([PurchaseOption](purchaseoption.md)) you can associate with the purchase.

## Return Value

The result of the purchase, [PurchaseResult](purchaseresult.md).

## Discussion

StoreKit provides several APIs you can use to enable customers to initiate a purchase. Before using [purchase(confirmIn:options:)](<purchase(confirmin_options_)-6dj6y.md>), consider the following APIs and choose the one that best suits your app’s implementation:

- Use [PurchaseAction](../purchaseaction.md) for apps that use [SwiftUI](../../swiftui.md) on any platform, including multi-scene apps for visionOS.
- Use [purchase(confirmIn:options:)](<purchase(confirmin_options_)-6dj6y.md>) for apps that use [UIKit](../../uikit.md).
- Use [purchase(confirmIn:options:)](<purchase(confirmin_options_)-8eai6.md>) for apps that run on macOS and use [AppKit](../../appkit.md).
- Use [purchase(options:)](<purchase(options_).md>) for apps that runs on watchOS.

> [!important] Important
> If you use StoreKit views such as [ProductView](../productview.md), [StoreView](../storeview.md), or [SubscriptionStoreView](../subscriptionstoreview.md) you don’t need to call any other API to initiate a purchase. StoreKit manages the purchase action automatically, including presenting the purchase confirmation UI. For more information, see [StoreKit views](../storekit-views.md).

This method may throw a [PurchaseError](purchaseerror.md) or [StoreKitError](../storekiterror.md).

## See Also

### Purchasing a product

- [purchase(options:)](<purchase(options_).md>) — Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [purchase(confirmIn:options:)](<purchase(confirmin_options_)-3bivf.md>) — Processes a purchase for the product.
- [purchase(confirmIn:options:)](<purchase(confirmin_options_)-8eai6.md>) — Processes a purchase for the product.
- [PurchaseOption](purchaseoption.md) — Optional settings for a product purchase that add account information, purchase details, and offers, or that specify behaviors.
- [PurchaseResult](purchaseresult.md) — The result of a purchase.
- [PurchaseError](purchaseerror.md) — Error information for product purchase errors.
