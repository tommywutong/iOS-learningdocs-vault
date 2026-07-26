---
title: title
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibaritem/title
source_url: 'https://developer.apple.com/documentation/uikit/uibaritem/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibaritem/title.json'
content_hash: 'sha256:8d05c3cc15cc6e9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarItem](../uibaritem.md)

# title

<sub>Instance Property</sub>

The title displayed on the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var title: String? { get set }
```

## Discussion

You should set this property before adding the item to a bar. The default value is `nil`.

## See Also

### Getting and setting properties

- [image](image.md) — The image used to represent the item.
- [landscapeImagePhone](landscapeimagephone.md) — The image to use to represent the item in landscape orientation when using the iPhone appearance idiom.
- [largeContentSizeImage](largecontentsizeimage.md) — The image to display for users who are blind or have low vision.
- [imageInsets](imageinsets.md) — The image inset or outset for each edge.
- [landscapeImagePhoneInsets](landscapeimagephoneinsets.md) — The image inset or outset for each edge of the image in landscape orientation when using the iPhone appearance idiom.
- [largeContentSizeImageInsets](largecontentsizeimageinsets.md) — The insets to apply to the bar item’s large image when displaying the image in an assistive UI.
- [enabled](isenabled.md) — A Boolean value indicating whether the item is enabled.
- [tag](tag.md) — The bar item’s tag, an app-supplied integer that you can use to identify bar item objects in your app.
