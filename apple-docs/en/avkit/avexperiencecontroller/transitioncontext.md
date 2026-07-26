---
title: AVExperienceController.TransitionContext
framework: AVKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/transitioncontext
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/transitioncontext.json'
content_hash: 'sha256:7cc1d214c0589c9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# AVExperienceController.TransitionContext

<sub>Structure</sub>

The state of the transition provided to the delegate object.

<sub>visionOS</sub>

```swift
@preconcurrency struct TransitionContext
```

## Overview

When `AVExperienceController` transitions its `experience` from `fromExperience` to `toExperience`, delegate callbacks provide instances of `TransitionContext` to allow clients to respond as the transition progresses or reverts. The normal `Status` sequence is `.preparing` -\> `.transitioning` -\> `.completed` Once `.completed`, `AVExperienceController`’s `experience` is now the `toExperience`.

Not all transitions are `.completed`, instead they are `.reversed` back to the `fromExperience`. Reversed transitions can happen after `.preparing` or after `.transitioning`, but it will not happen after `.completed` or before `.preparing`. When a transition is reversed a reason is provided.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Inspecting the transition

- [fromExperience](transitioncontext/fromexperience.md) — The experience of the `AVExperienceController` before the transition was initiated.
- [toExperience](transitioncontext/toexperience.md) — The experience to which the `AVExperienceController` has been requested to transition to.
- [status](transitioncontext/status-swift.property.md) — The status of the transition.

### Understanding transition results

- [Status](transitioncontext/status-swift.enum.md) — Describes the status of a transition.
- [TransitionResult](transitioncontext/transitionresult.md) — Describes the result of a transition.
- [ReversedReason](transitioncontext/reversedreason.md)

## See Also

### Responding to experience changes

- [experienceController(_:didChangeAvailableExperiences:)](<delegate-swift.protocol/experiencecontroller(__didchangeavailableexperiences_).md>) — Tells the delegate when the available experiences change.
- [experienceController(_:prepareForTransitionUsing:)](<delegate-swift.protocol/experiencecontroller(__preparefortransitionusing_).md>) — Tells the delegate that the system is preparing for a transition.
- [experienceController(_:didChangeTransitionContext:)](<delegate-swift.protocol/experiencecontroller(__didchangetransitioncontext_).md>) — Tells the delegate when the transition context changes during a transition.
