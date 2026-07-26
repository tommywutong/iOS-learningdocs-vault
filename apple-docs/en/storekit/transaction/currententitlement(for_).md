---
title: 'currentEntitlement(for:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+（18.4 起废弃）, iPadOS 15.0+（18.4 起废弃）, macOS 12.0+（15.4 起废弃）, tvOS 15.0+（18.4 起废弃）, visionOS 1.0+（2.4 起废弃）, watchOS 8.0+（11.4 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/storekit/transaction/currententitlement(for:)'
source_url: 'https://developer.apple.com/documentation/storekit/transaction/currententitlement(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/currententitlement%28for%3A%29.json'
content_hash: 'sha256:6214394715deebd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# currentEntitlement(for:)

<sub>Type Method</sub>

Gets the latest transactions that entitle the customer to a specified product.

> [!warning] Deprecated
> Use [currentEntitlements](currententitlements.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func currentEntitlement(for productID: String) async -> VerificationResult<Transaction>?
```

## Parameters

- `productID` — In-App Purchase product identifier.

## Return Value

A [VerificationResult](../verificationresult.md) or `nil` if the customer has no current In-App Purchases.

## See Also

### Deprecated

- [currentEntitlements(for:)](<currententitlements(for_).md>) — Gets the transactions that entitle the user to items purchased under a product ID.
- [offerPeriodStringRepresentation](offerperiodstringrepresentation.md) — The string representation of the offer period applied to the subscription offer for this transaction. _(deprecated)_
