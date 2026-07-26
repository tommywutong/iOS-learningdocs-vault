---
title: AVPlayerItemLegibleOutput.TextStylingResolution
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.struct.json'
content_hash: 'sha256:d7583e738020eaaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemLegibleOutput](../avplayeritemlegibleoutput.md)

# AVPlayerItemLegibleOutput.TextStylingResolution

<sub>Structure</sub>

A text styling resolution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct TextStylingResolution
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Text styling options

- [AVPlayerItemLegibleOutputTextStylingResolutionDefault](textstylingresolution-swift.struct/default.md) — The text styling information is the same level of information that AVFoundation uses within a player layer.
- [AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly](textstylingresolution-swift.struct/sourceandrulesonly.md) — The level of resolution excludes styling provided by the user-level Media Accessibility settings.

### Initializers

- [init(rawValue:)](<textstylingresolution-swift.struct/init(rawvalue_).md>) — Creates a text styling resolution structure with a string value.

## See Also

### Configuring text styling

- [textStylingResolution](textstylingresolution-swift.property.md) — A string identifier indicating the degree of text styling to be applied to attributed strings vended by the  object.
