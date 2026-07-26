---
title: animationImages
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/animationimages
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/animationimages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/animationimages.json'
content_hash: 'sha256:e58a44a056b41381'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# animationImages

<sub>Instance Property</sub>

An array of [UIImage](../uiimage.md) objects to use for an animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var animationImages: [UIImage]? { get set }
```

## Discussion

The array must contain [UIImage](../uiimage.md) objects. You may use the same image object more than once in the array. Setting this property to a value other than `nil` hides the image represented by the [image](image.md) property. The value of this property is `nil` by default.

## See Also

### Related Documentation

- [image](image.md) — The image displayed in the image view.

### Animating a sequence of images

- [highlightedAnimationImages](highlightedanimationimages.md) — An array of [UIImage](../uiimage.md) objects to use for an animation when the view is highlighted.
- [animationDuration](animationduration.md) — The amount of time it takes to go through one cycle of the images.
- [animationRepeatCount](animationrepeatcount.md) — Specifies the number of times to repeat the animation.
- [- startAnimating](<startanimating().md>) — Starts animating the images in the receiver.
- [- stopAnimating](<stopanimating().md>) — Stops animating the images in the receiver.
- [animating](isanimating.md) — Returns a Boolean value indicating whether the animation is running.
