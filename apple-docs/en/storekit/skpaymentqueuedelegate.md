---
title: SKPaymentQueueDelegate
framework: StoreKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+（18.0 起废弃）, iPadOS 13.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.15+（15.0 起废弃）, tvOS 13.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentqueuedelegate
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueuedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueuedelegate.json'
content_hash: 'sha256:1a91f659b40dfc86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKPaymentQueueDelegate

<sub>Protocol</sub>

The protocol that provides information needed to complete transactions.

> [!warning] Deprecated
> No longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SKPaymentQueueDelegate : NSObjectProtocol
```

## Overview

This protocol includes a method that lets your app determine whether to continue a transaction if the customer’s App Store storefront changes.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Continuing transactions

- [- paymentQueue:shouldContinueTransaction:inStorefront:](<skpaymentqueuedelegate/paymentqueue(__shouldcontinue_in_).md>) — Asks the delegate whether to continue the transaction if the device’s App Store storefront changes during a transaction. _(deprecated)_

### Showing price consent

- [- paymentQueueShouldShowPriceConsent:](<skpaymentqueuedelegate/paymentqueueshouldshowpriceconsent(__).md>) — Asks the delegate whether to immediately display a price consent sheet. _(deprecated)_

## See Also

### Essentials

- [Setting up the transaction observer for the payment queue](setting-up-the-transaction-observer-for-the-payment-queue.md) — Enable your app to receive and handle transactions by adding an observer.
- [Offering, completing, and restoring in-app purchases](offering-completing-and-restoring-in-app-purchases.md) — Fetch, display, purchase, validate, and finish transactions in your app.
- [SKPaymentQueue](skpaymentqueue.md) — A queue of payment transactions for the App Store to process. _(deprecated)_
- [SKPaymentTransactionObserver](skpaymenttransactionobserver.md) — A set of methods that process transactions, unlock purchased functionality, and continue promoted In-App Purchases. _(deprecated)_
- [SKRequest](skrequest.md) — An abstract class that represents a request to the App Store. _(deprecated)_
