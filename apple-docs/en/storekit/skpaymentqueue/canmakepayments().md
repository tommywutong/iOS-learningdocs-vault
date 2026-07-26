---
title: canMakePayments()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentqueue/canmakepayments()
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/canmakepayments()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/canmakepayments%28%29.json'
content_hash: 'sha256:b25dd9a20165ed78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# canMakePayments()

<sub>Type Method</sub>

A method that indicates whether the person can make purchases.

> [!warning] Deprecated
> Use AppStore.canMakePayments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func canMakePayments() -> Bool
```

## Discussion

The Boolean value that this method returns is identical to the value of the type property [canMakePayments](../appstore/canmakepayments.md) in the [AppStore](../appstore.md) object. For more information about using and interpreting this value, see the type property page [canMakePayments](../appstore/canmakepayments.md).
