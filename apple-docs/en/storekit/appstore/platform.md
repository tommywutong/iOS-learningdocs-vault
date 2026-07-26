---
title: AppStore.Platform
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/appstore/platform
source_url: 'https://developer.apple.com/documentation/storekit/appstore/platform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/appstore/platform.json'
content_hash: 'sha256:6b87da6a3f422c35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppStore](../appstore.md)

# AppStore.Platform

<sub>Structure</sub>

Values that represent Apple platforms.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Platform
```

## Discussion

You choose a platform for your app when you add the new app in App Store Connect. For more information, see [Add a new app](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app/).

The platform values in `AppStore.Platform` are the same as those in App Store Connect.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting platform values

- [iOS](platform/ios.md) — A value that indicates the iOS platform.
- [macOS](platform/macos.md) — A value that indicates the macOS platform.
- [tvOS](platform/tvos.md) — A value that indicates the tvOS platform.
- [visionOS](platform/visionos.md) — A value that indicates the visionOS platform.

### Type Properties

- [managed](platform/managed.md)

## See Also

### Getting the original platform

- [originalPlatform](../apptransaction/originalplatform.md) — The platform on which the customer originally purchased the app.
