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
doc_path: '/documentation/uikit/uiimageasset/register(_:with:)-2plm5'
source_url: 'https://developer.apple.com/documentation/uikit/uiimageasset/register(_:with:)-2plm5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageasset/register%28_%3Awith%3A%29-2plm5.json'
content_hash: 'sha256:0ca80bb078067647'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageAsset](../uiimageasset.md)

# register(_:with:)

<sub>Instance Method</sub>

Registers an image with the specified trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func register(_ image: UIImage, with traitCollection: UITraitCollection)
```

## Parameters

- `image` — The image you want to register with the image asset.

- `traitCollection` — The traits to associate with `image`.

## Discussion

Each image in an image asset must have a unique set of traits. If the asset already contains a registered image with the equivalent traits, it replaces that image with the one in the `image` parameter.

> [!important] Important
> The trait collection must always contain an explicit value in its [displayScale](../uitraitcollection/displayscale.md) property. You may experience unexpected results from [- imageWithTraitCollection:](<image(with_)-3dsgf.md>) if the trait collection doesn’t explicitly define the desired scale.

## See Also

### Registering and unregistering images

- [- registerImage:withConfiguration:](<register(__with_)-89c5b.md>) — Registers an image with the specified image configuration details.
- [- unregisterImageWithTraitCollection:](<unregister(imagewith_).md>) — Unregisters the image with the specified trait collection from the image asset.
- [- unregisterImageWithConfiguration:](<unregisterimage(with_).md>) — Unregisters the image with the specified image configuration details from the image asset.
