---
title: isMainProgramContent
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/ismainprogramcontent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/ismainprogramcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/ismainprogramcontent.json'
content_hash: 'sha256:2d3c61e8cbf6553d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# isMainProgramContent

<sub>Type Property</sub>

A media characteristic that indicates a track or media selection option includes content its author indicates is essential to the asset’s presentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let isMainProgramContent: AVMediaCharacteristic
```

## Discussion

Example: an option that presents the main program audio for the presentation, regardless of locale, would typically have this characteristic.

The value of this characteristic is `public.main-program-content`.

The system infers the presence of this characteristic for a media option; it considers any option that doesn’t have the characteristic [AVMediaCharacteristicIsAuxiliaryContent](isauxiliarycontent.md) to be main content.

## See Also

### Content

- [AVMediaCharacteristicIsOriginalContent](isoriginalcontent.md) — A media characteristic that indicates that a track or media selection option contains original content.
- [AVMediaCharacteristicIsAuxiliaryContent](isauxiliarycontent.md) — A media characteristic that indicates a track or media selection option includes content its author indicates is auxiliary to the asset’s presentation.
- [AVMediaCharacteristicMachineGenerated](machinegenerated.md) — A media characteristic that indicates that a track was generated in an automated fashion by a machine.
