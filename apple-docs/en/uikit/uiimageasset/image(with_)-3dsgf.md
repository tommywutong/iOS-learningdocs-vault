---
title: 'image(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimageasset/image(with:)-3dsgf'
source_url: 'https://developer.apple.com/documentation/uikit/uiimageasset/image(with:)-3dsgf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageasset/image%28with%3A%29-3dsgf.json'
content_hash: 'sha256:34d86e9a8e001443'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageAsset](../uiimageasset.md)

# image(with:)

<sub>Instance Method</sub>

Retrieves the variant of the image that best matches the specified trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func image(with traitCollection: UITraitCollection) -> UIImage
```

## Parameters

- `traitCollection` — The trait collection to use when determining which image to return.

## Return Value

The found image.

## Discussion

If this method can’t locate an image that matches the specified trait collection precisely, it returns the best match available.

## See Also

### Retrieving an image from an image asset

- [- imageWithConfiguration:](<image(with_)-8jdwv.md>) — Retrieves the variant of the image that best matches the specified image configuration details.
