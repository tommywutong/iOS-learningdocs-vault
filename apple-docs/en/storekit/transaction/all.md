---
title: all
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/all
source_url: 'https://developer.apple.com/documentation/storekit/transaction/all'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/all.json'
content_hash: 'sha256:fecb93414cf14f03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# all

<sub>Type Property</sub>

A sequence that emits all the customer’s transactions for your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var all: Transaction.Transactions { get }
```

## Discussion

This sequence returns the customer’s transaction history current to the moment you access it. The sequence emits a finite number of transactions. If the App Store processes additional transactions for the customer while you’re accessing this sequence, they appear in the transaction listener [updates](updates.md).

The transaction history includes the following in-app purchases:

- Unfinished consumables
- Finished consumables that are refunded or revoked
- Non-consumables
- Auto-renewable subscriptions, including all renewals
- Auto-renewable subscriptions and non-consumables that the customer gets through Family Sharing

By default, when the [SKIncludeConsumableInAppPurchaseHistory](../../bundleresources/information-property-list/skincludeconsumableinapppurchasehistory.md) property list key is `false`, the transaction information excludes finished consumables (unless refunded or revoked).

To get all possible transactions, including all finished consumables, set the [SKIncludeConsumableInAppPurchaseHistory](../../bundleresources/information-property-list/skincludeconsumableinapppurchasehistory.md) property list key to `true`.

## See Also

### Transaction history and entitlements

- [Transaction](../transaction.md) — Information that represents the customer’s purchase of a product in your app.
- [updates](updates.md) — The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.
- [currentEntitlements](currententitlements.md) — A sequence of the latest transactions that entitle a customer to In-App Purchases and subscriptions.
