---
title: AVExperienceController.Configuration
framework: AVKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/configuration-swift.struct
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/configuration-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/configuration-swift.struct.json'
content_hash: 'sha256:c428836c00b097f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# AVExperienceController.Configuration

<sub>Structure</sub>

A structure that stores per-experience configuration.

<sub>visionOS</sub>

```swift
struct Configuration
```

## Topics

### Configuring experiences

- [expanded](configuration-swift.struct/expanded.md) — Configuration options for an expanded experience.
- [ExpandedConfiguration](expandedconfiguration.md) — A structure that specifies options for an expanded experience.

### Configuring placement

- [placement](configuration-swift.struct/placement-swift.property.md) — Supply a Placement to be used when the original container isn’t added to the view controller hierarchy; i.e. the AVPlayerViewController is off-screen.
- [Placement](configuration-swift.struct/placement-swift.struct.md) — A struct used to set the placement for the media playback to be experienced.

## See Also

### Configuring the experience

- [allowedExperiences](allowedexperiences.md) — The set of experiences the application supports.
- [availableExperiences](availableexperiences.md) — The allowed experiences that are available to use on the device at this time.
- [Experiences](experiences.md) — A structure that represents a collection of experiences to use with an experience controller.
- [experience](experience-swift.property.md) — The current experience.
- [Experience](experience-swift.enum.md) — The types of experiences the system supports.
- [configuration](configuration-swift.property.md) — The configuration options per experience.
