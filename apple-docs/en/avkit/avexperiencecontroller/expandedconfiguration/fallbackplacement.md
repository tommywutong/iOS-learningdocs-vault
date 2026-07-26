---
title: fallbackPlacement
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/expandedconfiguration/fallbackplacement
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/expandedconfiguration/fallbackplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/expandedconfiguration/fallbackplacement.json'
content_hash: 'sha256:1403b2a0ad1d5dc5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [ExpandedConfiguration](../expandedconfiguration.md)

# fallbackPlacement

<sub>Instance Property</sub>

A fallback placement to use when the original container isn’t in the view controller hierarchy.

<sub>visionOS</sub>

```swift
var fallbackPlacement: AVExperienceController.ExpandedConfiguration.Placement
```

## Discussion

The system places expanded experience over the scene of the original container. When the container isn’t available, the system uses this value. If neither specifies a valid placement, attempting to transition to an expanded experience fails.

## See Also

### Specifying placement

- [Placement](placement.md) — A structure that represents where the video will be experienced.
