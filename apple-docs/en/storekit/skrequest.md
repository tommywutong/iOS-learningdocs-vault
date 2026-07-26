---
title: SKRequest
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skrequest
source_url: 'https://developer.apple.com/documentation/storekit/skrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skrequest.json'
content_hash: 'sha256:86a1be780434db4b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKRequest

<sub>Class</sub>

An abstract class that represents a request to the App Store.

> [!warning] Deprecated
> No longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SKRequest
```

## Overview

To make a request, initialize a subclass of [SKRequest](skrequest.md)—such as [SKProductsRequest](skproductsrequest.md) or [SKReceiptRefreshRequest](skreceiptrefreshrequest.md)—set the [delegate](skrequest/delegate.md) property, and call the [- start](<skrequest/start().md>) method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [SKProductsRequest](skproductsrequest.md), [SKReceiptRefreshRequest](skreceiptrefreshrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Controlling the Request

- [- start](<skrequest/start().md>) — Sends the request to the Apple App Store. _(deprecated)_
- [- cancel](<skrequest/cancel().md>) — Cancels a previously started request. _(deprecated)_

### Accessing the Delegate

- [delegate](skrequest/delegate.md) — The delegate of the request object. _(deprecated)_
- [SKRequestDelegate](skrequestdelegate.md) — Common methods that are implemented by delegates for any subclass of the `SKRequest` abstract class. _(deprecated)_

## See Also

### Essentials

- [Setting up the transaction observer for the payment queue](setting-up-the-transaction-observer-for-the-payment-queue.md) — Enable your app to receive and handle transactions by adding an observer.
- [Offering, completing, and restoring in-app purchases](offering-completing-and-restoring-in-app-purchases.md) — Fetch, display, purchase, validate, and finish transactions in your app.
- [SKPaymentQueue](skpaymentqueue.md) — A queue of payment transactions for the App Store to process. _(deprecated)_
- [SKPaymentTransactionObserver](skpaymenttransactionobserver.md) — A set of methods that process transactions, unlock purchased functionality, and continue promoted In-App Purchases. _(deprecated)_
- [SKPaymentQueueDelegate](skpaymentqueuedelegate.md) — The protocol that provides information needed to complete transactions. _(deprecated)_
