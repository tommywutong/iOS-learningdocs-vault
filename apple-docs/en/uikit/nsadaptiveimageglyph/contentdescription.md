---
title: contentDescription
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsadaptiveimageglyph/contentdescription
source_url: 'https://developer.apple.com/documentation/uikit/nsadaptiveimageglyph/contentdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsadaptiveimageglyph/contentdescription.json'
content_hash: 'sha256:177ca5bec20e8be3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSAdaptiveImageGlyph](../nsadaptiveimageglyph.md)

# contentDescription

<sub>Instance Property</sub>

An alternate textual description of the image contents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var contentDescription: String { get }
```

## Discussion

This string contains a brief description of the image, which is useful for searches or places where you need a text-based description. The adaptive image derives the content of this property from the underlying image data.

## See Also

### Getting the content metadata

- [contentIdentifier](contentidentifier.md) — A unique identifier for this image.
- [contentType](contenttype.md) — The image data format to use for this image type.
