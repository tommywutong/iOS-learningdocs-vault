---
title: applicationUsername
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（18.0 起废弃）, iPadOS 7.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.9+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skmutablepayment/applicationusername
source_url: 'https://developer.apple.com/documentation/storekit/skmutablepayment/applicationusername'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skmutablepayment/applicationusername.json'
content_hash: 'sha256:1c4ef580ae55a42e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKMutablePayment](../skmutablepayment.md)

# applicationUsername

<sub>Instance Property</sub>

A string that associates the transaction with a user account on your service.

> [!warning] Deprecated
> Create a Product.PurchaseOption.appAccountToken to use in Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var applicationUsername: String? { get set }
```

## Discussion

Consider assigning a UUID to the [applicationUsername](applicationusername.md) property. When this value is a UUID, the App Store server stores it as an [appAccountToken](../transaction/appaccounttoken.md). In this scenario, the following happens:

- In the [App Store Server API](../../appstoreserverapi.md), the [JWSTransactionDecodedPayload](../../appstoreserverapi/jwstransactiondecodedpayload.md) object returns the [applicationUsername](applicationusername.md) value in the [appAccountToken](../../appstoreserverapi/appaccounttoken.md) field.
- In [App Store Server Notifications](../../appstoreservernotifications.md), the [JWSTransactionDecodedPayload](../../appstoreservernotifications/jwstransactiondecodedpayload.md) object returns the [applicationUsername](applicationusername.md) value in the [appAccountToken](../../appstoreservernotifications/appaccounttoken.md) field.
- When you call the [verifyReceipt](../../appstorereceipts/verify-receipt.md) endpoint to verify an App Store receipt, the App Store server returns the [applicationUsername](applicationusername.md) value in the [app_account_token](../../appstorereceipts/app_account_token.md) field of the [responseBody.Latest_receipt_info](../../appstorereceipts/responsebody/latest_receipt_info-data.dictionary.md).

The sample code below shows how to assign a UUID value to [applicationUsername](applicationusername.md). You may choose to generate the UUID on your server. Assign the value before adding the payment to the payment queue.

**Swift**

```swift
let payment = SKMutablePayment(product: product)
payment.applicationUsername = uuidString

SKPaymentQueue.default().add(payment)
```

**Objective-C**

```objc
SKMutablePayment *payment = [SKMutablePayment paymentWithProduct:product];
payment.applicationUsername = uuidString;

[[SKPaymentQueue defaultQueue] addPayment:payment];
```

If you don’t assign a UUID string value to [applicationUsername](applicationusername.md), the App Store server doesn’t persist the value. The value won’t appear in the [app_account_token](../../appstorereceipts/app_account_token.md) fields in notifications or receipts.

> [!important] Important
> An [applicationUsername](applicationusername.md) property that isn’t a UUID isn’t guaranteed to persist between the time when you add the payment transaction to the queue and when the queue updates the transaction.

## See Also

### Getting and Setting Attributes

- [productIdentifier](productidentifier.md) — A string that identifies a product that can be purchased from within your app. _(deprecated)_
- [quantity](quantity.md) — The number of items the user wants to purchase. _(deprecated)_
- [requestData](requestdata.md) — Reserved for future use. _(deprecated)_
