---
title: interactiveDismissShouldBegin
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/transition/zoomoptions/interactivedismissshouldbegin
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions/interactivedismissshouldbegin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/transition/zoomoptions/interactivedismissshouldbegin.json'
content_hash: 'sha256:2bf64132a50617ca'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UIViewController](../../../uiviewcontroller.md) · [Transition](../../transition.md) · [ZoomOptions](../zoomoptions.md)

# interactiveDismissShouldBegin

<sub>Instance Property</sub>

A closure that determines whether an interactive dismissal can begin.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var interactiveDismissShouldBegin: ((UIViewController.Transition.ZoomOptions.InteractionContext) -> Bool)? { get set }
```

## See Also

### Accessing the animation state

- [InteractionContext](interactioncontext.md) — Data you can use to determine whether an interactive dismissal can begin.
