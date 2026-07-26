---
title: 'unregisterImage(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimageasset/unregisterimage(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimageasset/unregisterimage(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageasset/unregisterimage%28with%3A%29.json'
content_hash: 'sha256:6d4f0c705476ad17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageAsset](../uiimageasset.md)

# unregisterImage(with:)

<sub>Instance Method</sub>

Unregisters the image with the specified image configuration details from the image asset.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func unregisterImage(with configuration: UIImage.Configuration)
```

## Parameters

- `configuration` — An object containing the image configuration details for a previously registered image. This method matches only the contents of the object, so you don’t need to specify the same object you used at registration time.

## Discussion

This method searches for an image whose configuration details match the information in the `configuration` parameter. The configuration details must match exactly, and must be associated with an image that you registered previously.

## See Also

### Registering and unregistering images

- [- registerImage:withTraitCollection:](<register(__with_)-2plm5.md>) — Registers an image with the specified trait collection.
- [- registerImage:withConfiguration:](<register(__with_)-89c5b.md>) — Registers an image with the specified image configuration details.
- [- unregisterImageWithTraitCollection:](<unregister(imagewith_).md>) — Unregisters the image with the specified trait collection from the image asset.
