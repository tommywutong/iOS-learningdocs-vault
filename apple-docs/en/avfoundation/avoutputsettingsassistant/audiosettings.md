---
title: audioSettings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avoutputsettingsassistant/audiosettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/audiosettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avoutputsettingsassistant/audiosettings.json'
content_hash: 'sha256:acfd18b5815beb6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVOutputSettingsAssistant](../avoutputsettingsassistant.md)

# audioSettings

<sub>Instance Property</sub>

An audio settings dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var audioSettings: [String : Any]? { get }
```

## Discussion

The value of this property may change as a result of setting a new value for the [sourceAudioFormat](sourceaudioformat.md) property. See [Audio settings](../audio-settings.md) for keys and values.

## See Also

### Configuring output settings

- [outputFileType](outputfiletype.md) — A uniform type identifier (UTI) that indicates the type of file to write.
- [sourceAudioFormat](sourceaudioformat.md) — The format of the source audio data.
- [videoSettings](videosettings.md) — A video settings dictionary.
- [sourceVideoFormat](sourcevideoformat.md) — The format of the source video data.
- [sourceVideoMinFrameDuration](sourcevideominframeduration.md) — A time value that describes the minimum frame duration of the video data.
- [sourceVideoAverageFrameDuration](sourcevideoaverageframeduration.md) — A time value that describes the average frame duration of the video data.
