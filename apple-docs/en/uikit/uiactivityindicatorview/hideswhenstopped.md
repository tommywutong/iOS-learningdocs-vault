---
title: hidesWhenStopped
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityindicatorview/hideswhenstopped
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityindicatorview/hideswhenstopped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityindicatorview/hideswhenstopped.json'
content_hash: 'sha256:b201c9f59f5f3741'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityIndicatorView](../uiactivityindicatorview.md)

# hidesWhenStopped

<sub>Instance Property</sub>

A Boolean value that controls whether the activity indicator is hidden when the animation is stopped.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var hidesWhenStopped: Bool { get set }
```

## Discussion

If the value of this property is [true](../../swift/true.md) (the default), the receiver sets its [hidden](../uiview/ishidden.md) property (`UIView`) to [true](../../swift/true.md) when receiver is not animating. If the [hidesWhenStopped](hideswhenstopped.md) property is [false](../../swift/false.md), the receiver is not hidden when animation stops. You stop an animating progress indicator with the [- stopAnimating](<stopanimating().md>) method.

## See Also

### Managing an activity indicator

- [- startAnimating](<startanimating().md>) — Starts the animation of the progress indicator.
- [- stopAnimating](<stopanimating().md>) — Stops the animation of the progress indicator.
- [animating](isanimating.md) — A Boolean value indicating whether the activity indicator is currently running its animation.
