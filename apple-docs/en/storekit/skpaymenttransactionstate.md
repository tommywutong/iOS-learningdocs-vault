---
title: SKPaymentTransactionState
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymenttransactionstate
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransactionstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransactionstate.json'
content_hash: 'sha256:a7a24a5558e2ed03'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKPaymentTransactionState

<sub>Enumeration</sub>

Values representing the state of a transaction.

> [!warning] Deprecated
> Use PurchaseResult from Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum SKPaymentTransactionState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [SKPaymentTransactionStatePurchasing](skpaymenttransactionstate/purchasing.md) — A transaction that is being processed by the App Store. _(deprecated)_
- [SKPaymentTransactionStatePurchased](skpaymenttransactionstate/purchased.md) — A successfully processed transaction. _(deprecated)_
- [SKPaymentTransactionStateFailed](skpaymenttransactionstate/failed.md) — A failed transaction. _(deprecated)_
- [SKPaymentTransactionStateRestored](skpaymenttransactionstate/restored.md) — A transaction that restores content previously purchased by the user. _(deprecated)_
- [SKPaymentTransactionStateDeferred](skpaymenttransactionstate/deferred.md) — A transaction that is in the queue, but its final status is pending external action such as Ask to Buy. _(deprecated)_

### Initializers

- [init(rawValue:)](<skpaymenttransactionstate/init(rawvalue_).md>) _(deprecated)_

## See Also

### Getting Transaction State

- [transactionState](skpaymenttransaction/transactionstate.md) — The current state of the transaction. _(deprecated)_
