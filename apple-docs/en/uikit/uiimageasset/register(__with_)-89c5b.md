---
title: 'register(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimageasset/register(_:with:)-89c5b'
source_url: 'https://developer.apple.com/documentation/uikit/uiimageasset/register(_:with:)-89c5b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageasset/register%28_%3Awith%3A%29-89c5b.json'
content_hash: 'sha256:1ccb1fbb1d97cf0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageAsset](../uiimageasset.md)

# register(_:with:)

<sub>Instance Method</sub>

Registers an image with the specified image configuration details.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func register(_ image: UIImage, with configuration: UIImage.Configuration)
```

## Parameters

- `image` — The image you want to register with the image asset.

- `configuration` — The image configuration details to associate with `image`.

## Discussion

Each image in an image asset must have a unique configuration. If the asset already contains a registered image with the equivalent configuration, it replaces that image with the one in the `image` parameter.

> [!important] Important
> The trait collection in `configuration` must always contain an explicit value in its [displayScale](../uitraitcollection/displayscale.md) property. You may experience unexpected results from [- imageWithConfiguration:](<image(with_)-8jdwv.md>) if the trait collection doesn’t explicitly define the desired scale.

## See Also

### Registering and unregistering images

- [- registerImage:withTraitCollection:](<register(__with_)-2plm5.md>) — Registers an image with the specified trait collection.
- [- unregisterImageWithTraitCollection:](<unregister(imagewith_).md>) — Unregisters the image with the specified trait collection from the image asset.
- [- unregisterImageWithConfiguration:](<unregisterimage(with_).md>) — Unregisters the image with the specified image configuration details from the image asset.
