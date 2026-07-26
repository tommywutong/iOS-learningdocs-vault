---
title: 'paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:didrevokeentitlementsforproductidentifiers:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:didrevokeentitlementsforproductidentifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransactionobserver/paymentqueue%28_%3Adidrevokeentitlementsforproductidentifiers%3A%29.json'
content_hash: 'sha256:70fc9def48a78913'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransactionObserver](../skpaymenttransactionobserver.md)

# paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)

<sub>Instance Method</sub>

Tells an observer that the customer is no longer entitled to one or more Family Sharing purchases.

> [!warning] Deprecated
> Use Transaction.updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func paymentQueue(_ queue: SKPaymentQueue, didRevokeEntitlementsForProductIdentifiers productIdentifiers: [String])
```

## Parameters

- `queue` — The payment queue that calls the delegate method.

- `productIdentifiers` — The list of product identifiers with revoked entitlements.

## Discussion

The system calls this delegate method whenever App Store revokes in-app purchases for a family member based on changes in Family Sharing, or when the purchaser gets a refund for an in-app purchase. Implement this method in your payment queue observer to reestablish a user’s access to products. Revoked transactions have the `cancellation_date` populated in the receipt.

For products with Family Sharing enabled, the following conditions may trigger this method in the family member’s app:

- The purchaser receives a refund for a non-consumable or an auto-renewable subscription they shared.
- The purchaser leaves the family group in which they were sharing subscriptions or non-consumables.
- The purchaser disables Family Sharing for a non-consumable or stops sharing a subscription.
- The purchaser hides an app, which makes their non-consumable purchase unavailable for sharing.
- The family member leaves the group and no longer gets access to shared purchases.
- The family organizer stops sharing payment in iCloud family settings. This change affects non-consumables.

By leaving a family group, or disabling sharing in any of the ways listed above, family members are no longer entitled to family-shared purchases. The `productIdentifiers` parameter contains the revoked product IDs. Your app needs to check the receipt on the device, which the system automatically updates prior to calling this method, and provide the correct level of access for the in-app purchases.

If you receive [App Store Server Notifications](../../appstoreservernotifications.md), your server receives a [notificationType](../../appstoreservernotifications/notificationtype.md) `REVOKE` for the family member when the conditions listed above occur.

> [!important] Important
> Always check the receipt to determine the users’s correct level of access for the product. A user may lose access through Family Sharing, but may have purchased the product directly.

StoreKit also calls this method in the purchaser’s app when the purchaser receives a refund for a non-consumable or an auto-renewable subscription, regardless if the product is shared with the family. If you receive [App Store Server Notifications](../../appstoreservernotifications.md), your server receives a [notificationType](../../appstoreservernotifications/notificationtype.md) `REFUND` for the purchaser.

If you use server-side receipt validation with the App Store, call your server to reprocess the receipt and update your purchase records.

## See Also

### Family Sharing

- [Supporting Family Sharing in your app](../supporting-family-sharing-in-your-app.md) — Provide service to share subscriptions and non-consumable products to family members.
- [isFamilyShareable](../skproduct/isfamilyshareable.md) — A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect. _(deprecated)_
