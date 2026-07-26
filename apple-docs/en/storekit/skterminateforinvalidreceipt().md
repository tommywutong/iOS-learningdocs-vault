---
title: SKTerminateForInvalidReceipt()
framework: StoreKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.1+, iPadOS 7.1+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 6.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skterminateforinvalidreceipt()
source_url: 'https://developer.apple.com/documentation/storekit/skterminateforinvalidreceipt()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skterminateforinvalidreceipt%28%29.json'
content_hash: 'sha256:b6cc01a665e7e6d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKTerminateForInvalidReceipt()

<sub>Function</sub>

Terminates an app if the license to use the app has expired.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SKTerminateForInvalidReceipt()
```

## See Also

### Providing access to previously purchased products

- [Restoring purchased products](restoring-purchased-products.md) — Give customers functionality that restores their purchases in your app to maintain access to purchased content.
- [SKReceiptRefreshRequest](skreceiptrefreshrequest.md) — A request to the App Store to get the app receipt, which represents the customer’s transactions with your app. _(deprecated)_
- [SKRequest](skrequest.md) — An abstract class that represents a request to the App Store. _(deprecated)_
- [SKPaymentTransaction](skpaymenttransaction.md) — An object in the payment queue. _(deprecated)_
