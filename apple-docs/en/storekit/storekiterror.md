---
title: StoreKitError
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/storekiterror
source_url: 'https://developer.apple.com/documentation/storekit/storekiterror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storekiterror.json'
content_hash: 'sha256:54f79ae73e90cc6e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# StoreKitError

<sub>Enumeration</sub>

StoreKit In-App Purchase error codes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum StoreKitError
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Error](../swift/error.md), [Escapable](../swift/escapable.md), [LocalizedError](../foundation/localizederror.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### StoreKit Error Codes

- [StoreKitError.networkError(_:)](<storekiterror/networkerror(__).md>) — A network error occurred.
- [StoreKitError.systemError(_:)](<storekiterror/systemerror(__).md>) — A system error occurred.
- [StoreKitError.userCancelled](storekiterror/usercancelled.md) — The user canceled.
- [StoreKitError.notAvailableInStorefront](storekiterror/notavailableinstorefront.md) — The function isn’t available on devices configured for this storefront.
- [StoreKitError.notEntitled](storekiterror/notentitled.md) — The app doesn’t have the appropriate entitlements to use the functionality.
- [StoreKitError.unknown](storekiterror/unknown.md) — An unknown error occurred.
- [StoreKitError.unsupported](storekiterror/unsupported.md) — The operation doesn’t support this product.

### Enumeration Cases

- [StoreKitError.invalidPresentationContext](storekiterror/invalidpresentationcontext.md) — StoreKit UI cannot be presented from the current context. _(beta)_
