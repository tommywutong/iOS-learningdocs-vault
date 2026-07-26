---
title: startAnimating()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/startanimating()
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/startanimating()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/startanimating%28%29.json'
content_hash: 'sha256:4a5621ff6dc1d8e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# startAnimating()

<sub>Instance Method</sub>

Starts animating the images in the receiver.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func startAnimating()
```

## Discussion

This method always starts the animation from the first image in the list.

## See Also

### Animating a sequence of images

- [animationImages](animationimages.md) — An array of [UIImage](../uiimage.md) objects to use for an animation.
- [highlightedAnimationImages](highlightedanimationimages.md) — An array of [UIImage](../uiimage.md) objects to use for an animation when the view is highlighted.
- [animationDuration](animationduration.md) — The amount of time it takes to go through one cycle of the images.
- [animationRepeatCount](animationrepeatcount.md) — Specifies the number of times to repeat the animation.
- [- stopAnimating](<stopanimating().md>) — Stops animating the images in the receiver.
- [animating](isanimating.md) — Returns a Boolean value indicating whether the animation is running.
