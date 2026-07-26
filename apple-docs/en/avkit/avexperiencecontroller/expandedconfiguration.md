---
title: AVExperienceController.ExpandedConfiguration
framework: AVKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/expandedconfiguration
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/expandedconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/expandedconfiguration.json'
content_hash: 'sha256:dc81d56fa535e9d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# AVExperienceController.ExpandedConfiguration

<sub>Structure</sub>

A structure that specifies options for an expanded experience.

<sub>visionOS</sub>

```swift
struct ExpandedConfiguration
```

## Overview

It’s valid to transition to this experience even when the original container isn’t in a view hierarchy. In this case, you must specify a [fallbackPlacement](expandedconfiguration/fallbackplacement.md) or the transition result is [AVExperienceController.TransitionContext.TransitionResult.reversed(reason:)](<transitioncontext/transitionresult/reversed(reason_).md>).

## Topics

### Creating an expanded configuration

- [init(fallbackPlacement:)](<expandedconfiguration/init(fallbackplacement_).md>) — Creates a configuration object for an expanded experience.

### Specifying placement

- [fallbackPlacement](expandedconfiguration/fallbackplacement.md) — A fallback placement to use when the original container isn’t in the view controller hierarchy.
- [Placement](expandedconfiguration/placement.md) — A structure that represents where the video will be experienced.

### Configuring automatic immersive transitions

- [automaticTransitionToImmersive](expandedconfiguration/automatictransitiontoimmersive-swift.property.md) — The expanded experience automatic transition behavior for the immersive experience.
- [AutomaticTransitionToImmersive](expandedconfiguration/automatictransitiontoimmersive-swift.enum.md) — The expanded experience automatic transition behavior into the immersive experience.

## See Also

### Configuring experiences

- [expanded](configuration-swift.struct/expanded.md) — Configuration options for an expanded experience.
