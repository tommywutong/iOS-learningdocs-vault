---
title: AVExperienceController.TransitionContext.ReversedReason.invalidConfiguration
framework: AVKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/invalidconfiguration
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/invalidconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/invalidconfiguration.json'
content_hash: 'sha256:4053854877430003'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVKit](../../../../avkit.md) · [AVExperienceController](../../../avexperiencecontroller.md) · [TransitionContext](../../transitioncontext.md) · [ReversedReason](../reversedreason.md)

# AVExperienceController.TransitionContext.ReversedReason.invalidConfiguration

<sub>Case</sub>

A transition could not be completed because some required configuration was unavailable.

<sub>visionOS</sub>

```swift
case invalidConfiguration
```

## Discussion

This can happen if AVPlayerViewController has been freed.

## See Also

### Reasons

- [AVExperienceController.TransitionContext.ReversedReason.invalidExperience](invalidexperience.md) — A transition was attempted with an experience that cannot be transitioned to.
- [AVExperienceController.TransitionContext.ReversedReason.transitionCancelled](transitioncancelled.md) — A transition in progress has been cancelled.
- [AVExperienceController.TransitionContext.ReversedReason.transitionFailed](transitionfailed.md) — A transition has failed.
- [AVExperienceController.TransitionContext.ReversedReason.transitionInProgress](transitioninprogress.md) — A transition was attempted while another transition was in progress.
