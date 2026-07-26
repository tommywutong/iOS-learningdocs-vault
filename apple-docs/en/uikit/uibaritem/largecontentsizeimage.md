---
title: largeContentSizeImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibaritem/largecontentsizeimage
source_url: 'https://developer.apple.com/documentation/uikit/uibaritem/largecontentsizeimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibaritem/largecontentsizeimage.json'
content_hash: 'sha256:b94b837874ab2ddd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarItem](../uibaritem.md)

# largeContentSizeImage

<sub>Instance Property</sub>

The image to display for users who are blind or have low vision.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var largeContentSizeImage: UIImage? { get set }
```

## Discussion

Use this property to specify a high-resolution version of the item’s image. When displaying an assistive interface for users who are blind or have low vision, UIKit displays this image instead of the standard image. The default value of this property is `nil`.

If you don’t specify an image for this property, UIKit scales the image that you specified in the [image](image.md) property.

## See Also

### Getting and setting properties

- [title](title.md) — The title displayed on the item.
- [image](image.md) — The image used to represent the item.
- [landscapeImagePhone](landscapeimagephone.md) — The image to use to represent the item in landscape orientation when using the iPhone appearance idiom.
- [imageInsets](imageinsets.md) — The image inset or outset for each edge.
- [landscapeImagePhoneInsets](landscapeimagephoneinsets.md) — The image inset or outset for each edge of the image in landscape orientation when using the iPhone appearance idiom.
- [largeContentSizeImageInsets](largecontentsizeimageinsets.md) — The insets to apply to the bar item’s large image when displaying the image in an assistive UI.
- [enabled](isenabled.md) — A Boolean value indicating whether the item is enabled.
- [tag](tag.md) — The bar item’s tag, an app-supplied integer that you can use to identify bar item objects in your app.
