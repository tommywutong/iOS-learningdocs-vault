---
title: AVExperienceController.TransitionContext.ReversedReason.transitionCancelled
framework: AVKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/transitioncancelled
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/transitioncancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/transitioncancelled.json'
content_hash: 'sha256:518f5bc48a328df6'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVKit](../../../../avkit.md) · [AVExperienceController](../../../avexperiencecontroller.md) · [TransitionContext](../../transitioncontext.md) · [ReversedReason](../reversedreason.md)

# AVExperienceController.TransitionContext.ReversedReason.transitionCancelled

<sub>Case</sub>

A transition in progress has been cancelled.

<sub>visionOS</sub>

```swift
case transitionCancelled
```

## Discussion

This can happen due to user interaction or some other system event.

## See Also

### Reasons

- [AVExperienceController.TransitionContext.ReversedReason.invalidConfiguration](invalidconfiguration.md) — A transition could not be completed because some required configuration was unavailable.
- [AVExperienceController.TransitionContext.ReversedReason.invalidExperience](invalidexperience.md) — A transition was attempted with an experience that cannot be transitioned to.
- [AVExperienceController.TransitionContext.ReversedReason.transitionFailed](transitionfailed.md) — A transition has failed.
- [AVExperienceController.TransitionContext.ReversedReason.transitionInProgress](transitioninprogress.md) — A transition was attempted while another transition was in progress.
