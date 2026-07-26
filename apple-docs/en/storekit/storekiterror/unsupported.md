---
title: StoreKitError.unsupported
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/storekiterror/unsupported
source_url: 'https://developer.apple.com/documentation/storekit/storekiterror/unsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storekiterror/unsupported.json'
content_hash: 'sha256:15f498f01cbb66f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [StoreKitError](../storekiterror.md)

# StoreKitError.unsupported

<sub>Case</sub>

The operation doesn’t support this product.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case unsupported
```

## Discussion

The system surfaces this error when the type that originates the request doesn’t support the operation. For example, initializing an [AdvancedCommerceProduct](../advancedcommerceproduct.md) using the product ID of an in-app purchase that isn’t registered as a generic SKU in App Store Connect.

## See Also

### StoreKit Error Codes

- [StoreKitError.networkError(_:)](<networkerror(__).md>) — A network error occurred.
- [StoreKitError.systemError(_:)](<systemerror(__).md>) — A system error occurred.
- [StoreKitError.userCancelled](usercancelled.md) — The user canceled.
- [StoreKitError.notAvailableInStorefront](notavailableinstorefront.md) — The function isn’t available on devices configured for this storefront.
- [StoreKitError.notEntitled](notentitled.md) — The app doesn’t have the appropriate entitlements to use the functionality.
- [StoreKitError.unknown](unknown.md) — An unknown error occurred.
