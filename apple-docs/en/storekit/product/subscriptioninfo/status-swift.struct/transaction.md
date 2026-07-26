---
title: transaction
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/status-swift.struct/transaction
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct/transaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/status-swift.struct/transaction.json'
content_hash: 'sha256:0dea119573de5570'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [Status](../status-swift.struct.md)

# transaction

<sub>Instance Property</sub>

The latest transaction for the subscription group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let transaction: VerificationResult<Transaction>
```

## See Also

### Getting subscription status information

- [state](state.md) — The renewal state of the auto-renewable subscription.
- [renewalInfo](renewalinfo.md) — The signed renewal information for the auto-renewable subscription.
- [RenewalInfo](../renewalinfo.md) — The renewal information for an auto-renewable subscription.
- [RenewalState](../renewalstate.md) — The renewal states of auto-renewable subscriptions.
