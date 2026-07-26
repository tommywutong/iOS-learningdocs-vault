---
title: totalSampleDataLength
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/totalsampledatalength
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/totalsampledatalength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/totalsampledatalength.json'
content_hash: 'sha256:a84e89804fcd4bb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# totalSampleDataLength

<sub>Instance Property</sub>

The total number of bytes of sample data the track requires.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var totalSampleDataLength: Int64 { get }
```

## Discussion

The value may be `0` if the framework can’t determine the total sample data length.

## See Also

### Accessing track information

- [isPlayable](isplayable.md) — A Boolean value that indicates whether the track is playable in the current environment.
- [isDecodable](isdecodable.md) — A Boolean value that indicates whether the track is decodable in the current environment.
- [enabled](isenabled.md) — A Boolean value that indicates whether the track’s container enables it.
- [isSelfContained](isselfcontained.md) — A Boolean value that indicates whether this track references sample data only within its container file.
- [hasProtectedContent](hasprotectedcontent.md) — A Boolean value that indicates whether a track contains protected content.
- [- hasMediaCharacteristic:](<hasmediacharacteristic(__).md>) — Returns a Boolean value that indicates whether the track references media with the specified media characteristic.
