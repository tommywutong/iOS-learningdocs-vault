---
title: SKProductStorePromotionController
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+（18.0 起废弃）, iPadOS 11.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 11.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductstorepromotioncontroller
source_url: 'https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductstorepromotioncontroller.json'
content_hash: 'sha256:310f76c657e5b9f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKProductStorePromotionController

<sub>Class</sub>

A product promotion controller for customizing the order and visibility of In-App Purchases per device.

> [!warning] Deprecated
> Use Product.PromotionInfo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class SKProductStorePromotionController
```

## Overview

For information about promoting In-App Purchases, see [Promoting In-App Purchases](promoting-in-app-purchases.md).

> [!note] Note
> [SKProductStorePromotionController](skproductstorepromotioncontroller.md) and promoted In-App Purchases aren’t available to compatible iPad and iPhone apps running in visionOS.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Managing promoted product order

- [- fetchStorePromotionOrderWithCompletionHandler:](<skproductstorepromotioncontroller/fetchstorepromotionorder(completionhandler_).md>) — Reads the product order override that determines the promoted product order on this device. _(deprecated)_
- [- updateStorePromotionOrder:completionHandler:](<skproductstorepromotioncontroller/update(storepromotionorder_completionhandler_).md>) — Overrides the promoted product order on this device. _(deprecated)_

### Managing promoted product visibility

- [- fetchStorePromotionVisibilityForProduct:completionHandler:](<skproductstorepromotioncontroller/fetchstorepromotionvisibility(for_completionhandler_).md>) — Reads the visibility setting of a promoted product in the App Store for this device. _(deprecated)_
- [- updateStorePromotionVisibility:forProduct:completionHandler:](<skproductstorepromotioncontroller/update(storepromotionvisibility_for_completionhandler_).md>) — Updates the visibility of the product on the App Store, per device. _(deprecated)_
- [SKProductStorePromotionVisibility](skproductstorepromotionvisibility.md) — The visibility settings that determine if an in-app purchase is visible on a device. _(deprecated)_

### Getting the controller

- [+ defaultController](<skproductstorepromotioncontroller/default().md>) — Returns the default product store promotion controller. _(deprecated)_

## See Also

### Promotions

- [Promoting In-App Purchases](promoting-in-app-purchases.md) — Show promoted In-App Purchases on your product page and handle purchases that customers initiate on the App Store.
- [Testing promoted In-App Purchases](testing-promoted-in-app-purchases.md) — Test your In-App Purchases before making your app available in the App Store.
