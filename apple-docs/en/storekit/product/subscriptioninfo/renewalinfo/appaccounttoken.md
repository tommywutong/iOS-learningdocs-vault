---
title: appAccountToken
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/appaccounttoken
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/appaccounttoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/appaccounttoken.json'
content_hash: 'sha256:631ff2308e53ac90'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# appAccountToken

<sub>Instance Property</sub>

The app account token you provided during the subscription purchase, if one exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 18.4, macOS 15.4, tvOS 18.4, watchOS 11.4, visionOS 2.4)
var appAccountToken: UUID? { get }
```

## Discussion

If you include an app account token in the purchase options when the customer purchases or changes the subscription,  this property is the app account token you provide. If you don’t provide an app account token, this property is `nil`.

## See Also

### Identifying the account

- [appTransactionID](apptransactionid.md) — The unique identifier of the app download transaction.
