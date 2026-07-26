---
title: SKProductStorePromotionVisibility
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+（18.0 起废弃）, iPadOS 11.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 11.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductstorepromotionvisibility
source_url: 'https://developer.apple.com/documentation/storekit/skproductstorepromotionvisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductstorepromotionvisibility.json'
content_hash: 'sha256:c234f34e35e0645f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKProductStorePromotionVisibility

<sub>Enumeration</sub>

The visibility settings that determine if an in-app purchase is visible on a device.

> [!warning] Deprecated
> Use Product.PromotionInfo.Visibility.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@frozen enum SKProductStorePromotionVisibility
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration cases

- [SKProductStorePromotionVisibilityDefault](skproductstorepromotionvisibility/default.md) — Indicates product visibility is the same as the default value set in App Store Connect. _(deprecated)_
- [SKProductStorePromotionVisibilityHide](skproductstorepromotionvisibility/hide.md) — Indicates product is hidden. _(deprecated)_
- [SKProductStorePromotionVisibilityShow](skproductstorepromotionvisibility/show.md) — Indicates product is shown. _(deprecated)_

### Initializers

- [init(rawValue:)](<skproductstorepromotionvisibility/init(rawvalue_).md>) _(deprecated)_

## See Also

### Managing promoted product visibility

- [- fetchStorePromotionVisibilityForProduct:completionHandler:](<skproductstorepromotioncontroller/fetchstorepromotionvisibility(for_completionhandler_).md>) — Reads the visibility setting of a promoted product in the App Store for this device. _(deprecated)_
- [- updateStorePromotionVisibility:forProduct:completionHandler:](<skproductstorepromotioncontroller/update(storepromotionvisibility_for_completionhandler_).md>) — Updates the visibility of the product on the App Store, per device. _(deprecated)_
