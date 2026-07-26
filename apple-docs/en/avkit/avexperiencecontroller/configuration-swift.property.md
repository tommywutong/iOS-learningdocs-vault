---
title: configuration
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/configuration-swift.property
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/configuration-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/configuration-swift.property.json'
content_hash: 'sha256:997f496c2c0fcbd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# configuration

<sub>Instance Property</sub>

The configuration options per experience.

<sub>visionOS</sub>

```swift
@MainActor final var configuration: AVExperienceController.Configuration
```

## Discussion

You may modify the configuration at any time, but after the [experienceController(_:prepareForTransitionUsing:)](<delegate-swift.protocol/experiencecontroller(__preparefortransitionusing_).md>) delegate callback returns, the system copies the configuration and uses it for the ensuing transition. Further modifications affect subsequent transitions.

## See Also

### Configuring the experience

- [allowedExperiences](allowedexperiences.md) — The set of experiences the application supports.
- [availableExperiences](availableexperiences.md) — The allowed experiences that are available to use on the device at this time.
- [Experiences](experiences.md) — A structure that represents a collection of experiences to use with an experience controller.
- [experience](experience-swift.property.md) — The current experience.
- [Experience](experience-swift.enum.md) — The types of experiences the system supports.
- [Configuration](configuration-swift.struct.md) — A structure that stores per-experience configuration.
