---
title: textStylingResolution
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.property.json'
content_hash: 'sha256:5aff9461720fcbbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemLegibleOutput](../avplayeritemlegibleoutput.md)

# textStylingResolution

<sub>Instance Property</sub>

A string identifier indicating the degree of text styling to be applied to attributed strings vended by the  object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var textStylingResolution: AVPlayerItemLegibleOutput.TextStylingResolution { get set }
```

## Discussion

Valid values are described in `Text Style Settings`.  An exception ([invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md)) is raised if this property is set to any other value.

The default value is [AVPlayerItemLegibleOutputTextStylingResolutionDefault](textstylingresolution-swift.struct/default.md), which indicates that attributed strings vended by the receiver includes the same level of styling information that would be used if the text was rendered by an instance of [AVPlayerLayer](../avplayerlayer.md).

> [!note] Note
> This is an advanced feature and you should rarely need to change it from the default value.

## See Also

### Configuring text styling

- [TextStylingResolution](textstylingresolution-swift.struct.md) — A text styling resolution.
