---
title: 'currentEntitlements(for:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/transaction/currententitlements(for:)'
source_url: 'https://developer.apple.com/documentation/storekit/transaction/currententitlements(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/currententitlements%28for%3A%29.json'
content_hash: 'sha256:41b1a4d181beefe5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# currentEntitlements(for:)

<sub>Type Method</sub>

Gets the transactions that entitle the user to items purchased under a product ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func currentEntitlements(for productID: String) -> Transaction.Transactions
```

## Parameters

- `productID` — Identifies the product to check entitlements for.

## Return Value

A sequence containing all transactions that entitle the user to the product.

## Discussion

If a generic SKU is provided, the returned sequence will yield all transactions that entitle the user to Advanced Commerce Items purchased using the generic product’s ID.

If an ID for a regular IAP is provided, the returned sequence will contain no more than one transaction.

## See Also

### Deprecated

- [currentEntitlement(for:)](<currententitlement(for_).md>) — Gets the latest transactions that entitle the customer to a specified product. _(deprecated)_
- [offerPeriodStringRepresentation](offerperiodstringrepresentation.md) — The string representation of the offer period applied to the subscription offer for this transaction. _(deprecated)_
