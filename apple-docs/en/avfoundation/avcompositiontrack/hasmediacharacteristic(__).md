---
title: 'hasMediaCharacteristic(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcompositiontrack/hasmediacharacteristic(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/hasmediacharacteristic(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/hasmediacharacteristic%28_%3A%29.json'
content_hash: 'sha256:ffdfea019ddd34a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# hasMediaCharacteristic(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the track references media with the specified media characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

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
- [isEnabled](isenabled.md) — A Boolean value that indicates whether the track’s container enables it.
- [isSelfContained](isselfcontained.md) — A Boolean value that indicates whether this track references sample data only within its container file.
- [totalSampleDataLength](totalsampledatalength.md) — The total number of bytes of sample data the track requires.
