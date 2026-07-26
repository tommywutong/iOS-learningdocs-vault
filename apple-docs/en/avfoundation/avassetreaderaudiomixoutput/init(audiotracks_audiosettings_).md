---
title: 'init(audioTracks:audioSettings:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreaderaudiomixoutput/init(audiotracks:audiosettings:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/init(audiotracks:audiosettings:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderaudiomixoutput/init%28audiotracks%3Aaudiosettings%3A%29.json'
content_hash: 'sha256:39d74a0deb305f4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderAudioMixOutput](../avassetreaderaudiomixoutput.md)

# init(audioTracks:audioSettings:)

<sub>Initializer</sub>

Creates an object that reads mixed audio from the specified audio tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(audioTracks: [AVAssetTrack], audioSettings: [String : Any]?)
```

## Parameters

- `audioTracks` — An array of track objects of type [AVMediaTypeAudio](../avmediatype/audio.md) from which to source the sample buffers to mix.

- `audioSettings` — Optional audio settings to use for audio output. Pass `nil` to receive the decoded samples in an uncompressed format. To determine the specific format, examine the value of the sample buffer’s [formatDescription](../../coremedia/cmsamplebuffer/formatdescription.md) property. For non-`nil` audio settings, the dictionary must contain values for the [Linear PCM format settings](../linear-pcm-format-settings.md) keys. The output doesn’t support the [AVSampleRateConverterAudioQualityKey](../../avfaudio/avsamplerateconverteraudioqualitykey.md) constant.
