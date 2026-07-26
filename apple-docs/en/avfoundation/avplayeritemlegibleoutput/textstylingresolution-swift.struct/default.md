---
title: default
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.struct/default
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.struct/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.struct/default.json'
content_hash: 'sha256:f017504db366b68e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayerItemLegibleOutput](../../avplayeritemlegibleoutput.md) · [TextStylingResolution](../textstylingresolution-swift.struct.md)

# default

<sub>Type Property</sub>

The text styling information is the same level of information that AVFoundation uses within a player layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let `default`: AVPlayerItemLegibleOutput.TextStylingResolution
```

## Discussion

Specify this level of text styling resolution to receive attributed strings from an `AVPlayerItemLegibleOutput` that include the same level of styling information that AVFoundation would use itself to render text within an [AVPlayerLayer](../../avplayerlayer.md). The text styling will accommodate user-level Media Accessibility settings.

## See Also

### Text styling options

- [AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly](sourceandrulesonly.md) — The level of resolution excludes styling provided by the user-level Media Accessibility settings.
