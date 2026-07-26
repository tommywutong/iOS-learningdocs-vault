---
title: SKProductsRequest
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductsrequest
source_url: 'https://developer.apple.com/documentation/storekit/skproductsrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductsrequest.json'
content_hash: 'sha256:bf6367154bb831a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKProductsRequest

<sub>Class</sub>

An object that can retrieve localized information from the App Store about a specified list of products.

> [!warning] Deprecated
> Use Product.products(for:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SKProductsRequest
```

## Overview

Your app uses an [SKProductsRequest](skproductsrequest.md) object to present localized prices and other information to the user without having to maintain that list of product information itself.

To use an [SKProductsRequest](skproductsrequest.md) object, you initialize it with a list of product identifier strings, attach a delegate, and then call the request’s [- start](<skrequest/start().md>) method. When the request completes, your delegate receives an [SKProductsResponse](skproductsresponse.md) object.

> [!note] Note
> Be sure to keep a strong reference to the request object; otherwise, the system might deallocate the request before it can complete.

## Relationships

- **Inherits From**: [SKRequest](skrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a Products Request

- [- initWithProductIdentifiers:](<skproductsrequest/init(productidentifiers_).md>) — Initializes the request with the set of product identifiers. _(deprecated)_

### Setting the Delegate

- [delegate](skproductsrequest/delegate.md) — The delegate that receives the response of the app’s products request. _(deprecated)_
- [SKProductsRequestDelegate](skproductsrequestdelegate.md) — A set of methods the delegate implements so it receives the product information your app requests. _(deprecated)_

## See Also

### Product information

- [Loading in-app product identifiers](loading-in-app-product-identifiers.md) — Load the unique identifiers for your in-app products to retrieve product information from the App Store.
- [Fetching product information from the App Store](fetching-product-information-from-the-app-store.md) — Retrieve up-to-date information about the products for sale in your app to display to your customers.
- [SKProductsResponse](skproductsresponse.md) — An App Store response to a request for information about a list of products. _(deprecated)_
- [SKProduct](skproduct.md) — Information about a registered product in App Store Connect. _(deprecated)_
