---
title: isEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/isenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/isenabled.json'
content_hash: 'sha256:91359b346b4cc25c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the track’s container enables it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

For file-based media, you can change its [enabled](../avplayeritemtrack/isenabled.md) presentation state using [AVPlayerItemTrack](../avplayeritemtrack.md).

## See Also

### Accessing track information

- [isPlayable](isplayable.md) — A Boolean value that indicates whether the track is playable in the current environment.
- [isDecodable](isdecodable.md) — A Boolean value that indicates whether the track is decodable in the current environment.
- [isSelfContained](isselfcontained.md) — A Boolean value that indicates whether this track references sample data only within its container file.
- [hasProtectedContent](hasprotectedcontent.md) — A Boolean value that indicates whether a track contains protected content.
- [totalSampleDataLength](totalsampledatalength.md) — The total number of bytes of sample data the track requires.
- [- hasMediaCharacteristic:](<hasmediacharacteristic(__).md>) — Returns a Boolean value that indicates whether the track references media with the specified media characteristic.
