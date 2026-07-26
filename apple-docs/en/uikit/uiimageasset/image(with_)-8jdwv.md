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
doc_path: '/documentation/uikit/uiimageasset/image(with:)-8jdwv'
source_url: 'https://developer.apple.com/documentation/uikit/uiimageasset/image(with:)-8jdwv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageasset/image%28with%3A%29-8jdwv.json'
content_hash: 'sha256:690d4d504afb967c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageAsset](../uiimageasset.md)

# image(with:)

<sub>Instance Method</sub>

Retrieves the variant of the image that best matches the specified image configuration details.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func image(with configuration: UIImage.Configuration) -> UIImage
```

## Parameters

- `configuration` — The configuration details to use when determining which image to return.

## Return Value

The image object for the specified configuration.

## Discussion

If this method can’t locate an image that matches the specified image configuration precisely, it returns the best match available.

## See Also

### Retrieving an image from an image asset

- [- imageWithTraitCollection:](<image(with_)-3dsgf.md>) — Retrieves the variant of the image that best matches the specified trait collection.
