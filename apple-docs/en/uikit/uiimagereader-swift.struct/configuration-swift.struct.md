---
title: UIImageReader.Configuration
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct.json'
content_hash: 'sha256:ab8a0d8103ffd91b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageReader](../uiimagereader-swift.struct.md)

# UIImageReader.Configuration

<sub>Structure</sub>

The properties that a reader uses to decode images.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct Configuration
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md)

## Topics

### Creating the configuration

- [init()](<configuration-swift.struct/init().md>) — Creates a new instance of the image reader configuration.

### Configuration properties

- [prefersHighDynamicRange](configuration-swift.struct/prefershighdynamicrange.md) — A Boolean value that indicates whether the image reader should decode the image as HDR when the type is capable of decoding in either SDR or HDR.
- [preparesImagesForDisplay](configuration-swift.struct/preparesimagesfordisplay.md) — A Boolean value that indicates whether the image reader prepares the image for display.
- [preferredThumbnailSize](configuration-swift.struct/preferredthumbnailsize.md) — The thumbnail size in pixels that the image reader makes the image.
- [pixelsPerInch](configuration-swift.struct/pixelsperinch.md) — The integral scale that the image reader applies to the image.
