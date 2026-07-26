---
title: contentType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsadaptiveimageglyph/contenttype
source_url: 'https://developer.apple.com/documentation/uikit/nsadaptiveimageglyph/contenttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsadaptiveimageglyph/contenttype.json'
content_hash: 'sha256:af37b0925ea71907'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSAdaptiveImageGlyph](../nsadaptiveimageglyph.md)

# contentType

<sub>Type Property</sub>

The image data format to use for this image type.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class var contentType: UTType { get }
```

## Discussion

Use this type when you need to specify the type of the image data. Adaptive images are compatible with the HEIC format, but include extra metadata about the supported resolutions and sizes.

## See Also

### Getting the content metadata

- [contentIdentifier](contentidentifier.md) — A unique identifier for this image.
- [contentDescription](contentdescription.md) — An alternate textual description of the image contents.
