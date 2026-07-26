---
title: contentIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsadaptiveimageglyph/contentidentifier
source_url: 'https://developer.apple.com/documentation/uikit/nsadaptiveimageglyph/contentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsadaptiveimageglyph/contentidentifier.json'
content_hash: 'sha256:8e51ada54c9f66d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSAdaptiveImageGlyph](../nsadaptiveimageglyph.md)

# contentIdentifier

<sub>Instance Property</sub>

A unique identifier for this image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var contentIdentifier: String { get }
```

## Discussion

Use this property to create a persistent reference to this specific image in your code. The image data contains this content identifier, so the value persists between instantiations.

## See Also

### Getting the content metadata

- [contentDescription](contentdescription.md) — An alternate textual description of the image contents.
- [contentType](contenttype.md) — The image data format to use for this image type.
