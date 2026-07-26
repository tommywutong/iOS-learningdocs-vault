---
title: 'experienceController(_:didChangeTransitionContext:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangetransitioncontext:)'
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangetransitioncontext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller%28_%3Adidchangetransitioncontext%3A%29.json'
content_hash: 'sha256:f465c8f088856b82'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [Delegate](../delegate-swift.protocol.md)

# experienceController(_:didChangeTransitionContext:)

<sub>Instance Method</sub>

Tells the delegate when the transition context changes during a transition.

<sub>visionOS</sub>

```swift
@MainActor func experienceController(_ controller: AVExperienceController, didChangeTransitionContext context: AVExperienceController.TransitionContext)
```

## Parameters

- `controller` — The experience controller.

- `context` — An structure that contains information about the transition.

## Discussion

Implement this method to track the transition between experiences.

## See Also

### Responding to experience changes

- [experienceController(_:didChangeAvailableExperiences:)](<experiencecontroller(__didchangeavailableexperiences_).md>) — Tells the delegate when the available experiences change.
- [experienceController(_:prepareForTransitionUsing:)](<experiencecontroller(__preparefortransitionusing_).md>) — Tells the delegate that the system is preparing for a transition.
- [TransitionContext](../transitioncontext.md) — The state of the transition provided to the delegate object.
