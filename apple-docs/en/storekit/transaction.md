---
title: Transaction
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction
source_url: 'https://developer.apple.com/documentation/storekit/transaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction.json'
content_hash: 'sha256:ef408c2d27a2c486'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# Transaction

<sub>Structure</sub>

Information that represents the customer’s purchase of a product in your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Transaction
```

## Overview

A _transaction_ represents a successful In-App Purchase. The App Store generates a transaction each time a customer purchases an In-App Purchase product or renews a subscription. For each transaction that represents a current purchase, your app unlocks the purchased content or service and finishes the transaction.

Use the `Transaction` type to perform these transaction-related tasks:

- Get the customer’s transaction history, latest transactions, and current entitlements to unlock content and services.
- Access transaction properties.
- Finish a transaction after your app delivers the purchased content or service.
- Access the raw JSON Web Signature (JWS) string and supporting values to verify the transaction information.
- Listen for new transactions while the app is running.
- Begin a refund request from within your app.

### Access transaction history and current entitlements

Your app doesn’t create transaction objects. Instead, StoreKit automatically makes up-to-date transactions available to your app, including when someone launches the app for the first time.

> [!note] Related sessions from WWDC22
> Session 110404: [Implement proactive in-app purchase restore](https://developer.apple.com/videos/play/wwdc2022/110404/)

You access transactions in several ways:

- Get transaction history anytime by accessing the static [all](transaction/all.md) sequence, or get just the most recent transaction for a product with the [latestTransaction](product/latesttransaction.md) property of [Product](product.md).
- Receive notifications for new transactions while your app is running when customers complete a purchase outside of the app, including on another device, through the transaction listener, [updates](transaction/updates.md).
- Access the latest transaction for a subscription group through the subscription status API, using [transaction](product/subscriptioninfo/status-swift.struct/transaction.md).
- After a successful In-App Purchase, StoreKit returns the transaction through [Product.PurchaseResult.success(_:)](<product/purchaseresult/success(__).md>).

The most important use of transaction information is for determining which In-App Purchases the customer has paid access to, so your app can unlock the content or service. The [currentEntitlements](transaction/currententitlements.md) API provides the information you need to unlock all of the customer’s paid content in your app. Use `currentEntitlements` to get a list of transactions for all the products the customer is currently entitled to, including non-consumable In-App Purchases and currently active subscriptions.

### Verify transactions

The App Store cryptographically signs transaction information in JWS format. StoreKit automatically validates and returns the signed information, wrapped in a [VerificationResult](verificationresult.md). When the `VerificationResult` wraps a `Transaction` value, it provides the raw JWS string in the [jwsRepresentation](verificationresult/jwsrepresentation-21vgo.md) property. If you get a transaction through [VerificationResult.verified(_:)](<verificationresult/verified(__).md>), the information passed validation. If you get it through [VerificationResult.unverified(_:_:)](<verificationresult/unverified(____).md>), the information didn’t pass StoreKit’s automatic validation. Your app can immediately access the transaction information in the [Transaction properties](transaction-properties.md).

To perform your own validation on the device, use the verification result’s [jwsRepresentation](verificationresult/jwsrepresentation-21vgo.md) string, and use the provided convenience properties [headerData](verificationresult/headerdata-9egfp.md), [payloadData](verificationresult/payloaddata-uyle.md), and [signatureData](verificationresult/signaturedata-4pyv8.md). For added control and security, send the `jwsRepresentation` to your server to verify. Consider using the App Store Server Library to implement your verification. The library provides the functions `verifyAndDecodeTransaction` and `verifyAndDecodeRenewalInfo` in each language the library supports. For more information, see [Simplifying your implementation by using the App Store Server Library](../appstoreserverapi/simplifying-your-implementation-by-using-the-app-store-server-library.md).

> [!tip] Tip
> The [jwsRepresentation](verificationresult/jwsrepresentation-21vgo.md) is the same as the [JWSTransaction](../appstoreserverapi/jwstransaction.md) that the [App Store Server API](../appstoreserverapi.md) returns and to the [JWSTransaction](../appstoreservernotifications/jwstransaction.md) that you receive in [App Store Server Notifications V2](../appstoreservernotifications/app-store-server-notifications-v2.md). You can validate them on your server in the same way.

If StoreKit returns a transaction as verified, the transaction is valid for the device. For information about performing your own verification for a device, see [deviceVerification](transaction/deviceverification.md).

For more information about JWS, see the [IETF RFC 7515](https://datatracker.ietf.org/doc/html/rfc7515) specification.

### Access purchases made with the original API

All In-App Purchases that customers make are equally available to your app in this `Transaction` API, and in receipts using the [Original API for In-App Purchase](original-api-for-in-app-purchase.md), as follows:

- New purchases that customers make with the original API are available immediately using the `Transaction` API.
- Purchases that customers make with the [purchase(options:)](<product/purchase(options_).md>) method are available in the original API when your app refreshes the receipt. For more information, see [SKReceiptRefreshRequest](skreceiptrefreshrequest.md).

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Identifiable](../swift/identifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Transaction properties

- [Transaction properties](transaction-properties.md) — The properties of a transaction, including identifiers, purchase and revocation dates and details, status, and offer details.
- [appTransactionID](transaction/apptransactionid.md) — The unique identifier of the app download transaction.

### Monitoring transaction-related changes

- [updates](transaction/updates.md) — The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.
- [Transactions](transaction/transactions.md) — An asynchronous sequence of transactions.

### Getting transaction history

- [latest(for:)](<transaction/latest(for_).md>) — Gets the customer’s most recent transaction for an In-App Purchase.
- [all](transaction/all.md) — A sequence that emits all the customer’s transactions for your app.
- [unfinished](transaction/unfinished.md) — A sequence that emits unfinished transactions for the customer.
- [SKIncludeConsumableInAppPurchaseHistory](../bundleresources/information-property-list/skincludeconsumableinapppurchasehistory.md) — A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.

### Getting current entitlements

- [currentEntitlements](transaction/currententitlements.md) — A sequence of the latest transactions that entitle a customer to In-App Purchases and subscriptions.

### Getting transactions for a product

- [all(for:)](<transaction/all(for_).md>) — Gets all the transactions associated with this product ID.

### Finishing the transaction

- [finish()](<transaction/finish().md>) — Indicates to the App Store that the app delivered the purchased content or enabled the service to finish the transaction.
- [unfinished](transaction/unfinished.md) — A sequence that emits unfinished transactions for the customer.

### Verifying transactions

- [deviceVerification](transaction/deviceverification.md) — The device verification value you use to verify whether the transaction belongs to the device.
- [deviceVerificationNonce](transaction/deviceverificationnonce.md) — The UUID for computing the device verification value.
- [signedDate](transaction/signeddate.md) — The date that the App Store signed the JWS transaction.

### Getting transaction info in JSON format

- [jsonRepresentation](transaction/jsonrepresentation.md) — The JSON representation of the transaction information.

### Requesting refunds

- [Testing refund requests](testing-refund-requests.md) — Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.
- [beginRefundRequest(in:)](<transaction/beginrefundrequest(in_)-9k0pj.md>) — Presents the refund request sheet for the transaction in a window scene.
- [beginRefundRequest(in:)](<transaction/beginrefundrequest(in_)-63bvd.md>) — Presents the refund request sheet for the transaction in a view controller.
- [beginRefundRequest(for:in:)](<transaction/beginrefundrequest(for_in_)-65tph.md>) — Presents the refund request sheet for the specified transaction in a window scene.
- [beginRefundRequest(for:in:)](<transaction/beginrefundrequest(for_in_)-9mscy.md>) — Presents the refund request sheet for the specified transaction in a view controller.
- [RefundRequestError](transaction/refundrequesterror.md) — The error codes for refund requests.
- [RefundRequestStatus](transaction/refundrequeststatus.md) — The status codes for refund requests.

### Advanced Commerce transaction data

- [advancedCommerceInfo](transaction/advancedcommerceinfo-swift.property.md) — Metadata for transactions that use the Advanced Commerce API.
- [AdvancedCommerceInfo](transaction/advancedcommerceinfo-swift.struct.md) — Metadata for transactions that use the Advanced Commerce API.

### Getting offer types

- [OfferType](transaction/offertype-swift.struct.md) — The types of offers that apply to a transaction.

### Deprecated

- [currentEntitlement(for:)](<transaction/currententitlement(for_).md>) — Gets the latest transactions that entitle the customer to a specified product. _(deprecated)_
- [currentEntitlements(for:)](<transaction/currententitlements(for_).md>) — Gets the transactions that entitle the user to items purchased under a product ID.
- [offerPeriodStringRepresentation](transaction/offerperiodstringrepresentation.md) — The string representation of the offer period applied to the subscription offer for this transaction. _(deprecated)_

### Structures

- [CommitmentInfo](transaction/commitmentinfo-swift.struct.md)
- [RevocationType](transaction/revocationtype-swift.struct.md)

### Instance Properties

- [billingPlanType](transaction/billingplantype.md)
- [bundleOriginalTransactionID](transaction/bundleoriginaltransactionid.md)
- [bundleProductID](transaction/bundleproductid.md) — Identifies the bundle product the transaction is for. If this transaction is created as a result of a subscription bundle purchase or renewal, this field will be populated with the product ID of the bundle.
- [bundleSubscriptionGroupID](transaction/bundlesubscriptiongroupid.md) — Identifies the subscription bundle group the transaction is for.
- [bundleTransactionID](transaction/bundletransactionid.md)
- [commitmentInfo](transaction/commitmentinfo-swift.property.md)
- [previousOriginalTransactionID](transaction/previousoriginaltransactionid.md) — The original transaction ID of the subscription this one replaced when a customer switched between a standalone auto-renewable subscription and a subscription bundle (in either direction).
- [revocationPercentage](transaction/revocationpercentage.md) — The percentage of the transaction amount that the App Store has refunded or revoked, expressed as a decimal.
- [revocationType](transaction/revocationtype-swift.property.md) — The type of refund or revocation that applies to the transaction.
- [revocationTypeStringRepresentation](transaction/revocationtypestringrepresentation.md) — The string representation of the [revocationType](transaction/revocationtype-swift.property.md), or `nil` if the transaction was not revoked. _(deprecated)_

## See Also

### Transaction history and entitlements

- [updates](transaction/updates.md) — The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.
- [all](transaction/all.md) — A sequence that emits all the customer’s transactions for your app.
- [currentEntitlements](transaction/currententitlements.md) — A sequence of the latest transactions that entitle a customer to In-App Purchases and subscriptions.
