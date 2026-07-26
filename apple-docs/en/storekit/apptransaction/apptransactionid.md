---
title: appTransactionID
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction/apptransactionid
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/apptransactionid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/apptransactionid.json'
content_hash: 'sha256:192d9cece822b6f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# appTransactionID

<sub>Instance Property</sub>

The unique identifier of the app download transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 18.4, macOS 15.4, tvOS 18.4, watchOS 11.4, visionOS 2.4)
var appTransactionID: String { get }
```

## Discussion

The App Store generates a single, globally unique `appTransactionID` for each Apple Account that downloads your app and for each family group member for apps that support Family Sharing.

This value remains the same for the same Apple Account and app if the customer redownloads the app on any device, receives a refund, repurchases the app, or changes the storefront. For apps that support Family Sharing, the `appTransactionID` is unique for each family group member.

The `appTransactionID` is available even if a customer makes no in-app purchases.

The App Store server and StoreKit provide the `appTransactionID` in the following APIs:

- This symbol, `appTransactionID`, in the [AppTransaction](../apptransaction.md) object
- [appTransactionID](../product/subscriptioninfo/renewalinfo/apptransactionid.md), in the subscription renewal information [RenewalInfo](../product/subscriptioninfo/renewalinfo.md)
- [appTransactionID](../transaction/apptransactionid.md), in the transaction information [Transaction](../transaction.md)
- In transaction and subscription renewal information you receive from notifications, [App Store Server Notifications V2](../../appstoreservernotifications/app-store-server-notifications-v2.md)
- In transaction and subscription renewal information you receive from the [App Store Server API](../../appstoreserverapi.md)
