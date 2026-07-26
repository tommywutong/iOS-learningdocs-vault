---
title: allTransactions
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/advancedcommerceproduct/alltransactions
source_url: 'https://developer.apple.com/documentation/storekit/advancedcommerceproduct/alltransactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/advancedcommerceproduct/alltransactions.json'
content_hash: 'sha256:0283bffaed79ca38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AdvancedCommerceProduct](../advancedcommerceproduct.md)

# allTransactions

<sub>Instance Property</sub>

All transactions associated with the generic product ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allTransactions: Transaction.Transactions { get }
```

## See Also

### Getting transactions and entitlements

- [currentEntitlements](currententitlements.md) — The transactions that entitle the customer to Advanced Commerce Items purchased using the generic product ID.
- [latestTransaction](latesttransaction.md) — The most recent transaction associated with the generic product ID, if it exists.
