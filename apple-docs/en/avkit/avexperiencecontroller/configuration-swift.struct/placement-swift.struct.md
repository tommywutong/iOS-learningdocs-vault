---
title: AVExperienceController.Configuration.Placement
framework: AVKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/configuration-swift.struct/placement-swift.struct
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/configuration-swift.struct/placement-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/configuration-swift.struct/placement-swift.struct.json'
content_hash: 'sha256:bec823ab65b37e92'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [Configuration](../configuration-swift.struct.md)

# AVExperienceController.Configuration.Placement

<sub>Structure</sub>

A struct used to set the placement for the media playback to be experienced.

<sub>visionOS</sub>

```swift
struct Placement
```

## Overview

Controls where an experience is placed. It can be over a UIScene.

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md)

## Topics

### Placements

- [over(scene:)](<placement-swift.struct/over(scene_).md>) — Place the video over the provided scene.
- [unspecified](placement-swift.struct/unspecified.md) — Used as default when no UIScene is specified as a placement.

## See Also

### Configuring placement

- [placement](placement-swift.property.md) — Supply a Placement to be used when the original container isn’t added to the view controller hierarchy; i.e. the AVPlayerViewController is off-screen.
