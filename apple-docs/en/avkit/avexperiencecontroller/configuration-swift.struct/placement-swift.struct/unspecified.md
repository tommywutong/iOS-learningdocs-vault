---
title: unspecified
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/configuration-swift.struct/placement-swift.struct/unspecified
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/configuration-swift.struct/placement-swift.struct/unspecified'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/configuration-swift.struct/placement-swift.struct/unspecified.json'
content_hash: 'sha256:bb14f2b3e7ec9437'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVKit](../../../../avkit.md) · [AVExperienceController](../../../avexperiencecontroller.md) · [Configuration](../../configuration-swift.struct.md) · [Placement](../placement-swift.struct.md)

# unspecified

<sub>Type Property</sub>

Used as default when no UIScene is specified as a placement.

<sub>visionOS</sub>

```swift
static var unspecified: AVExperienceController.Configuration.Placement { get }
```

## Discussion

Experiences will be placed over the UIScene of the original container. If contained within a UIScene, the system will use that scene as a placement, if possible.

## See Also

### Placements

- [over(scene:)](<over(scene_).md>) — Place the video over the provided scene.
