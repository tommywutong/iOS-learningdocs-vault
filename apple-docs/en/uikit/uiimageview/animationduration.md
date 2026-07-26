---
title: animationDuration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/animationduration
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/animationduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/animationduration.json'
content_hash: 'sha256:df5ccc8d8e88333e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# animationDuration

<sub>Instance Property</sub>

The amount of time it takes to go through one cycle of the images.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var animationDuration: TimeInterval { get set }
```

## Discussion

The time duration is measured in seconds. The default value of this property is `0.0`, which causes the image view to use a duration equal to the number of images multiplied by 1/30th of a second. Thus, if you had 30 images, the duration would be 1 second.

## See Also

### Animating a sequence of images

- [animationImages](animationimages.md) — An array of [UIImage](../uiimage.md) objects to use for an animation.
- [highlightedAnimationImages](highlightedanimationimages.md) — An array of [UIImage](../uiimage.md) objects to use for an animation when the view is highlighted.
- [animationRepeatCount](animationrepeatcount.md) — Specifies the number of times to repeat the animation.
- [- startAnimating](<startanimating().md>) — Starts animating the images in the receiver.
- [- stopAnimating](<stopanimating().md>) — Stops animating the images in the receiver.
- [animating](isanimating.md) — Returns a Boolean value indicating whether the animation is running.
