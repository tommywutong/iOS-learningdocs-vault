---
title: sourceVideoFormat
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avoutputsettingsassistant/sourcevideoformat
source_url: 'https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/sourcevideoformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avoutputsettingsassistant/sourcevideoformat.json'
content_hash: 'sha256:6cd99b43dc1ab2fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVOutputSettingsAssistant](../avoutputsettingsassistant.md)

# sourceVideoFormat

<sub>Instance Property</sub>

The format of the source video data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sourceVideoFormat: CMVideoFormatDescription? { get set }
```

## Discussion

The default value is `nil`, which means the assistant doesn’t know the video format. Setting a value for this property helps the assistant generate more complete video settings. After setting a value, requery the [videoSettings](videosettings.md) property to get the latest values.

## See Also

### Configuring output settings

- [outputFileType](outputfiletype.md) — A uniform type identifier (UTI) that indicates the type of file to write.
- [audioSettings](audiosettings.md) — An audio settings dictionary.
- [sourceAudioFormat](sourceaudioformat.md) — The format of the source audio data.
- [videoSettings](videosettings.md) — A video settings dictionary.
- [sourceVideoMinFrameDuration](sourcevideominframeduration.md) — A time value that describes the minimum frame duration of the video data.
- [sourceVideoAverageFrameDuration](sourcevideoaverageframeduration.md) — A time value that describes the average frame duration of the video data.
