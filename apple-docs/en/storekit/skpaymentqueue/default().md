---
title: default()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentqueue/default()
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/default()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/default%28%29.json'
content_hash: 'sha256:0a1254f6928ecd46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# default()

<sub>Type Method</sub>

Returns the default payment queue instance.

> [!warning] Deprecated
> No longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func `default`() -> Self
```

## Return Value

The default payment queue.

## Discussion

Apps do not create a payment queue. Instead, they retrieve the  queue by calling this class method.

### Special Considerations

The payment queue is not available in Simulator. Attempting to retrieve the payment queue logs a warning.
