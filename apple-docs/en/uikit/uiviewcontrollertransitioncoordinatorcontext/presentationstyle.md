---
title: presentationStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/presentationstyle
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/presentationstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/presentationstyle.json'
content_hash: 'sha256:7a7452c23996b70e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md)

# presentationStyle

<sub>Instance Property</sub>

The presentation style to use for the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var presentationStyle: UIModalPresentationStyle { get }
```

## Return Value

The modal presentation style associated with the transition or [UIModalPresentationNone](../uimodalpresentationstyle/none.md) if the transition is not a modal presentation or dismissal. For a list of possible values, see “Modal Presentation Styles” in [UIViewController](../uiviewcontroller.md).

## Discussion

When presenting or dismissing a view controller modally, this method returns the presentation style used for that transition. For interface rotations and other events that don’t involve a specific transition between view controllers, this method returns [UIModalPresentationNone](../uimodalpresentationstyle/none.md).

## See Also

### Getting the behavior attributes

- [transitionDuration](transitionduration.md) — Returns the noninteractive duration of a transition.
- [completionCurve](completioncurve.md) — Returns the completion curve associated with the transition.
- [completionVelocity](completionvelocity.md) — Returns the starting velocity to use for any final animations.
- [percentComplete](percentcomplete.md) — Returns the percentage of completion for an interactive transition when it moves to its noninteractive phase.
