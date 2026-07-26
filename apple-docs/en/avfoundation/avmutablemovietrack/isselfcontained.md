---
title: isSelfContained
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/isselfcontained
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/isselfcontained'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/isselfcontained.json'
content_hash: 'sha256:dddcc298e605abb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# isSelfContained

<sub>Instance Property</sub>

A Boolean value that indicates whether this track references sample data only within its container file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var isSelfContained: Bool { get }
```

## See Also

### Accessing track information

- [isPlayable](isplayable.md) — A Boolean value that indicates whether the track is playable in the current environment.
- [isDecodable](isdecodable.md) — A Boolean value that indicates whether the track is decodable in the current environment.
- [enabled](isenabled.md) — A Boolean value that indicates whether the track’s container enables it.
- [hasProtectedContent](hasprotectedcontent.md) — A Boolean value that indicates whether a track contains protected content.
- [totalSampleDataLength](totalsampledatalength.md) — The total number of bytes of sample data the track requires.
- [- hasMediaCharacteristic:](<hasmediacharacteristic(__).md>) — Returns a Boolean value that indicates whether the track references media with the specified media characteristic.
