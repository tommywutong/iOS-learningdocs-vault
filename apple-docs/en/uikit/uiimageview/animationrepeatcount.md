---
title: animationRepeatCount
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/animationrepeatcount
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/animationrepeatcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/animationrepeatcount.json'
content_hash: 'sha256:09fd40ba4e042006'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# animationRepeatCount

<sub>Instance Property</sub>

Specifies the number of times to repeat the animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var animationRepeatCount: Int { get set }
```

## Discussion

The default value is `0`, which specifies to repeat the animation indefinitely.

## See Also

### Animating a sequence of images

- [animationImages](animationimages.md) — An array of [UIImage](../uiimage.md) objects to use for an animation.
- [highlightedAnimationImages](highlightedanimationimages.md) — An array of [UIImage](../uiimage.md) objects to use for an animation when the view is highlighted.
- [animationDuration](animationduration.md) — The amount of time it takes to go through one cycle of the images.
- [- startAnimating](<startanimating().md>) — Starts animating the images in the receiver.
- [- stopAnimating](<stopanimating().md>) — Stops animating the images in the receiver.
- [animating](isanimating.md) — Returns a Boolean value indicating whether the animation is running.
