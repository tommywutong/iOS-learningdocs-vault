---
title: Product.PurchaseResult
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/purchaseresult
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseresult.json'
content_hash: 'sha256:8e3d978b93d364d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# Product.PurchaseResult

<sub>Enumeration</sub>

The result of a purchase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum PurchaseResult
```

## Overview

The value of the purchase result represents the state of the purchase. When successful, the associated value contains a [VerificationResult](../verificationresult.md) of the transaction. The following example illustrates calling [purchase(options:)](<purchase(options_).md>) on a [Product](../product.md) value, checking the purchase status, and inspecting information about a successful transaction.

```swift
let result = try await product.purchase()
switch result {
case .success(let verificationResult):
    switch verificationResult {
    case .verified(let transaction):
        // Give the user access to purchased content.
        ...
        // Complete the transaction after providing
        // the user access to the content.
        await transaction.finish()
    case .unverified(let transaction, let verificationError):
        // Handle unverified transactions based 
        // on your business model.
        ...
    }
case .pending:
    // The purchase requires action from the customer. 
    // If the transaction completes, 
    // it's available through Transaction.updates.
    break
case .userCancelled:
    // The user canceled the purchase.
    break
@unknown default:
    break
}

```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the Purchase Results

- [Product.PurchaseResult.success(_:)](<purchaseresult/success(__).md>) — The purchase succeeded and results in a transaction.
- [Product.PurchaseResult.userCancelled](purchaseresult/usercancelled.md) — The user canceled the purchase.
- [Product.PurchaseResult.pending](purchaseresult/pending.md) — The purchase is pending, and requires action from the customer.

## See Also

### Purchase requests and results

- [PurchaseAction](../purchaseaction.md) — An action that starts an In-App Purchase.
- [purchase(options:)](<purchase(options_).md>) — Initiates a purchase for the product with the App Store and displays the confirmation sheet.
