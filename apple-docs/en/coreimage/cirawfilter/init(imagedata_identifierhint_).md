---
title: 'init(imageData:identifierHint:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cirawfilter/init(imagedata:identifierhint:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cirawfilter/init(imagedata:identifierhint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawfilter/init%28imagedata%3Aidentifierhint%3A%29.json'
content_hash: 'sha256:4f92397896bc82b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRAWFilter](../cirawfilter.md)

# init(imageData:identifierHint:)

<sub>Initializer</sub>

Creates a RAW filter from the image data and type hint that you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(imageData data: Data, identifierHint: String?)
```

## Parameters

- `data` — The image data.

- `identifierHint` — A string that identifies the image type.

## See Also

### Creating a filter

- [+ filterWithCVPixelBuffer:properties:](<init(cvpixelbuffer_properties_)-6209q.md>) — Creates a RAW filter from the pixel buffer and its properties that you specify.
- [+ filterWithImageURL:](<init(imageurl_).md>) — Creates a RAW filter from the image at the URL location that you specify.
