---
title: AVExperienceController.Experience.immersive
framework: AVKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/experience-swift.enum/immersive
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.enum/immersive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/experience-swift.enum/immersive.json'
content_hash: 'sha256:4747b15e8fe8c80a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [Experience](../experience-swift.enum.md)

# AVExperienceController.Experience.immersive

<sub>Case</sub>

Indicates an experience in which the video extends beyond the app window boundaries/container.

<sub>visionOS</sub>

```swift
case immersive
```

## Discussion

It is valid to transition to `immersive` even when the `AVPlayerViewController` is not in the view hiearchy. In this case, a Placement must be specified through the Configuration object. If no placement is specified, the transition result will be `.reversed`.

## See Also

### Supported experiences

- [AVExperienceController.Experience.embedded](embedded.md) — An experience where the video embeds within its original container.
- [AVExperienceController.Experience.expanded](expanded.md) — An experience where the system places the video outside of its original container.
- [AVExperienceController.Experience.multiview](multiview.md) — An experience where multiple videos play together.
