---
title: contentStretch
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（6.0 起废弃）, iPadOS 3.0+（6.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiview/contentstretch
source_url: 'https://developer.apple.com/documentation/uikit/uiview/contentstretch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/contentstretch.json'
content_hash: 'sha256:1d93c19e4427204d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# contentStretch

<sub>Instance Property</sub>

The rectangle that defines the stretchable and nonstretchable regions of a view.

> [!warning] Deprecated
> To achieve the same effect, use [- resizableImageWithCapInsets:](<../uiimage/resizableimage(withcapinsets_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) CGRect contentStretch;
```

## Discussion

You use this property to control how a view’s content is stretched to fill its bounds when the view is resized. Content stretching is often used to animate the resizing of a view. For example, buttons and other controls use stretching to maintain crisp borders while allowing the middle portions of the control to stretch and fill the available space.

> [!note] Note
> For stretching image-based content, it is simpler to use a [UIImageView](../uiimageview.md) object with a stretchable image instead of setting this property. You can create a stretchable image using the [- stretchableImageWithLeftCapWidth:topCapHeight:](<../uiimage/stretchableimage(withleftcapwidth_topcapheight_).md>) method of [UIImage](../uiimage.md).

The values you specify for this rectangle must be normalized to the range `0.0` to `1.0`. These values are then scaled to the size of the view’s content to obtain the appropriate pixel values. The default value for this rectangle has an origin of `(0.0, 0.0)` and a size of `(1.0, 1.0)`. This reflects a rectangle whose stretchable portion encompasses the entire content.
