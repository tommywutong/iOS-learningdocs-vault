---
title: AVExperienceController.TransitionContext.ReversedReason
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason.json'
content_hash: 'sha256:74c9b204cdf52079'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [TransitionContext](../transitioncontext.md)

# AVExperienceController.TransitionContext.ReversedReason

<sub>Enumeration</sub>

<sub>visionOS</sub>

```swift
@preconcurrency enum ReversedReason
```

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Reasons

- [AVExperienceController.TransitionContext.ReversedReason.invalidConfiguration](reversedreason/invalidconfiguration.md) — A transition could not be completed because some required configuration was unavailable.
- [AVExperienceController.TransitionContext.ReversedReason.invalidExperience](reversedreason/invalidexperience.md) — A transition was attempted with an experience that cannot be transitioned to.
- [AVExperienceController.TransitionContext.ReversedReason.transitionCancelled](reversedreason/transitioncancelled.md) — A transition in progress has been cancelled.
- [AVExperienceController.TransitionContext.ReversedReason.transitionFailed](reversedreason/transitionfailed.md) — A transition has failed.
- [AVExperienceController.TransitionContext.ReversedReason.transitionInProgress](reversedreason/transitioninprogress.md) — A transition was attempted while another transition was in progress.

## See Also

### Understanding transition results

- [Status](status-swift.enum.md) — Describes the status of a transition.
- [TransitionResult](transitionresult.md) — Describes the result of a transition.
