---
title: totalSampleDataLength
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/totalsampledatalength
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/totalsampledatalength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/totalsampledatalength.json'
content_hash: 'sha256:32f3625df7c49f1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# totalSampleDataLength

<sub>Instance Property</sub>

The total number of bytes of sample data the track requires.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var totalSampleDataLength: Int64 { get }
```

## Discussion

The value may be `0` if the framework can’t determine the total sample data length.

## See Also

### Accessing track information

- [isPlayable](isplayable.md) — A Boolean value that indicates whether the track is playable in the current environment.
- [isDecodable](isdecodable.md) — A Boolean value that indicates whether the track is decodable in the current environment.
- [isEnabled](isenabled.md) — A Boolean value that indicates whether the track’s container enables it.
- [isSelfContained](isselfcontained.md) — A Boolean value that indicates whether this track references sample data only within its container file.
- [- hasMediaCharacteristic:](<hasmediacharacteristic(__).md>) — Returns a Boolean value that indicates whether the track references media with the specified media characteristic.
