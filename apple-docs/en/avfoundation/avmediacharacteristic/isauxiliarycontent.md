---
title: isAuxiliaryContent
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/isauxiliarycontent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/isauxiliarycontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/isauxiliarycontent.json'
content_hash: 'sha256:c05c559bf03e0e25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# isAuxiliaryContent

<sub>Type Property</sub>

A media characteristic that indicates a track or media selection option includes content its author indicates is auxiliary to the asset’s presentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let isAuxiliaryContent: AVMediaCharacteristic
```

## Discussion

An example of auxiliary content is audio commentary about the presentation.

The value of this characteristic is `public.auxiliary-content`.

For QuickTime movies and `.m4v` files, a media option has this characteristic only if the media’s author tags it that way, or if it belongs to an alternate track group that excludes its associated track from autoselection.

## See Also

### Content

- [AVMediaCharacteristicIsOriginalContent](isoriginalcontent.md) — A media characteristic that indicates that a track or media selection option contains original content.
- [AVMediaCharacteristicIsMainProgramContent](ismainprogramcontent.md) — A media characteristic that indicates a track or media selection option includes content its author indicates is essential to the asset’s presentation.
- [AVMediaCharacteristicMachineGenerated](machinegenerated.md) — A media characteristic that indicates that a track was generated in an automated fashion by a machine.
