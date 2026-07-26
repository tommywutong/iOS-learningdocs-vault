---
title: updates
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/updates
source_url: 'https://developer.apple.com/documentation/storekit/transaction/updates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/updates.json'
content_hash: 'sha256:030fdb21489c98f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# updates

<sub>Type Property</sub>

The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var updates: Transaction.Transactions { get }
```

## Discussion

Use [updates](updates.md) to receive new transactions while the app is running. This sequence receives transactions that occur outside of the app, such as Ask to Buy transactions, offer code redemptions, and purchases that customers make in the App Store. It also emits transactions that customers complete in your app on another device.

Note that after a successful in-app purchase on the same device, StoreKit returns the transaction through [Product.PurchaseResult.success(_:)](<../product/purchaseresult/success(__).md>).

> [!important] Important
> Create a [Task](../../swift/task.md) to iterate through the transactions from the listener as soon as your app launches. If your app has unfinished transactions, the [updates](updates.md) listener receives them once, immediately after the app launches. Without the [Task](../../swift/task.md) to listen for these transactions, your app may miss them.

The following example shows a class that creates a [Task](../../swift/task.md) when it initializes. The task retrieves and processes any unfinished transactions.

```swift
final class TransactionObserver {
    
    var updates: Task<Void, Never>? = nil
    
    init() {
        updates = newTransactionListenerTask()
    }

    deinit {
        // Cancel the update handling task when you deinitialize the class.
        updates?.cancel()
    }
    
    private func newTransactionListenerTask() -> Task<Void, Never> {
        Task(priority: .background) {
            for await verificationResult in Transaction.updates {
                self.handle(updatedTransaction: verificationResult)
            }
        }
    }
    
    private func handle(updatedTransaction verificationResult: VerificationResult<Transaction>) {
        guard case .verified(let transaction) = verificationResult else {
            // Ignore unverified transactions.
            return
        }

        if let revocationDate = transaction.revocationDate {
            // Remove access to the product identified by transaction.productID.
            // Transaction.revocationReason provides details about
            // the revoked transaction.
            <#...#>
        } else if let expirationDate = transaction.expirationDate,
            expirationDate < Date() {
            // Do nothing, this subscription is expired.
            return
        } else if transaction.isUpgraded {
            // Do nothing, there is an active transaction
            // for a higher level of service.
            return
        } else {
            // Provide access to the product identified by
            // transaction.productID.
            <#...#>
        }
    }
    
}
```

The [updates](updates.md) listener receives unfinished transactions just once at app launch, but you can use the [unfinished](unfinished.md) listener to get your app’s unfinished transactions at any time. For information on finishing transactions, see [finish()](<finish().md>).

## See Also

### Related Documentation

- [Supporting offer codes in your app](../supporting-offer-codes-in-your-app.md) — Enable customers to redeem offer codes through the App Store or within your app.

### Transaction history and entitlements

- [Transaction](../transaction.md) — Information that represents the customer’s purchase of a product in your app.
- [all](all.md) — A sequence that emits all the customer’s transactions for your app.
- [currentEntitlements](currententitlements.md) — A sequence of the latest transactions that entitle a customer to In-App Purchases and subscriptions.
