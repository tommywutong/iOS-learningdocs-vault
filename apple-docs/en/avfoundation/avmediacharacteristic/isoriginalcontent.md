---
title: isOriginalContent
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/isoriginalcontent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/isoriginalcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/isoriginalcontent.json'
content_hash: 'sha256:11c28ba536b059b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# isOriginalContent

<sub>Type Property</sub>

A media characteristic that indicates that a track or media selection option contains original content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let isOriginalContent: AVMediaCharacteristic
```

## Discussion

This characteristic differentiates original content from supplementary or derivative content, such as a language translation.

## See Also

### Content

- [AVMediaCharacteristicIsMainProgramContent](ismainprogramcontent.md) — A media characteristic that indicates a track or media selection option includes content its author indicates is essential to the asset’s presentation.
- [AVMediaCharacteristicIsAuxiliaryContent](isauxiliarycontent.md) — A media characteristic that indicates a track or media selection option includes content its author indicates is auxiliary to the asset’s presentation.
- [AVMediaCharacteristicMachineGenerated](machinegenerated.md) — A media characteristic that indicates that a track was generated in an automated fashion by a machine.
