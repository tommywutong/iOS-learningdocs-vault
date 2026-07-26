---
title: AVExperienceController.Experience
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/experience-swift.enum
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/experience-swift.enum.json'
content_hash: 'sha256:eb88373ce0de8f74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# AVExperienceController.Experience

<sub>Enumeration</sub>

The types of experiences the system supports.

<sub>visionOS</sub>

```swift
@preconcurrency enum Experience
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Supported experiences

- [AVExperienceController.Experience.embedded](experience-swift.enum/embedded.md) — An experience where the video embeds within its original container.
- [AVExperienceController.Experience.expanded](experience-swift.enum/expanded.md) — An experience where the system places the video outside of its original container.
- [AVExperienceController.Experience.multiview](experience-swift.enum/multiview.md) — An experience where multiple videos play together.
- [AVExperienceController.Experience.immersive](experience-swift.enum/immersive.md) — Indicates an experience in which the video extends beyond the app window boundaries/container.

## See Also

### Configuring the experience

- [allowedExperiences](allowedexperiences.md) — The set of experiences the application supports.
- [availableExperiences](availableexperiences.md) — The allowed experiences that are available to use on the device at this time.
- [Experiences](experiences.md) — A structure that represents a collection of experiences to use with an experience controller.
- [experience](experience-swift.property.md) — The current experience.
- [configuration](configuration-swift.property.md) — The configuration options per experience.
- [Configuration](configuration-swift.struct.md) — A structure that stores per-experience configuration.
