---
title: sourceVideoAverageFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avoutputsettingsassistant/sourcevideoaverageframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/sourcevideoaverageframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avoutputsettingsassistant/sourcevideoaverageframeduration.json'
content_hash: 'sha256:b9bd9922d9e27552'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVOutputSettingsAssistant](../avoutputsettingsassistant.md)

# sourceVideoAverageFrameDuration

<sub>Instance Property</sub>

A time value that describes the average frame duration of the video data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sourceVideoAverageFrameDuration: CMTime { get set }
```

## Discussion

Setting this property enables the output settings assistant to generate more complete video settings. After setting a value, requery the [videoSettings](videosettings.md) property to get the latest values.

The default value is `1/30`, which means the output settings assistant assumes that your source video has a frame rate of 30fps.

## See Also

### Configuring output settings

- [outputFileType](outputfiletype.md) — A uniform type identifier (UTI) that indicates the type of file to write.
- [audioSettings](audiosettings.md) — An audio settings dictionary.
- [sourceAudioFormat](sourceaudioformat.md) — The format of the source audio data.
- [videoSettings](videosettings.md) — A video settings dictionary.
- [sourceVideoFormat](sourcevideoformat.md) — The format of the source video data.
- [sourceVideoMinFrameDuration](sourcevideominframeduration.md) — A time value that describes the minimum frame duration of the video data.
