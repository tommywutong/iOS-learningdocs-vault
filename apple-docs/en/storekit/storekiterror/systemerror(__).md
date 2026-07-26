---
title: 'StoreKitError.systemError(_:)'
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/storekiterror/systemerror(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/storekiterror/systemerror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storekiterror/systemerror%28_%3A%29.json'
content_hash: 'sha256:a808f02723192632'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [StoreKitError](../storekiterror.md)

# StoreKitError.systemError(_:)

<sub>Case</sub>

A system error occurred.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case systemError(any Error)
```

## See Also

### StoreKit Error Codes

- [StoreKitError.networkError(_:)](<networkerror(__).md>) — A network error occurred.
- [StoreKitError.userCancelled](usercancelled.md) — The user canceled.
- [StoreKitError.notAvailableInStorefront](notavailableinstorefront.md) — The function isn’t available on devices configured for this storefront.
- [StoreKitError.notEntitled](notentitled.md) — The app doesn’t have the appropriate entitlements to use the functionality.
- [StoreKitError.unknown](unknown.md) — An unknown error occurred.
- [StoreKitError.unsupported](unsupported.md) — The operation doesn’t support this product.
