---
title: 'init(outputSettings:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemvideooutput/init(outputsettings:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/init(outputsettings:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemvideooutput/init%28outputsettings%3A%29.json'
content_hash: 'sha256:bbf2bd60e7b3ca9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemVideoOutput](../avplayeritemvideooutput.md)

# init(outputSettings:)

<sub>Initializer</sub>

Creates a video output object initialized with the specified output settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(outputSettings: [String : any Sendable]?)
```

## Parameters

- `outputSettings` — The client requirements for output [CVPixelBuffer](../../corevideo/cvpixelbuffer-q2e.md) objects, expressed using the constants in `AVVideoSettings.h`.

## Discussion

For uncompressed video output, start with `kCVPixelBuffer*` keys in `<CoreVideo/CVPixelBuffer.h>`. In addition to the keys in `CVPixelBuffer.h`, uncompressed video settings dictionaries may also provide a value for [AVVideoAllowWideColorKey](../avvideoallowwidecolorkey.md).

## See Also

### Creating a video output

- [- initWithPixelBufferAttributes:](<init(pixelbufferattributes_)-7n7v8.md>) — Creates a video output object using the specified pixel buffer attributes. _(deprecated)_
- [init(pixelBufferAttributes:)](<init(pixelbufferattributes_)-18izh.md>) — Initializes an instance of AVPlayerItemVideoOutput, using the specified pixel buffer attributes, for video image output
