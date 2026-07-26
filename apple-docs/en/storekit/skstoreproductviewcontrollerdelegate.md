---
title: SKStoreProductViewControllerDelegate
framework: StoreKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.0+, macOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductviewcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductviewcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductviewcontrollerdelegate.json'
content_hash: 'sha256:8a45c8488142ba40'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductViewControllerDelegate

<sub>Protocol</sub>

A protocol to call when the customer dismisses the store screen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
protocol SKStoreProductViewControllerDelegate : NSObjectProtocol
```

## Overview

Typically, this protocol is implemented by the view controller in your application that originally displayed the store screen.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to a Dismiss Action

- [- productViewControllerDidFinish:](<skstoreproductviewcontrollerdelegate/productviewcontrollerdidfinish(__).md>) — Called when the user dismisses the store screen.

## See Also

### Setting a delegate

- [delegate](skstoreproductviewcontroller/delegate.md) — The store view controller’s delegate.
