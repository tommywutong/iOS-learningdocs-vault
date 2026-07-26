---
title: audioSettings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreaderaudiomixoutput/audiosettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/audiosettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderaudiomixoutput/audiosettings.json'
content_hash: 'sha256:4e16d5bd25f429ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderAudioMixOutput](../avassetreaderaudiomixoutput.md)

# audioSettings

<sub>Instance Property</sub>

The audio settings that the output uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var audioSettings: [String : Any]? { get }
```

## Discussion

The dictionary must contain values for the keys in [Linear PCM format settings](../linear-pcm-format-settings.md).

Setting the property value to `nil` indicates that the output returns audio samples in an uncompressed format.

## See Also

### Inspecting an output

- [audioTracks](audiotracks.md) — The tracks from which the output reads audio.
