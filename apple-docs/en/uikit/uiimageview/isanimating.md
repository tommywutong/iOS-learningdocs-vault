---
title: isAnimating
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/isanimating
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/isanimating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/isanimating.json'
content_hash: 'sha256:86cb48fc6c1edb43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# isAnimating

<sub>Instance Property</sub>

Returns a Boolean value indicating whether the animation is running.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isAnimating: Bool { get }
```

## Return Value

[true](../../swift/true.md) if the animation is running; otherwise, [false](../../swift/false.md).

## See Also

### Animating a sequence of images

- [animationImages](animationimages.md) — An array of [UIImage](../uiimage.md) objects to use for an animation.
- [highlightedAnimationImages](highlightedanimationimages.md) — An array of [UIImage](../uiimage.md) objects to use for an animation when the view is highlighted.
- [animationDuration](animationduration.md) — The amount of time it takes to go through one cycle of the images.
- [animationRepeatCount](animationrepeatcount.md) — Specifies the number of times to repeat the animation.
- [- startAnimating](<startanimating().md>) — Starts animating the images in the receiver.
- [- stopAnimating](<stopanimating().md>) — Stops animating the images in the receiver.
