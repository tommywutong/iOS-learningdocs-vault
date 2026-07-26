---
title: SKProductsRequestDelegate
framework: StoreKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductsrequestdelegate
source_url: 'https://developer.apple.com/documentation/storekit/skproductsrequestdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductsrequestdelegate.json'
content_hash: 'sha256:5ed99de7d8af3a8d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKProductsRequestDelegate

<sub>Protocol</sub>

A set of methods the delegate implements so it receives the product information your app requests.

> [!warning] Deprecated
> Get products using Product.products(for:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SKProductsRequestDelegate : SKRequestDelegate
```

## Overview

The [SKProductsRequestDelegate](skproductsrequestdelegate.md) protocol declares methods that are implemented by the delegate of an [SKProductsRequest](skproductsrequest.md) object. The delegate receives the product information that the product request referred to. Your app uses this information when presenting products to users in its in-app store.

> [!warning] Warning
> Responses received by the `SKProductsRequestDelegate` may not be returned on a specific thread. If you make assumptions about which queue will handle delegate responses, you may encounter unintended performance and compatibility issues in the future.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [SKRequestDelegate](skrequestdelegate.md)

## Topics

### Receiving the Response

- [- productsRequest:didReceiveResponse:](<skproductsrequestdelegate/productsrequest(__didreceive_).md>) — Accepts the App Store response that contains the app-requested product information. _(deprecated)_

## See Also

### Setting the Delegate

- [delegate](skproductsrequest/delegate.md) — The delegate that receives the response of the app’s products request. _(deprecated)_
