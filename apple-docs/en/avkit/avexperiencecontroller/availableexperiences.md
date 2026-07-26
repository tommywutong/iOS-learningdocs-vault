---
title: availableExperiences
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/availableexperiences
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/availableexperiences'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/availableexperiences.json'
content_hash: 'sha256:584eaf11ee214900'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# availableExperiences

<sub>Instance Property</sub>

The allowed experiences that are available to use on the device at this time.

<sub>visionOS</sub>

```swift
@MainActor final var availableExperiences: AVExperienceController.Experiences { get }
```

## Discussion

This property is a subset of [allowedExperiences](allowedexperiences.md), filtered for platform, device configuration, and system state.

## See Also

### Configuring the experience

- [allowedExperiences](allowedexperiences.md) — The set of experiences the application supports.
- [Experiences](experiences.md) — A structure that represents a collection of experiences to use with an experience controller.
- [experience](experience-swift.property.md) — The current experience.
- [Experience](experience-swift.enum.md) — The types of experiences the system supports.
- [configuration](configuration-swift.property.md) — The configuration options per experience.
- [Configuration](configuration-swift.struct.md) — A structure that stores per-experience configuration.
