---
title: machineGenerated
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/machinegenerated
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/machinegenerated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/machinegenerated.json'
content_hash: 'sha256:0c8d21a489a7d700'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# machineGenerated

<sub>Type Property</sub>

A media characteristic that indicates that a track was generated in an automated fashion by a machine.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let machineGenerated: AVMediaCharacteristic
```

## Discussion

This media characteristic can be used to distinguish machine generated content from human authored content. The value of this characteristic is @“public.machine-generated”.

Note for content authors: for QuickTime movie and .m4v files and for HTTP Live Streaming, a media option is considered to have the characteristic AVMediaCharacteristicIsOriginalContent only if it’s explicitly tagged with the characteristic. See the discussion of the tagging of tracks with media characteristics below.

Also see -[AVAssetTrack hasMediaCharacteristic:] and -[AVMediaSelectionOption hasMediaCharacteristic:].

## See Also

### Content

- [AVMediaCharacteristicIsOriginalContent](isoriginalcontent.md) — A media characteristic that indicates that a track or media selection option contains original content.
- [AVMediaCharacteristicIsMainProgramContent](ismainprogramcontent.md) — A media characteristic that indicates a track or media selection option includes content its author indicates is essential to the asset’s presentation.
- [AVMediaCharacteristicIsAuxiliaryContent](isauxiliarycontent.md) — A media characteristic that indicates a track or media selection option includes content its author indicates is auxiliary to the asset’s presentation.
