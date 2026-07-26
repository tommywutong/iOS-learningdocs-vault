---
title: promotionalIcon
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/producticonphase/promotionalicon
source_url: 'https://developer.apple.com/documentation/storekit/producticonphase/promotionalicon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/producticonphase/promotionalicon.json'
content_hash: 'sha256:090eb9d3d9e56205'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ProductIconPhase](../producticonphase.md)

# promotionalIcon

<sub>Instance Property</sub>

The promotional image, if the loading task is successful.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var promotionalIcon: Image? { get }
```

## Discussion

This value is `nil` while the image is loading, or if the system can’t access the promotional image for any reason. Use this value as a convenience to access the image in code that doesn’t depend on the reason an image may not be accessible.

For information about setting up promotional images, see [Promote in-app purchases](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases).
