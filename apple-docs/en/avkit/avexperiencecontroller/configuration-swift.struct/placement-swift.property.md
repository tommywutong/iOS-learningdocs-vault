---
title: placement
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/configuration-swift.struct/placement-swift.property
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/configuration-swift.struct/placement-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/configuration-swift.struct/placement-swift.property.json'
content_hash: 'sha256:e6deb6f82ebdb7f0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [Configuration](../configuration-swift.struct.md)

# placement

<sub>Instance Property</sub>

Supply a Placement to be used when the original container isn’t added to the view controller hierarchy; i.e. the AVPlayerViewController is off-screen.

<sub>visionOS</sub>

```swift
var placement: AVExperienceController.Configuration.Placement
```

## Discussion

Indicates the placement of where the media playback will be experienced. Setting this property will apply to all experiences, unless its overwritten by the targeted experience configuration object.

## See Also

### Configuring placement

- [Placement](placement-swift.struct.md) — A struct used to set the placement for the media playback to be experienced.
