---
title: isEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/isenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/isenabled.json'
content_hash: 'sha256:b0822d603af72ce4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the track’s container enables it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEnabled: Bool { get }
```

## Discussion

For file-based media, you can change its [enabled](../avplayeritemtrack/isenabled.md) presentation state using [AVPlayerItemTrack](../avplayeritemtrack.md).

## See Also

### Accessing track information

- [isPlayable](isplayable.md) — A Boolean value that indicates whether the track is playable in the current environment.
- [isDecodable](isdecodable.md) — A Boolean value that indicates whether the track is decodable in the current environment.
- [isSelfContained](isselfcontained.md) — A Boolean value that indicates whether this track references sample data only within its container file.
- [totalSampleDataLength](totalsampledatalength.md) — The total number of bytes of sample data the track requires.
- [- hasMediaCharacteristic:](<hasmediacharacteristic(__).md>) — Returns a Boolean value that indicates whether the track references media with the specified media characteristic.
