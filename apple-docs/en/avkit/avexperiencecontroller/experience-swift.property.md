---
title: experience
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/experience-swift.property
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/experience-swift.property.json'
content_hash: 'sha256:2e3f2a55d2b80864'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# experience

<sub>Instance Property</sub>

The current experience.

<sub>visionOS</sub>

```swift
@MainActor final var experience: AVExperienceController.Experience { get }
```

## Discussion

The system updates this value only after the [status](transitioncontext/status-swift.property.md) changes to [AVExperienceController.TransitionContext.Status.finished(result:)](<transitioncontext/status-swift.enum/finished(result_).md>).

Implement the [experienceController(_:didChangeTransitionContext:)](<delegate-swift.protocol/experiencecontroller(__didchangetransitioncontext_).md>) delegate method to observe changes to this value.

## See Also

### Configuring the experience

- [allowedExperiences](allowedexperiences.md) — The set of experiences the application supports.
- [availableExperiences](availableexperiences.md) — The allowed experiences that are available to use on the device at this time.
- [Experiences](experiences.md) — A structure that represents a collection of experiences to use with an experience controller.
- [Experience](experience-swift.enum.md) — The types of experiences the system supports.
- [configuration](configuration-swift.property.md) — The configuration options per experience.
- [Configuration](configuration-swift.struct.md) — A structure that stores per-experience configuration.
