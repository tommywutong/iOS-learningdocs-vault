---
title: isEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibaritem/isenabled
source_url: 'https://developer.apple.com/documentation/uikit/uibaritem/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibaritem/isenabled.json'
content_hash: 'sha256:87517bf3910f2ace'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarItem](../uibaritem.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value indicating whether the item is enabled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

If [false](../../swift/false.md), the item is drawn partially dimmed to indicate it’s disabled. The default value is [true](../../swift/true.md).

## See Also

### Getting and setting properties

- [title](title.md) — The title displayed on the item.
- [image](image.md) — The image used to represent the item.
- [landscapeImagePhone](landscapeimagephone.md) — The image to use to represent the item in landscape orientation when using the iPhone appearance idiom.
- [largeContentSizeImage](largecontentsizeimage.md) — The image to display for users who are blind or have low vision.
- [imageInsets](imageinsets.md) — The image inset or outset for each edge.
- [landscapeImagePhoneInsets](landscapeimagephoneinsets.md) — The image inset or outset for each edge of the image in landscape orientation when using the iPhone appearance idiom.
- [largeContentSizeImageInsets](largecontentsizeimageinsets.md) — The insets to apply to the bar item’s large image when displaying the image in an assistive UI.
- [tag](tag.md) — The bar item’s tag, an app-supplied integer that you can use to identify bar item objects in your app.
