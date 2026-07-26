---
title: subscriptionStatus
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/subscriptionstatus
source_url: 'https://developer.apple.com/documentation/storekit/transaction/subscriptionstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/subscriptionstatus.json'
content_hash: 'sha256:21ebfc3d7c3d0c43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# subscriptionStatus

<sub>Instance Property</sub>

An array that contains status information for a subscription group, including renewal and transaction information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0)
var subscriptionStatus: Product.SubscriptionInfo.Status? { get async }
```

## Discussion

This value is `nil` if the product in the transaction isn’t an auto-renewable subscription, specifically, if the [productType](producttype.md) is anything other than [autoRenewable](../product/producttype/autorenewable.md).

The array can have more than one subscription status, for example, if your subscription supports Family Sharing. Provide the customer with service for the subscription based on the highest level of service where the subscription status is [subscribed](../product/subscriptioninfo/renewalstate/subscribed.md).
