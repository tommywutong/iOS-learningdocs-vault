---
title: sourceAndRulesOnly
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.struct/sourceandrulesonly
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.struct/sourceandrulesonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.struct/sourceandrulesonly.json'
content_hash: 'sha256:e1e5637b13e9701b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayerItemLegibleOutput](../../avplayeritemlegibleoutput.md) · [TextStylingResolution](../textstylingresolution-swift.struct.md)

# sourceAndRulesOnly

<sub>Type Property</sub>

The level of resolution excludes styling provided by the user-level Media Accessibility settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let sourceAndRulesOnly: AVPlayerItemLegibleOutput.TextStylingResolution
```

## Discussion

You typically use this option to override the styling specified in source media. When overriding the styling, you are strongly encouraged to allow your custom styling in turn to be overridden by user preferences for text styling that are available as Media Accessibility settings. See `Media Accessibility Function` for more information.

## See Also

### Text styling options

- [AVPlayerItemLegibleOutputTextStylingResolutionDefault](default.md) — The text styling information is the same level of information that AVFoundation uses within a player layer.
