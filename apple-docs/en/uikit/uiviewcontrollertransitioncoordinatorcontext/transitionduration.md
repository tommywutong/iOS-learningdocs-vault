---
title: transitionDuration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/transitionduration
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/transitionduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/transitionduration.json'
content_hash: 'sha256:fc5350f8132d5379'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md)

# transitionDuration

<sub>Instance Property</sub>

Returns the noninteractive duration of a transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var transitionDuration: TimeInterval { get }
```

## Return Value

The expected duration, in seconds, of the view controller transition, if it proceeds noninteractively.

## Discussion

The transition duration defines the time for the main transition to finish. Use this value when configuring your own animations if you want them to end at the same time as the main transition.

## See Also

### Getting the behavior attributes

- [presentationStyle](presentationstyle.md) — The presentation style to use for the transition.
- [completionCurve](completioncurve.md) — Returns the completion curve associated with the transition.
- [completionVelocity](completionvelocity.md) — Returns the starting velocity to use for any final animations.
- [percentComplete](percentcomplete.md) — Returns the percentage of completion for an interactive transition when it moves to its noninteractive phase.
