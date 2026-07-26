---
title: audioSampleIsIndependentlyDecodable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplecursoraudiodependencyinfo/audiosampleisindependentlydecodable
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursoraudiodependencyinfo/audiosampleisindependentlydecodable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursoraudiodependencyinfo/audiosampleisindependentlydecodable.json'
content_hash: 'sha256:62c4e74a596628a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursorAudioDependencyInfo](../avsamplecursoraudiodependencyinfo.md)

# audioSampleIsIndependentlyDecodable

<sub>Instance Property</sub>

A Boolean value indicating whether the sample is independently decodable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var audioSampleIsIndependentlyDecodable: ObjCBool
```

## Discussion

The value of this property is [true](../../swift/true.md) for Immediate Playout Frames (IPFs) and Independent Frames (IFs).

## See Also

### Querying independent decodability

- [audioSamplePacketRefreshCount](audiosamplepacketrefreshcount.md) — The number of samples, starting at the current sample, that must be fed to the decoder to achieve full decoder refresh.
