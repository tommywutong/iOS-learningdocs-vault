---
title: 'init(imageURL:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cirawfilter/init(imageurl:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cirawfilter/init(imageurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawfilter/init%28imageurl%3A%29.json'
content_hash: 'sha256:f155d1b9ad28905f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRAWFilter](../cirawfilter.md)

# init(imageURL:)

<sub>Initializer</sub>

Creates a RAW filter from the image at the URL location that you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(imageURL url: URL)
```

## Parameters

- `url` — The URL location of the image.

## See Also

### Creating a filter

- [+ filterWithCVPixelBuffer:properties:](<init(cvpixelbuffer_properties_)-6209q.md>) — Creates a RAW filter from the pixel buffer and its properties that you specify.
- [+ filterWithImageData:identifierHint:](<init(imagedata_identifierhint_).md>) — Creates a RAW filter from the image data and type hint that you specify.
