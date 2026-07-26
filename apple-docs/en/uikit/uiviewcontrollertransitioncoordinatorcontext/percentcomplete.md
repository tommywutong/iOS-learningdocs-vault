---
title: percentComplete
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/percentcomplete
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/percentcomplete'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/percentcomplete.json'
content_hash: 'sha256:7d95fd3e6d090a48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md)

# percentComplete

<sub>Instance Property</sub>

Returns the percentage of completion for an interactive transition when it moves to its noninteractive phase.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var percentComplete: CGFloat { get }
```

## Return Value

The percentage of completion when an interactive transition moves to its noninteractive completion phase.

## Discussion

Use this value to determine how much of the interactive transition completed before the transition was canceled or moved to its final animations.

## See Also

### Getting the behavior attributes

- [presentationStyle](presentationstyle.md) — The presentation style to use for the transition.
- [transitionDuration](transitionduration.md) — Returns the noninteractive duration of a transition.
- [completionCurve](completioncurve.md) — Returns the completion curve associated with the transition.
- [completionVelocity](completionvelocity.md) — Returns the starting velocity to use for any final animations.
