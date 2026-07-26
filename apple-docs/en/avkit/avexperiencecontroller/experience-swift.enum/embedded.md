---
title: AVExperienceController.Experience.embedded
framework: AVKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/experience-swift.enum/embedded
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.enum/embedded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/experience-swift.enum/embedded.json'
content_hash: 'sha256:c1037ccda22a6e8a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [Experience](../experience-swift.enum.md)

# AVExperienceController.Experience.embedded

<sub>Case</sub>

An experience where the video embeds within its original container.

<sub>visionOS</sub>

```swift
case embedded
```

## Discussion

This experience is the starting state and is valid on all platforms. You may embed video in the original container even if that container isn’t visible or not in the view hierarchy. It’s valid to transition to this experience from any other experience, even when the player view controller isn’t in the view hierarchy.

It’s the app’s responsibility to correctly manage the player view controller’s view lifecycle.

> [!note] Note
> This experience to is analogous to a player view controller’s inline state.

## See Also

### Supported experiences

- [AVExperienceController.Experience.expanded](expanded.md) — An experience where the system places the video outside of its original container.
- [AVExperienceController.Experience.multiview](multiview.md) — An experience where multiple videos play together.
- [AVExperienceController.Experience.immersive](immersive.md) — Indicates an experience in which the video extends beyond the app window boundaries/container.
