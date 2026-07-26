---
title: audioSamplePacketRefreshCount
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplecursoraudiodependencyinfo/audiosamplepacketrefreshcount
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursoraudiodependencyinfo/audiosamplepacketrefreshcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursoraudiodependencyinfo/audiosamplepacketrefreshcount.json'
content_hash: 'sha256:e5ffad22acc3b1f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursorAudioDependencyInfo](../avsamplecursoraudiodependencyinfo.md)

# audioSamplePacketRefreshCount

<sub>Instance Property</sub>

The number of samples, starting at the current sample, that must be fed to the decoder to achieve full decoder refresh.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var audioSamplePacketRefreshCount: Int
```

## Discussion

The value of [audioSampleIsIndependentlyDecodable](audiosampleisindependentlydecodable.md) must be [true](../../swift/true.md) for this value to take effect.

The value of this property is `0` for Immediate Playout Frames (IPFs).

## See Also

### Querying independent decodability

- [audioSampleIsIndependentlyDecodable](audiosampleisindependentlydecodable.md) — A Boolean value indicating whether the sample is independently decodable.
