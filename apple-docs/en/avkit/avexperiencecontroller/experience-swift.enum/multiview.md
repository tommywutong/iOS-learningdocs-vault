---
title: AVExperienceController.Experience.multiview
framework: AVKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/experience-swift.enum/multiview
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.enum/multiview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/experience-swift.enum/multiview.json'
content_hash: 'sha256:967e0a1534ce16cd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [Experience](../experience-swift.enum.md)

# AVExperienceController.Experience.multiview

<sub>Case</sub>

An experience where multiple videos play together.

<sub>visionOS</sub>

```swift
case multiview
```

## Discussion

Configure this experience type using an [AVMultiviewManager](../../avmultiviewmanager.md).

It’s valid to transition to this experience from a player view controller that isn’t in a view hierarchy. This is useful when adding additional videos to a multiview experience.

Transition to embedded to remove an item from the multiview experience.

## See Also

### Supported experiences

- [AVExperienceController.Experience.embedded](embedded.md) — An experience where the video embeds within its original container.
- [AVExperienceController.Experience.expanded](expanded.md) — An experience where the system places the video outside of its original container.
- [AVExperienceController.Experience.immersive](immersive.md) — Indicates an experience in which the video extends beyond the app window boundaries/container.
