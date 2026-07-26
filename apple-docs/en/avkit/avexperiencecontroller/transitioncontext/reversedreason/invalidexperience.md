---
title: AVExperienceController.TransitionContext.ReversedReason.invalidExperience
framework: AVKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/invalidexperience
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/invalidexperience'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/invalidexperience.json'
content_hash: 'sha256:1bcff09415ff0550'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVKit](../../../../avkit.md) · [AVExperienceController](../../../avexperiencecontroller.md) · [TransitionContext](../../transitioncontext.md) · [ReversedReason](../reversedreason.md)

# AVExperienceController.TransitionContext.ReversedReason.invalidExperience

<sub>Case</sub>

A transition was attempted with an experience that cannot be transitioned to.

<sub>visionOS</sub>

```swift
case invalidExperience
```

## Discussion

Possible response is to consult `AVExperienceController.experience` and `AVExperienceController.availableExperiences` to choose a different experience to transition to.

## See Also

### Reasons

- [AVExperienceController.TransitionContext.ReversedReason.invalidConfiguration](invalidconfiguration.md) — A transition could not be completed because some required configuration was unavailable.
- [AVExperienceController.TransitionContext.ReversedReason.transitionCancelled](transitioncancelled.md) — A transition in progress has been cancelled.
- [AVExperienceController.TransitionContext.ReversedReason.transitionFailed](transitionfailed.md) — A transition has failed.
- [AVExperienceController.TransitionContext.ReversedReason.transitionInProgress](transitioninprogress.md) — A transition was attempted while another transition was in progress.
