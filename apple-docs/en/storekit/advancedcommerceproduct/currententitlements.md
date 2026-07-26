---
title: currentEntitlements
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/advancedcommerceproduct/currententitlements
source_url: 'https://developer.apple.com/documentation/storekit/advancedcommerceproduct/currententitlements'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/advancedcommerceproduct/currententitlements.json'
content_hash: 'sha256:3cb622411af0f797'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AdvancedCommerceProduct](../advancedcommerceproduct.md)

# currentEntitlements

<sub>Instance Property</sub>

The transactions that entitle the customer to Advanced Commerce Items purchased using the generic product ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentEntitlements: Transaction.Transactions { get }
```

## See Also

### Getting transactions and entitlements

- [allTransactions](alltransactions.md) — All transactions associated with the generic product ID.
- [latestTransaction](latesttransaction.md) — The most recent transaction associated with the generic product ID, if it exists.
