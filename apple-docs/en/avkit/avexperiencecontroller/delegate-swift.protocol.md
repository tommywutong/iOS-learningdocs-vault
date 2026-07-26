---
title: AVExperienceController.Delegate
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/delegate-swift.protocol
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/delegate-swift.protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/delegate-swift.protocol.json'
content_hash: 'sha256:e778bbe172e46dd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# AVExperienceController.Delegate

<sub>Protocol</sub>

A protocol that defines the methods to implement to respond to experience changes.

<sub>visionOS</sub>

```swift
@MainActor protocol Delegate : AnyObject
```

## Overview

Use this delegate to be informed of transitions and to update applications state based on these changes.

## Topics

### Responding to experience changes

- [experienceController(_:didChangeAvailableExperiences:)](<delegate-swift.protocol/experiencecontroller(__didchangeavailableexperiences_).md>) — Tells the delegate when the available experiences change.
- [experienceController(_:prepareForTransitionUsing:)](<delegate-swift.protocol/experiencecontroller(__preparefortransitionusing_).md>) — Tells the delegate that the system is preparing for a transition.
- [experienceController(_:didChangeTransitionContext:)](<delegate-swift.protocol/experiencecontroller(__didchangetransitioncontext_).md>) — Tells the delegate when the transition context changes during a transition.
- [TransitionContext](transitioncontext.md) — The state of the transition provided to the delegate object.

## See Also

### Configuring a delegate

- [delegate](delegate-swift.property.md) — A delegate object for the experience controller.
