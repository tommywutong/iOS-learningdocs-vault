---
title: allowedExperiences
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/allowedexperiences
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/allowedexperiences'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/allowedexperiences.json'
content_hash: 'sha256:aa2c1a37d74e46b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# allowedExperiences

<sub>Instance Property</sub>

The set of experiences the application supports.

<sub>visionOS</sub>

```swift
@MainActor final var allowedExperiences: AVExperienceController.Experiences { get set }
```

## Discussion

Use this to allow additional experiences like multiview, or to disable expanded. This list is the basis for [availableExperiences](availableexperiences.md), which filters out inapplicable experiences.

> [!note] Note
> Because [AVExperienceController.Experience.embedded](experience-swift.enum/embedded.md) is the initial experience, and the one returned to when others end, it’s a programming error to exclude it from this list.

## See Also

### Configuring the experience

- [availableExperiences](availableexperiences.md) — The allowed experiences that are available to use on the device at this time.
- [Experiences](experiences.md) — A structure that represents a collection of experiences to use with an experience controller.
- [experience](experience-swift.property.md) — The current experience.
- [Experience](experience-swift.enum.md) — The types of experiences the system supports.
- [configuration](configuration-swift.property.md) — The configuration options per experience.
- [Configuration](configuration-swift.struct.md) — A structure that stores per-experience configuration.
