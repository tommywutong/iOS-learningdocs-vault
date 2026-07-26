---
title: 'init(mediaType:outputSettings:sourceFormatHint:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/init(mediatype:outputsettings:sourceformathint:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/init(mediatype:outputsettings:sourceformathint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/init%28mediatype%3Aoutputsettings%3Asourceformathint%3A%29.json'
content_hash: 'sha256:98d90906026df9e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# init(mediaType:outputSettings:sourceFormatHint:)

<sub>Initializer</sub>

Creates an input that appends sample buffers of the specified type and format hint to the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(mediaType: AVMediaType, outputSettings: [String : Any]?, sourceFormatHint: CMFormatDescription?)
```

## Parameters

- `mediaType` — The type of media that an input accepts.

- `outputSettings` — The settings to use for encoding the media you append to the output. Create an output settings dictionary manually, or use [AVOutputSettingsAssistant](../avoutputsettingsassistant.md) to create preset-based settings.

- `sourceFormatHint` — A hint about the format of the media data to append. The input uses the source format hint to fill in missing output settings. If you specify a hint, you only need to specify [AVFormatIDKey](../../avfaudio/avformatidkey.md) for the audio output settings, and [AVVideoCodecKey](../avvideocodeckey.md) is the only required key for video output settings. The system raises an error if the format description isn’t valid for the indicated media type.

## Discussion

To guarantee successful file writing, ensure that sample buffers you append are of the specified format.

## See Also

### Creating an input

- [- initWithMediaType:outputSettings:](<init(mediatype_outputsettings_).md>) — Creates an input to append sample buffers of the specified type to the output file.
