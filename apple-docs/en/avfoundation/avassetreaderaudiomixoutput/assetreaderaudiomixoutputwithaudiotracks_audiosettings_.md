---
title: 'assetReaderAudioMixOutputWithAudioTracks:audioSettings:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreaderaudiomixoutput/assetreaderaudiomixoutputwithaudiotracks:audiosettings:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/assetreaderaudiomixoutputwithaudiotracks:audiosettings:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderaudiomixoutput/assetreaderaudiomixoutputwithaudiotracks%3Aaudiosettings%3A.json'
content_hash: 'sha256:bc5dfb8b479c1dcb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderAudioMixOutput](../avassetreaderaudiomixoutput.md)

# assetReaderAudioMixOutputWithAudioTracks:audioSettings:

<sub>Type Method</sub>

Creates an object that reads mixed audio from the specified audio tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetReaderAudioMixOutputWithAudioTracks:(NSArray<AVAssetTrack *> *) audioTracks audioSettings:(NSDictionary<NSString *,id> *) audioSettings;
```

## Parameters

- `audioTracks` — An array of track objects of type [AVMediaTypeAudio](../avmediatype/audio.md) from which to source the sample buffers to mix.

- `audioSettings` — Optional audio settings to use for audio output. Pass `nil` to receive the decoded samples in an uncompressed format. To determine the specific format, examine the value of the sample buffer’s [formatDescription](../../coremedia/cmsamplebuffer/formatdescription.md) property. For non-`nil` audio settings, the dictionary must contain values for the [Linear PCM format settings](../linear-pcm-format-settings.md) keys. The output doesn’t support the [AVSampleRateConverterAudioQualityKey](../../avfaudio/avsamplerateconverteraudioqualitykey.md) constant.

## Return Value

A new audio mix output, or `nil` if initialization fails.

## See Also

### Creating an audio mix output

- [- initWithAudioTracks:audioSettings:](<init(audiotracks_audiosettings_).md>) — Creates an object that reads mixed audio from the specified audio tracks.
