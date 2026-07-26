---
title: 'restoreCompletedTransactions(withApplicationUsername:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（18.0 起废弃）, iPadOS 7.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.9+（15.0 起废弃）, tvOS 7.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymentqueue/restorecompletedtransactions(withapplicationusername:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/restorecompletedtransactions(withapplicationusername:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/restorecompletedtransactions%28withapplicationusername%3A%29.json'
content_hash: 'sha256:ab286a0dfae8c93c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# restoreCompletedTransactions(withApplicationUsername:)

<sub>Instance Method</sub>

Asks the payment queue to restore previously completed purchases, providing an opaque identifier for the user’s account.

> [!warning] Deprecated
> Use AppStore.sync().

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func restoreCompletedTransactions(withApplicationUsername username: String?)
```

## Parameters

- `username` — An opaque identifier for the user’s account on your system.

## See Also

### Related Documentation

- [applicationUsername](../skpayment/applicationusername.md) — A string that associates the transaction with a user account on your service. _(deprecated)_

### Restoring Purchases

- [- restoreCompletedTransactions](<restorecompletedtransactions().md>) — Asks the payment queue to restore previously completed purchases. _(deprecated)_
