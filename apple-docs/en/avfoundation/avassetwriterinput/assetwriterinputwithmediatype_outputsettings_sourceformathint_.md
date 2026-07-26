---
title: 'assetWriterInputWithMediaType:outputSettings:sourceFormatHint:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinput/assetwriterinputwithmediatype:outputsettings:sourceformathint:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/assetwriterinputwithmediatype:outputsettings:sourceformathint:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/assetwriterinputwithmediatype%3Aoutputsettings%3Asourceformathint%3A.json'
content_hash: 'sha256:51a5a2dd3c3f3cd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# assetWriterInputWithMediaType:outputSettings:sourceFormatHint:

<sub>Type Method</sub>

Returns a new input that appends sample buffers of the specified type and format hint to the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetWriterInputWithMediaType:(AVMediaType) mediaType outputSettings:(NSDictionary<NSString *,id> *) outputSettings sourceFormatHint:(CMFormatDescriptionRef) sourceFormatHint;
```

## Parameters

- `mediaType` — The type of media that an input accepts.

- `outputSettings` — The settings to use for encoding the media you append to the output. Create an output settings dictionary manually, or use [AVOutputSettingsAssistant](../avoutputsettingsassistant.md) to create preset-based settings.

- `sourceFormatHint` — A hint about the format of the media data to append. The input uses the source format hint to fill in missing output settings. If you specify a hint, you only need to specify [AVFormatIDKey](../../avfaudio/avformatidkey.md) for the audio output settings, and [AVVideoCodecKey](../avvideocodeckey.md) is the only required key for video output settings. The system raises an error if the format description isn’t valid for the indicated media type.

## Return Value

A new asset writer input.

## Discussion

To guarantee successful file writing, ensure that sample buffers you append are of the specified format.

## See Also

### Creating an input

- [assetWriterInputWithMediaType:outputSettings:](assetwriterinputwithmediatype_outputsettings_.md) — Returns a new input to append sample buffers of the specified type to the output file.
- [- initWithMediaType:outputSettings:](<init(mediatype_outputsettings_).md>) — Creates an input to append sample buffers of the specified type to the output file.
- [- initWithMediaType:outputSettings:sourceFormatHint:](<init(mediatype_outputsettings_sourceformathint_).md>) — Creates an input that appends sample buffers of the specified type and format hint to the output file.
