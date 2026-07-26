---
title: Product.PromotionInfo
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.4+, iPadOS 16.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/promotioninfo
source_url: 'https://developer.apple.com/documentation/storekit/product/promotioninfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/promotioninfo.json'
content_hash: 'sha256:f031254b9019ff48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# Product.PromotionInfo

<sub>Structure</sub>

Information about a promoted In-App Purchase that customizes its order and visibility on the device.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct PromotionInfo
```

## Overview

The `Product.PromotionInfo` structure represents promoted in-app purchases available in your app. You set up promoted in-app purchases using App Store Connect, including their default display order and visibility settings. Use this API to override and customize their order and visibility. Overrides are per device. They can take effect after the user launches the app at least once.

You don’t instantiate this structure. To get a list of `Product.PromotionInfo` objects, call the static method [updateProductOrder(byID:)](<promotioninfo/updateproductorder(byid_).md>) with a list of product identifiers that represent your promoted in-app purchases. Then call [currentOrder](promotioninfo/currentorder.md) to get the list of `Product.PromotionInfo` objects. To change their order, call [updateAll(_:)](<promotioninfo/updateall(__).md>) with the promoted in-app purchases listed in the desired order. To change the order using product identifiers, call [updateProductOrder(byID:)](<promotioninfo/updateproductorder(byid_).md>).

To prevent a promoted in-app purchase from appearing in the App Store on the device, there are two options:

- Hide the product by setting the [visibility](promotioninfo/visibility-swift.property.md) value to [Product.PromotionInfo.Visibility.hidden](promotioninfo/visibility-swift.enum/hidden.md) and calling [update()](<promotioninfo/update().md>), or call [updateProductVisibility(_:for:)](<promotioninfo/updateproductvisibility(__for_).md>).
- Remove the product from the list by excluding it when you call [updateAll(_:)](<promotioninfo/updateall(__).md>) or [updateProductOrder(byID:)](<promotioninfo/updateproductorder(byid_).md>).

To cancel your overrides and return to the default order and visibility, call [updateAll(_:)](<promotioninfo/updateall(__).md>) or [updateProductOrder(byID:)](<promotioninfo/updateproductorder(byid_).md>) with an empty array.

For more information about promoting in-app purchases, see [Supporting promoted In-App Purchases in your app](../supporting-promoted-in-app-purchases-in-your-app.md).

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md)

## Topics

### Getting the product ID

- [productID](promotioninfo/productid.md) — The product identifier of the promoted in-app purchase.

### Managing promotion order

- [updateProductOrder(byID:)](<promotioninfo/updateproductorder(byid_).md>) — Sets the display order of promoted in-app purchases in the App Store, using product identifiers.

### Getting overridden order

- [currentOrder](promotioninfo/currentorder.md) — Gets the customized order of the promotion info objects the represent promoted products.

### Managing promotion visibility

- [visibility](promotioninfo/visibility-swift.property.md) — A value that indicates whether the promoted in-app purchase is visible or hidden on the user’s device.
- [Visibility](promotioninfo/visibility-swift.enum.md) — The visibility states for product promotion information.
- [updateProductVisibility(_:for:)](<promotioninfo/updateproductvisibility(__for_).md>) — Updates a value that indicates whether a promoted in-app purchase appears in the App Store on the user’s device.

### Updating order and visibility

- [update()](<promotioninfo/update().md>) — Saves your changes to the promoted product’s visibility.
- [updateAll(_:)](<promotioninfo/updateall(__).md>) — Sets the order and visibility of all the promoted products and saves your changes.

## See Also

### Promoted In-App Purchases

- [Supporting promoted In-App Purchases in your app](../supporting-promoted-in-app-purchases-in-your-app.md) — Display promoted In-App Purchases on your product page and handle purchases that users initiate on the App Store.
- [PurchaseIntent](../purchaseintent.md) — An instance that emits purchase intents, which indicate that the customer initiated a purchase outside of your app, for your app to complete.
- [Testing promoted In-App Purchases](../testing-promoted-in-app-purchases.md) — Test your In-App Purchases before making your app available in the App Store.
