---
title: requestedAudioFormat
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsamplebufferoutputaudioconfiguration/requestedaudioformat
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutputaudioconfiguration/requestedaudioformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsamplebufferoutputaudioconfiguration/requestedaudioformat.json'
content_hash: 'sha256:e5cf69cd6f020cf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemSampleBufferOutputAudioConfiguration](../avplayeritemsamplebufferoutputaudioconfiguration.md)

# requestedAudioFormat

<sub>Instance Property</sub>

Indicates the audio format in which the client prefers to receive the output sample buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var requestedAudioFormat: CMFormatDescription? { get set }
```

## Discussion

Must be a PCM format.

The output `CMSampleBuffers'` `CMFormatDescription` may not exactly match this format description, but it will match the parts described in the `AudioStreamBasicDescription`.

Specifying a PCM format is currently required.  In the future it may be optional.
