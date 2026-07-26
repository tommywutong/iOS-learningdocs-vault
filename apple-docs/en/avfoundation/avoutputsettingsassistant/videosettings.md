---
title: videoSettings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avoutputsettingsassistant/videosettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/videosettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avoutputsettingsassistant/videosettings.json'
content_hash: 'sha256:cb7874acca90ff2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVOutputSettingsAssistant](../avoutputsettingsassistant.md)

# videoSettings

<sub>Instance Property</sub>

A video settings dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var videoSettings: [String : Any]? { get }
```

## Discussion

The value of this property may change as a result of setting a new value for the [sourceVideoFormat](sourcevideoformat.md) property. See [Video settings](../video-settings.md) for the supported keys and values.

## See Also

### Configuring output settings

- [outputFileType](outputfiletype.md) — A uniform type identifier (UTI) that indicates the type of file to write.
- [audioSettings](audiosettings.md) — An audio settings dictionary.
- [sourceAudioFormat](sourceaudioformat.md) — The format of the source audio data.
- [sourceVideoFormat](sourcevideoformat.md) — The format of the source video data.
- [sourceVideoMinFrameDuration](sourcevideominframeduration.md) — A time value that describes the minimum frame duration of the video data.
- [sourceVideoAverageFrameDuration](sourcevideoaverageframeduration.md) — A time value that describes the average frame duration of the video data.
