---
title: latestTransaction
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/latesttransaction
source_url: 'https://developer.apple.com/documentation/storekit/product/latesttransaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/latesttransaction.json'
content_hash: 'sha256:68ab917a797b94d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# latestTransaction

<sub>Instance Property</sub>

The most recent transaction for the product.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var latestTransaction: VerificationResult<Transaction>? { get async }
```

## Discussion

This value is `nil` if the customer has never purchased this product. The following code example illustrates requesting the most recent transaction for a product to determine whether the customer has purchased the product:

```swift
guard let resultingTransaction = await product.latestTransaction else {
    // The customer hasn't purchased this product.
    return
}
guard case .verified(let transaction) = resultingTransaction else {
    // Ignore unverified transactions.
    return
}
// Update your app based on the details from the most recent transaction.
```

By default, when the [SKIncludeConsumableInAppPurchaseHistory](../../bundleresources/information-property-list/skincludeconsumableinapppurchasehistory.md) property list key is `false`, this value excludes finished consumable in-app purchases unless they are refunded or revoked.

If you set the [SKIncludeConsumableInAppPurchaseHistory](../../bundleresources/information-property-list/skincludeconsumableinapppurchasehistory.md) property list key to `true`, this value returns all transactions, including consumable in-app purchases that your app marked as finished ([finish()](<../transaction/finish().md>)).
