---
title: 'init(pixelBufferAttributes:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+（27.0 起废弃）, iPadOS 6.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avplayeritemvideooutput/init(pixelbufferattributes:)-7n7v8'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/init(pixelbufferattributes:)-7n7v8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemvideooutput/init%28pixelbufferattributes%3A%29-7n7v8.json'
content_hash: 'sha256:fc28281a2b5eab38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemVideoOutput](../avplayeritemvideooutput.md)

# init(pixelBufferAttributes:)

<sub>Initializer</sub>

Creates a video output object using the specified pixel buffer attributes.

> [!warning] Deprecated
> Use init(pixelBufferAttributes: CVPixelBuffer.Attributes) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(pixelBufferAttributes: [String : any Sendable]? = nil)
```

## Parameters

- `pixelBufferAttributes` — The pixel buffer attributes required for video output. For a list of pixel buffer attributes you can include in this dictionary, see the `CVPixelBuffer.h` header file in the Core Video framework.

## Return Value

An initialized video output object.

## See Also

### Creating a video output

- [init(pixelBufferAttributes:)](<init(pixelbufferattributes_)-18izh.md>) — Initializes an instance of AVPlayerItemVideoOutput, using the specified pixel buffer attributes, for video image output
- [- initWithOutputSettings:](<init(outputsettings_).md>) — Creates a video output object initialized with the specified output settings.
