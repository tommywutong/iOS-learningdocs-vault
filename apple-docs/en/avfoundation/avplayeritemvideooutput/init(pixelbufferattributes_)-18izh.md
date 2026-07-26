---
title: 'init(pixelBufferAttributes:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemvideooutput/init(pixelbufferattributes:)-18izh'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/init(pixelbufferattributes:)-18izh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemvideooutput/init%28pixelbufferattributes%3A%29-18izh.json'
content_hash: 'sha256:7c6780ac217028c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemVideoOutput](../avplayeritemvideooutput.md)

# init(pixelBufferAttributes:)

<sub>Initializer</sub>

Initializes an instance of AVPlayerItemVideoOutput, using the specified pixel buffer attributes, for video image output

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(pixelBufferAttributes: CVPixelBufferAttributes)
```

## Discussion

- pixelBufferAttributes: The client requirements for output pixel buffers

## See Also

### Creating a video output

- [- initWithPixelBufferAttributes:](<init(pixelbufferattributes_)-7n7v8.md>) — Creates a video output object using the specified pixel buffer attributes. _(deprecated)_
- [- initWithOutputSettings:](<init(outputsettings_).md>) — Creates a video output object initialized with the specified output settings.
