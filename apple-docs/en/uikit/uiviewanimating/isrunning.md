---
title: isRunning
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewanimating/isrunning
source_url: 'https://developer.apple.com/documentation/uikit/uiviewanimating/isrunning'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewanimating/isrunning.json'
content_hash: 'sha256:58018f421941e115'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewAnimating](../uiviewanimating.md)

# isRunning

<sub>Instance Property</sub>

A Boolean value indicating whether the animation is currently running.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isRunning: Bool { get }
```

## Discussion

This property reflects whether the animation is running either in the forward or reverse direction. The value of this property is [true](../../swift/true.md) only after a call to the [- startAnimation](<startanimation().md>) method. The value is [false](../../swift/false.md) when the animator is paused or stopped.

## See Also

### Getting the animator’s state

- [fractionComplete](fractioncomplete.md) — The completion percentage of the animation.
- [reversed](isreversed.md) — A Boolean value indicating whether the animation is running in the reverse direction.
- [state](state.md) — The current state of the animation.
