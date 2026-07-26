---
title: 'experienceController(_:didChangeAvailableExperiences:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangeavailableexperiences:)'
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangeavailableexperiences:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller%28_%3Adidchangeavailableexperiences%3A%29.json'
content_hash: 'sha256:6eaf33166033e065'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [Delegate](../delegate-swift.protocol.md)

# experienceController(_:didChangeAvailableExperiences:)

<sub>Instance Method</sub>

Tells the delegate when the available experiences change.

<sub>visionOS</sub>

```swift
@MainActor func experienceController(_ controller: AVExperienceController, didChangeAvailableExperiences availableExperiences: AVExperienceController.Experiences)
```

## Parameters

- `controller` — The experience controller.

- `availableExperiences` — The current value of [availableExperiences](../availableexperiences.md).

## Discussion

Use this callback to hide or show interface elements based on which experiences are possible.

## See Also

### Responding to experience changes

- [experienceController(_:prepareForTransitionUsing:)](<experiencecontroller(__preparefortransitionusing_).md>) — Tells the delegate that the system is preparing for a transition.
- [experienceController(_:didChangeTransitionContext:)](<experiencecontroller(__didchangetransitioncontext_).md>) — Tells the delegate when the transition context changes during a transition.
- [TransitionContext](../transitioncontext.md) — The state of the transition provided to the delegate object.
