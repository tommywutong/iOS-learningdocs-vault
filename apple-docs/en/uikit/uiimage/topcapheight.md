---
title: topCapHeight
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiimage/topcapheight
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/topcapheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/topcapheight.json'
content_hash: 'sha256:45e2dfee5a1618fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# topCapHeight

<sub>Instance Property</sub>

The vertical end-cap size.

> [!warning] Deprecated
> Use the [capInsets](capinsets.md) property instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
var topCapHeight: Int { get }
```

## Discussion

End caps specify the portion of an image that should not be resized when an image is stretched. This technique is used to implement buttons and other resizable image-based interface elements. When a button with end caps is resized, the resizing occurs only in the middle of the button, in the region between the end caps. The end caps themselves keep their original size and appearance.

This property specifies the size of the top end cap. The middle (stretchable) portion is assumed to be 1 pixel wide. The bottom end cap is therefore computed by adding the size of the top end cap and the middle portion together and then subtracting that value from the height of the image:

```objc
bottomCapHeight = image.size.height - (image.topCapHeight + 1);
```

By default, this property is set to 0, which indicates that the image does not use end caps and the entire image is subject to stretching. To create a new image with a nonzero value for this property, use the [- stretchableImageWithLeftCapWidth:topCapHeight:](<stretchableimage(withleftcapwidth_topcapheight_).md>) method.

## See Also

### Deprecated

- [- stretchableImageWithLeftCapWidth:topCapHeight:](<stretchableimage(withleftcapwidth_topcapheight_).md>) — Creates and returns a new image object with the specified cap values. _(deprecated)_
- [leftCapWidth](leftcapwidth.md) — The horizontal end-cap size. _(deprecated)_
