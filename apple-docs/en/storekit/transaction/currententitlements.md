---
title: currentEntitlements
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/currententitlements
source_url: 'https://developer.apple.com/documentation/storekit/transaction/currententitlements'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/currententitlements.json'
content_hash: 'sha256:6ef3a643cce3f0f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# currentEntitlements

<sub>Type Property</sub>

A sequence of the latest transactions that entitle a customer to In-App Purchases and subscriptions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var currentEntitlements: Transaction.Transactions { get }
```

## Discussion

The current entitlements sequence emits the latest transaction for each product the customer has an entitlement to, specifically:

- A transaction for each non-consumable In-App Purchase
- The latest transaction for each auto-renewable subscription that has a [RenewalState](../product/subscriptioninfo/renewalstate.md) state of [subscribed](../product/subscriptioninfo/renewalstate/subscribed.md) or [inGracePeriod](../product/subscriptioninfo/renewalstate/ingraceperiod.md)
- The latest transaction for each non-renewing subscription, including finished ones

Products that the App Store has refunded or revoked don’t appear in the current entitlements. Consumable In-App Purchases also don’t appear in the current entitlements. To get transactions for unfinished consumables, use the [unfinished](unfinished.md) or [all](all.md) sequences in [Transaction](../transaction.md).

The following example illustrates iterating through the current entitlements:

```swift
func refreshPurchasedProducts() async {
    // Iterate through the user's purchased products.
    for await verificationResult in Transaction.currentEntitlements {
        switch verificationResult {
        case .verified(let transaction):
            // Check the type of product for the transaction
            // and provide access to the content as appropriate.
            ...
        case .unverified(let unverifiedTransaction, let verificationError):
            // Handle unverified transactions based on your
            // business model.
            ...
        }
    }
}
```

## See Also

### Transaction history and entitlements

- [Transaction](../transaction.md) — Information that represents the customer’s purchase of a product in your app.
- [updates](updates.md) — The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.
- [all](all.md) — A sequence that emits all the customer’s transactions for your app.
