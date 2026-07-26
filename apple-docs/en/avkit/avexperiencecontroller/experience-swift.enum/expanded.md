---
title: AVExperienceController.Experience.expanded
framework: AVKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/experience-swift.enum/expanded
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.enum/expanded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/experience-swift.enum/expanded.json'
content_hash: 'sha256:b9aa714eb68614a8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [Experience](../experience-swift.enum.md)

# AVExperienceController.Experience.expanded

<sub>Case</sub>

An experience where the system places the video outside of its original container.

<sub>visionOS</sub>

```swift
case expanded
```

## Discussion

Transition to this experience to get the appropriate expanded experience for the platform.

It’s valid to transition to this experience even when the original container isn’t in a view hierarchy. In this case, you must specify a [fallbackPlacement](../expandedconfiguration/fallbackplacement.md) or the transition result is [AVExperienceController.TransitionContext.TransitionResult.reversed(reason:)](<../transitioncontext/transitionresult/reversed(reason_).md>).

> [!note] Note
> This experience to is analogous to a player view controller’s fullscreen state.

## See Also

### Supported experiences

- [AVExperienceController.Experience.embedded](embedded.md) — An experience where the video embeds within its original container.
- [AVExperienceController.Experience.multiview](multiview.md) — An experience where multiple videos play together.
- [AVExperienceController.Experience.immersive](immersive.md) — Indicates an experience in which the video extends beyond the app window boundaries/container.
