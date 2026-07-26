---
title: AVExperienceController.TransitionContext.ReversedReason.transitionFailed
framework: AVKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/transitionfailed
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/transitionfailed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/transitionfailed.json'
content_hash: 'sha256:e863121df3e59f4f'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVKit](../../../../avkit.md) · [AVExperienceController](../../../avexperiencecontroller.md) · [TransitionContext](../../transitioncontext.md) · [ReversedReason](../reversedreason.md)

# AVExperienceController.TransitionContext.ReversedReason.transitionFailed

<sub>Case</sub>

A transition has failed.

<sub>visionOS</sub>

```swift
case transitionFailed
```

## Discussion

This could fail due to changes in the system state after a transition is prepared.

## See Also

### Reasons

- [AVExperienceController.TransitionContext.ReversedReason.invalidConfiguration](invalidconfiguration.md) — A transition could not be completed because some required configuration was unavailable.
- [AVExperienceController.TransitionContext.ReversedReason.invalidExperience](invalidexperience.md) — A transition was attempted with an experience that cannot be transitioned to.
- [AVExperienceController.TransitionContext.ReversedReason.transitionCancelled](transitioncancelled.md) — A transition in progress has been cancelled.
- [AVExperienceController.TransitionContext.ReversedReason.transitionInProgress](transitioninprogress.md) — A transition was attempted while another transition was in progress.
