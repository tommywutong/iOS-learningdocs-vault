---
title: 'unregister(imageWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimageasset/unregister(imagewith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimageasset/unregister(imagewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageasset/unregister%28imagewith%3A%29.json'
content_hash: 'sha256:32af781b3f47d621'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageAsset](../uiimageasset.md)

# unregister(imageWith:)

<sub>Instance Method</sub>

Unregisters the image with the specified trait collection from the image asset.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func unregister(imageWith traitCollection: UITraitCollection)
```

## Parameters

- `traitCollection` — A trait collection containing the traits for a previously registered image. This method matches only the trait values, so you don’t need to specify the same object you used at registration time.

## Discussion

This method searches for an image whose trait collection matches the one in the `traitCollection` parameter. The traits in both collections must match exactly, and the matching trait collection must be associated with an image that you registered previously.

## See Also

### Registering and unregistering images

- [- registerImage:withTraitCollection:](<register(__with_)-2plm5.md>) — Registers an image with the specified trait collection.
- [- registerImage:withConfiguration:](<register(__with_)-89c5b.md>) — Registers an image with the specified image configuration details.
- [- unregisterImageWithConfiguration:](<unregisterimage(with_).md>) — Unregisters the image with the specified image configuration details from the image asset.
