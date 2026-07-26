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
doc_path: /documentation/uikit/uiactivityindicatorview/startanimating()
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityindicatorview/startanimating()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityindicatorview/startanimating%28%29.json'
content_hash: 'sha256:9986784d93a391cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityIndicatorView](../uiactivityindicatorview.md)

# startAnimating()

<sub>Instance Method</sub>

Starts the animation of the progress indicator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func startAnimating()
```

## Discussion

When the progress indicator is animated, the gear spins to indicate indeterminate progress. The indicator is animated until [- stopAnimating](<stopanimating().md>) is called.

## See Also

### Managing an activity indicator

- [- stopAnimating](<stopanimating().md>) — Stops the animation of the progress indicator.
- [animating](isanimating.md) — A Boolean value indicating whether the activity indicator is currently running its animation.
- [hidesWhenStopped](hideswhenstopped.md) — A Boolean value that controls whether the activity indicator is hidden when the animation is stopped.
