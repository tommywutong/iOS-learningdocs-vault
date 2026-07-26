---
title: AVExperienceController.Experiences
framework: AVKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/experiences
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/experiences'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/experiences.json'
content_hash: 'sha256:521b4e7f85b7bf44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# AVExperienceController.Experiences

<sub>Structure</sub>

A structure that represents a collection of experiences to use with an experience controller.

<sub>visionOS</sub>

```swift
@preconcurrency struct Experiences
```

## Overview

When creating, choose between using [only(_:)](<experiences/only(__).md>) or [recommended(excluding:including:)](<experiences/recommended(excluding_including_).md>). Use [only(_:)](<experiences/only(__).md>) to specify the list of supported experiences. Use [recommended(excluding:including:)](<experiences/recommended(excluding_including_).md>) to include the default set of experiences appropriate for a given platform.

Experiences can be explicitly included or excluded from this list with the corresponding parameters.

## Relationships

- **Conforms To**: [Collection](../../swift/collection.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [Sequence](../../swift/sequence.md)

## Topics

### Defining experiences

- [only(_:)](<experiences/only(__).md>) — Returns a set of experiences for the provided list.
- [recommended(excluding:including:)](<experiences/recommended(excluding_including_).md>) — Returns the recommended set of experiences.

## See Also

### Configuring the experience

- [allowedExperiences](allowedexperiences.md) — The set of experiences the application supports.
- [availableExperiences](availableexperiences.md) — The allowed experiences that are available to use on the device at this time.
- [experience](experience-swift.property.md) — The current experience.
- [Experience](experience-swift.enum.md) — The types of experiences the system supports.
- [configuration](configuration-swift.property.md) — The configuration options per experience.
- [Configuration](configuration-swift.struct.md) — A structure that stores per-experience configuration.
