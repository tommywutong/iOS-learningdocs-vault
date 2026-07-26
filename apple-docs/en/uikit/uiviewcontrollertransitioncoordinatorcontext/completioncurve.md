---
title: completionCurve
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/completioncurve
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/completioncurve'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/completioncurve.json'
content_hash: 'sha256:8260c44c88b67792'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md)

# completionCurve

<sub>Instance Property</sub>

Returns the completion curve associated with the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var completionCurve: UIView.AnimationCurve { get }
```

## Return Value

The completion curve for the view controller transition. For a list of possible values, see the [AnimationCurve](../uiview/animationcurve.md) type.

## Discussion

The completion curve defines the timing of the animations. For interactive transitions, this value is usually obtained from the [completionCurve](../uiviewcontrollerinteractivetransitioning/completioncurve.md) property of the interactive animator object. Use this value when configuring your own animations if you want the same timing as the main transition.

## See Also

### Getting the behavior attributes

- [presentationStyle](presentationstyle.md) — The presentation style to use for the transition.
- [transitionDuration](transitionduration.md) — Returns the noninteractive duration of a transition.
- [completionVelocity](completionvelocity.md) — Returns the starting velocity to use for any final animations.
- [percentComplete](percentcomplete.md) — Returns the percentage of completion for an interactive transition when it moves to its noninteractive phase.
