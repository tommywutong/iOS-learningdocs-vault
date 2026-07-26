---
title: highlightedAnimationImages
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/highlightedanimationimages
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/highlightedanimationimages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/highlightedanimationimages.json'
content_hash: 'sha256:78777e61cf650480'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# highlightedAnimationImages

<sub>Instance Property</sub>

An array of [UIImage](../uiimage.md) objects to use for an animation when the view is highlighted.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var highlightedAnimationImages: [UIImage]? { get set }
```

## Discussion

The array must contain [UIImage](../uiimage.md) objects. You may use the same image object more than once in the array. Setting this property to a value other than `nil` hides the image represented by the [highlightedImage](highlightedimage.md) property. The value of this property is `nil` by default.

## See Also

### Related Documentation

- [highlightedImage](highlightedimage.md) — The highlighted image displayed in the image view.

### Animating a sequence of images

- [animationImages](animationimages.md) — An array of [UIImage](../uiimage.md) objects to use for an animation.
- [animationDuration](animationduration.md) — The amount of time it takes to go through one cycle of the images.
- [animationRepeatCount](animationrepeatcount.md) — Specifies the number of times to repeat the animation.
- [- startAnimating](<startanimating().md>) — Starts animating the images in the receiver.
- [- stopAnimating](<stopanimating().md>) — Stops animating the images in the receiver.
- [animating](isanimating.md) — Returns a Boolean value indicating whether the animation is running.
