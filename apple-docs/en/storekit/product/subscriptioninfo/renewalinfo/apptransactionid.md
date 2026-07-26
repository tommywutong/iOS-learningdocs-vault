---
title: appTransactionID
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/apptransactionid
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/apptransactionid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/apptransactionid.json'
content_hash: 'sha256:e5a7af93787bc0d5'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# appTransactionID

<sub>Instance Property</sub>

The unique identifier of the app download transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 18.4, macOS 15.4, tvOS 18.4, watchOS 11.4, visionOS 2.4)
var appTransactionID: String { get }
```

## Discussion

The App Store server APIs and StoreKit provide this value in several APIs. For more information, see [appTransactionID](../../../apptransaction/apptransactionid.md) in [AppTransaction](../../../apptransaction.md).

## See Also

### Identifying the account

- [appAccountToken](appaccounttoken.md) — The app account token you provided during the subscription purchase, if one exists.
