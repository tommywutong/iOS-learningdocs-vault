---
title: status
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/transitioncontext/status-swift.property
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/status-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/transitioncontext/status-swift.property.json'
content_hash: 'sha256:d6a36848e4f39796'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [TransitionContext](../transitioncontext.md)

# status

<sub>Instance Property</sub>

The status of the transition.

<sub>visionOS</sub>

```swift
let status: AVExperienceController.TransitionContext.Status
```

## Discussion

Use this to update your application state based on the current state of the transition.

## See Also

### Inspecting the transition

- [fromExperience](fromexperience.md) — The experience of the `AVExperienceController` before the transition was initiated.
- [toExperience](toexperience.md) — The experience to which the `AVExperienceController` has been requested to transition to.
