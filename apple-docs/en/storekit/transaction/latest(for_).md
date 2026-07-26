---
title: 'latest(for:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/transaction/latest(for:)'
source_url: 'https://developer.apple.com/documentation/storekit/transaction/latest(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/latest%28for%3A%29.json'
content_hash: 'sha256:fa52b0c25aa9a501'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# latest(for:)

<sub>Type Method</sub>

Gets the customer’s most recent transaction for an In-App Purchase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func latest(for productID: String) async -> VerificationResult<Transaction>?
```

## Parameters

- `productID` — The product identifier that the method uses to look up the most recent transaction.

## Return Value

A [VerificationResult](../verificationresult.md) with a single [Transaction](../transaction.md), or `nil` if the customer hasn’t purchased the product.

## Discussion

Call this method for any type of In-App Purchase. The following code example illustrates requesting the most recent transaction to determine whether the customer purchased the product indicated by the string `productIdentifier`:

```swift
guard let verificationResult = await Transaction.latest(for: productIdentifier) else {    
    // The customer hasn't purchased this product.
    return
}

switch verificationResult {
case .verified(let transaction):
    // Check the transaction and give the customer access to purchased 
    // content as appropriate.
    ...
case .unverified(let transaction, let verificationError):
    // Handle unverified transactions based 
    // on your business model.
    ...
}
```

By default, when the [SKIncludeConsumableInAppPurchaseHistory](../../bundleresources/information-property-list/skincludeconsumableinapppurchasehistory.md) property list key is `false`, this method excludes finished consumable in-app purchases unless they are refunded or revoked.

If you set the [SKIncludeConsumableInAppPurchaseHistory](../../bundleresources/information-property-list/skincludeconsumableinapppurchasehistory.md) property list key to `true`, this method returns all transactions, including consumable In-App Purchases that your app marked as finished ([finish()](<finish().md>)).

## See Also

### Getting transaction history

- [all](all.md) — A sequence that emits all the customer’s transactions for your app.
- [unfinished](unfinished.md) — A sequence that emits unfinished transactions for the customer.
- [SKIncludeConsumableInAppPurchaseHistory](../../bundleresources/information-property-list/skincludeconsumableinapppurchasehistory.md) — A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.
