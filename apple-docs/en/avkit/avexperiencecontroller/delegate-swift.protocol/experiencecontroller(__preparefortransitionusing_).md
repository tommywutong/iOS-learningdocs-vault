---
title: 'experienceController(_:prepareForTransitionUsing:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:preparefortransitionusing:)'
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:preparefortransitionusing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller%28_%3Apreparefortransitionusing%3A%29.json'
content_hash: 'sha256:fa667a3ebbbccbd0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [Delegate](../delegate-swift.protocol.md)

# experienceController(_:prepareForTransitionUsing:)

<sub>Instance Method</sub>

Tells the delegate that the system is preparing for a transition.

<sub>visionOS</sub>

```swift
@MainActor func experienceController(_ controller: AVExperienceController, prepareForTransitionUsing context: AVExperienceController.TransitionContext) async
```

## Parameters

- `controller` — The `AVExperienceController`.

- `context` — Contains information about the transition.

## Discussion

Implement this method to prepare the app’s state for the [toExperience](../transitioncontext/toexperience.md). This may include showing or hiding view controllers, putting the player view controller in the view hierarchy, or any other asynchronous work required for the transition. This is the last chance to update [configuration](../configuration-swift.property.md) before the transition begins.

## See Also

### Responding to experience changes

- [experienceController(_:didChangeAvailableExperiences:)](<experiencecontroller(__didchangeavailableexperiences_).md>) — Tells the delegate when the available experiences change.
- [experienceController(_:didChangeTransitionContext:)](<experiencecontroller(__didchangetransitioncontext_).md>) — Tells the delegate when the transition context changes during a transition.
- [TransitionContext](../transitioncontext.md) — The state of the transition provided to the delegate object.
