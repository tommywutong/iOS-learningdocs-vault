---
title: isFamilyShareable
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/isfamilyshareable
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/isfamilyshareable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/isfamilyshareable.json'
content_hash: 'sha256:aa54fa6f71196a5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# isFamilyShareable

<sub>Instance Property</sub>

A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect.

> [!warning] Deprecated
> Use Product.isFamilyShareable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isFamilyShareable: Bool { get }
```

## Discussion

Check the value of [isFamilyShareable](isfamilyshareable.md) to learn whether an in-app purchase is sharable with the family group.

```swift
// Determine whether an in-app purchase supports Family Sharing.
let myProduct: SKProduct = getProductWithId(id: "com.example.product_identifier")
if myProduct.isFamilyShareable {
    print("Product can be shared with family group.")
}
```

When displaying in-app purchases in your app, indicate whether the product includes Family Sharing to help customers make a selection that best fits their needs.

Configure your in-app purchases to allow Family Sharing in App Store Connect. For more information about setting up Family Sharing, see [Turn-on Family Sharing for in-app purchases](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/turn-on-family-sharing-for-in-app-purchases).

## See Also

### Family Sharing

- [Supporting Family Sharing in your app](../supporting-family-sharing-in-your-app.md) — Provide service to share subscriptions and non-consumable products to family members.
- [- paymentQueue:didRevokeEntitlementsForProductIdentifiers:](<../skpaymenttransactionobserver/paymentqueue(__didrevokeentitlementsforproductidentifiers_).md>) — Tells an observer that the customer is no longer entitled to one or more Family Sharing purchases. _(deprecated)_
