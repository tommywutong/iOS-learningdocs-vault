---
title: 'init(cvPixelBuffer:properties:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cirawfilter/init(cvpixelbuffer:properties:)-6209q'
source_url: 'https://developer.apple.com/documentation/coreimage/cirawfilter/init(cvpixelbuffer:properties:)-6209q'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawfilter/init%28cvpixelbuffer%3Aproperties%3A%29-6209q.json'
content_hash: 'sha256:56d80448089da144'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRAWFilter](../cirawfilter.md)

# init(cvPixelBuffer:properties:)

<sub>Initializer</sub>

Creates a RAW filter from the pixel buffer and its properties that you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(cvPixelBuffer buffer: CVPixelBuffer, properties: [AnyHashable : Any])
```

## Parameters

- `buffer` — A Core Video pixel buffer.

- `properties` — A dictionary that defines the properties of the pixel buffer.

## See Also

### Creating a filter

- [+ filterWithImageData:identifierHint:](<init(imagedata_identifierhint_).md>) — Creates a RAW filter from the image data and type hint that you specify.
- [+ filterWithImageURL:](<init(imageurl_).md>) — Creates a RAW filter from the image at the URL location that you specify.
