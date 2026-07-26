---
title: isInteractive
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollercontexttransitioning/isinteractive
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/isinteractive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning/isinteractive.json'
content_hash: 'sha256:ef48c64705ab47c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md)

# isInteractive

<sub>Instance Property</sub>

A Boolean value indicating whether the transition is currently interactive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isInteractive: Bool { get }
```

## Discussion

A transition is interactive only if the view controller’s delegate provides a corresponding interactive animator object.

Interactive transitions are drive by user-generated events. One common scenario is to use a gesture recognizer to report on the current progress of the animation. The gesture recognizer calls methods of this context object that indicate the completion percentage of the transition or indicate that the transition was canceled or completed by the user.

## See Also

### Getting the transition behaviors

- [animated](isanimated.md) — A Boolean value indicating whether the transition should be animated.
- [presentationStyle](presentationstyle.md) — Returns the presentation style for the view controller transition.
