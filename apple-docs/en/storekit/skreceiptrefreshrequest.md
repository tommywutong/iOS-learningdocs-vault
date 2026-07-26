---
title: SKReceiptRefreshRequest
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+（18.0 起废弃）, iPadOS 7.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.9+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skreceiptrefreshrequest
source_url: 'https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skreceiptrefreshrequest.json'
content_hash: 'sha256:e291ce32b2b0f37c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKReceiptRefreshRequest

<sub>Class</sub>

A request to the App Store to get the app receipt, which represents the customer’s transactions with your app.

> [!warning] Deprecated
> Use Transaction.all and AppTransaction.shared.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SKReceiptRefreshRequest
```

## Overview

> [!note] Note
> The receipt isn’t necessary if you use [AppTransaction](apptransaction.md) to validate the app download, or [Transaction](transaction.md) to validate in-app purchases. Only use the receipt if your app uses the [Original API for In-App Purchase](original-api-for-in-app-purchase.md), or needs the receipt to validate the app download because it can’t use [AppTransaction](apptransaction.md).

Use this API to request a new app receipt from the App Store if the receipt is invalid or missing from its expected location, [appStoreReceiptURL](../foundation/bundle/appstorereceipturl.md). To request the receipt using the [SKReceiptRefreshRequest](skreceiptrefreshrequest.md) object, you initialize it, attach a [delegate](skrequest/delegate.md), and then call the request’s [- start](<skrequest/start().md>) method.

> [!important] Important
> The receipt refresh request displays a system prompt that asks users to authenticate with their App Store credentials. For a better user experience, initiate the request after an explicit user action, like tapping or clicking a button.

When the request completes successfully, your delegate receives an [SKReceiptRefreshRequest](skreceiptrefreshrequest.md) object in its [- requestDidFinish:](<skrequestdelegate/requestdidfinish(__).md>) method. Locate the app receipt using the [appStoreReceiptURL](../foundation/bundle/appstorereceipturl.md) property. For information about validating the receipt, see [Choosing a receipt validation technique](choosing-a-receipt-validation-technique.md).

If the request fails and calls your delegate’s [- request:didFailWithError:](<skrequestdelegate/request(__didfailwitherror_).md>) method, your app needs to release the request and not attempt to call it a second time. Requests can fail when a user doesn’t authenticate or chooses to cancel the request. Without a validated receipt, assume the user doesn’t have access to premium content.

In the sandbox environment, you can initialize a receipt with any combination of properties for testing when you call [- initWithReceiptProperties:](<skreceiptrefreshrequest/init(receiptproperties_).md>).

### Use alternative techniques

There are times when using [SKReceiptRefreshRequest](skreceiptrefreshrequest.md) isn’t necessary, so avoid doing so, such as in the following scenarios:

- If the receipt is valid, but may be missing transactions, use [- restoreCompletedTransactions](<skpaymentqueue/restorecompletedtransactions().md>) instead. For example, the receipt may be missing a transaction if a person purchases a new subscription on another device.
- In the sandbox environment, before the tester completes their first in-app purchase. Receipts are initially absent in the sandbox environment for iOS and iPadOS apps. For more information, see [appStoreReceiptURL](../foundation/bundle/appstorereceipturl.md).

## Relationships

- **Inherits From**: [SKRequest](skrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing Receipt Refresh Requests

- [- initWithReceiptProperties:](<skreceiptrefreshrequest/init(receiptproperties_).md>) — Creates a receipt refresh request with optional properties. _(deprecated)_

### Receipt Properties and Keys

- [receiptProperties](skreceiptrefreshrequest/receiptproperties.md) — The properties of the receipt. _(deprecated)_
- [SKReceiptPropertyIsExpired](skreceiptpropertyisexpired.md) — A key with a value that indicates whether the receipt is in an expired state. _(deprecated)_
- [SKReceiptPropertyIsRevoked](skreceiptpropertyisrevoked.md) — A key with a value that indicates whether the receipt is in a revoked state. _(deprecated)_
- [SKReceiptPropertyIsVolumePurchase](skreceiptpropertyisvolumepurchase.md) — A key with a value that indicates whether the receipt is a Volume Purchase Plan receipt. _(deprecated)_

## See Also

### Purchase validation

- [Choosing a receipt validation technique](choosing-a-receipt-validation-technique.md) — Select the type of receipt validation, on the device or on your server, that works for your app.
- [Validating receipts with the App Store](validating-receipts-with-the-app-store.md) — Verify transactions with the App Store on a secure server.
- [appStoreReceiptURL](../foundation/bundle/appstorereceipturl.md) — The file URL for the bundle’s App Store receipt. _(deprecated)_
