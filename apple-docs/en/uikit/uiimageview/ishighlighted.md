---
title: isHighlighted
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/ishighlighted
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/ishighlighted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/ishighlighted.json'
content_hash: 'sha256:6e783608a1c5ec42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# isHighlighted

<sub>Instance Property</sub>

A Boolean value that determines whether the image is highlighted.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isHighlighted: Bool { get set }
```

## Discussion

This property determines whether the regular or highlighted images are used. When [highlighted](ishighlighted.md) is set to [true](../../swift/true.md), a non-animated image will use the [highlightedImage](highlightedimage.md) property and an animated image will use the [highlightedAnimationImages](highlightedanimationimages.md). If both of those properties are set to `nil` or if [highlighted](ishighlighted.md) is set to [false](../../swift/false.md), it will use the [image](image.md) and [animationImages](animationimages.md) properties.

## See Also

### Configuring the image view

- [userInteractionEnabled](isuserinteractionenabled.md) — A Boolean value that determines whether user events are ignored and removed from the event queue.
- [tintColor](tintcolor.md) — A color used to tint template images in the view hierarchy.
