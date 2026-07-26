---
title: latestTransaction
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/advancedcommerceproduct/latesttransaction
source_url: 'https://developer.apple.com/documentation/storekit/advancedcommerceproduct/latesttransaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/advancedcommerceproduct/latesttransaction.json'
content_hash: 'sha256:343076715ba686ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AdvancedCommerceProduct](../advancedcommerceproduct.md)

# latestTransaction

<sub>Instance Property</sub>

The most recent transaction associated with the generic product ID, if it exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var latestTransaction: VerificationResult<Transaction>? { get async }
```

## Discussion

This value is `nil` if the customer hasn’t made any purchases associated with the generic product ID.

## See Also

### Getting transactions and entitlements

- [allTransactions](alltransactions.md) — All transactions associated with the generic product ID.
- [currentEntitlements](currententitlements.md) — The transactions that entitle the customer to Advanced Commerce Items purchased using the generic product ID.
