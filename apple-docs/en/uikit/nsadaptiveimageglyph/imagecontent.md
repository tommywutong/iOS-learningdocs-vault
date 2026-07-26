---
title: imageContent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsadaptiveimageglyph/imagecontent
source_url: 'https://developer.apple.com/documentation/uikit/nsadaptiveimageglyph/imagecontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsadaptiveimageglyph/imagecontent.json'
content_hash: 'sha256:96114fbb71f3e85b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSAdaptiveImageGlyph](../nsadaptiveimageglyph.md)

# imageContent

<sub>Instance Property</sub>

The raw data for the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var imageContent: Data { get }
```

## Discussion

This property contains the image data, the unique identifier for the image, the image description, and additional metadata. When saving your content to disk, save the data for any adaptive images with the rest of your content. If you need to specify a type for the image data, use the value in the [contentType](contenttype.md) property.
