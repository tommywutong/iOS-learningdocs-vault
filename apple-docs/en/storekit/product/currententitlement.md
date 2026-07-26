---
title: currentEntitlement
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（18.4 起废弃）, iPadOS 15.0+（18.4 起废弃）, macOS 12.0+（15.4 起废弃）, tvOS 15.0+（18.4 起废弃）, visionOS 1.0+（2.4 起废弃）, watchOS 8.0+（11.4 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/product/currententitlement
source_url: 'https://developer.apple.com/documentation/storekit/product/currententitlement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/currententitlement.json'
content_hash: 'sha256:4e414b34a3a6a0ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# currentEntitlement

<sub>Instance Property</sub>

The transaction that entitles the user to the product.

> [!warning] Deprecated
> Use [currentEntitlements](currententitlements.md) property instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentEntitlement: VerificationResult<Transaction>? { get async }
```

## Discussion

This value is `nil` if the customer isn’t currently entitled to this product. Current entitlement information applies only to non-consumables, non-renewing subscriptions, and auto-renewable subscriptions. The following example checks the current entitlement for a product.

```swift
guard let verificationResult = await product.currentEntitlement else {
    // The user isn’t currently entitled to this product.
    return
}

switch verificationResult {
case .verified(let transaction):
    // Check the transaction and give the user access to purchased 
    // content as appropriate.
    ...
case .unverified(let transaction, let verificationError):
    // Handle unverified transactions based 
    // on your business model.
    ...
}
```
