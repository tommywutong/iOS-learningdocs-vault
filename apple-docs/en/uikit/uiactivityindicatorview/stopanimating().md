---
title: stopAnimating()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityindicatorview/stopanimating()
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityindicatorview/stopanimating()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityindicatorview/stopanimating%28%29.json'
content_hash: 'sha256:b9fe0286552e85aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityIndicatorView](../uiactivityindicatorview.md)

# stopAnimating()

<sub>Instance Method</sub>

Stops the animation of the progress indicator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func stopAnimating()
```

## Discussion

Call this method to stop the animation of the progress indicator started with a call to [- startAnimating](<startanimating().md>). When animating is stopped, the indicator is hidden, unless [hidesWhenStopped](hideswhenstopped.md) is [false](../../swift/false.md).

## See Also

### Managing an activity indicator

- [- startAnimating](<startanimating().md>) — Starts the animation of the progress indicator.
- [animating](isanimating.md) — A Boolean value indicating whether the activity indicator is currently running its animation.
- [hidesWhenStopped](hideswhenstopped.md) — A Boolean value that controls whether the activity indicator is hidden when the animation is stopped.
