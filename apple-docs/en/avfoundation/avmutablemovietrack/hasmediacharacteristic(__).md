---
title: 'hasMediaCharacteristic(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovietrack/hasmediacharacteristic(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/hasmediacharacteristic(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/hasmediacharacteristic%28_%3A%29.json'
content_hash: 'sha256:14a8fc3755cba605'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# hasMediaCharacteristic(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the track references media with the specified media characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func hasMediaCharacteristic(_ mediaCharacteristic: AVMediaCharacteristic) -> Bool
```

## Parameters

- `mediaCharacteristic` — The media characteristic of interest.

## Return Value

[true](../../swift/true.md) if the track references media with the specified characteristic; otherwise, [false](../../swift/false.md).

## See Also

### Accessing track information

- [isPlayable](isplayable.md) — A Boolean value that indicates whether the track is playable in the current environment.
- [isDecodable](isdecodable.md) — A Boolean value that indicates whether the track is decodable in the current environment.
- [enabled](isenabled.md) — A Boolean value that indicates whether the track’s container enables it.
- [isSelfContained](isselfcontained.md) — A Boolean value that indicates whether this track references sample data only within its container file.
- [hasProtectedContent](hasprotectedcontent.md) — A Boolean value that indicates whether a track contains protected content.
- [totalSampleDataLength](totalsampledatalength.md) — The total number of bytes of sample data the track requires.
