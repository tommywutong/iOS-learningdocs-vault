---
title: outputSettings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreadertrackoutput/outputsettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/outputsettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreadertrackoutput/outputsettings.json'
content_hash: 'sha256:77f24a8ee5613f53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderTrackOutput](../avassetreadertrackoutput.md)

# outputSettings

<sub>Instance Property</sub>

The output settings for this track output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var outputSettings: [String : Any]? { get }
```

## Discussion

The value is a dictionary that contains values for audio and video settings keys. A value of `nil` indicates that the track output vends samples in their original format as stored in the target track. In that case, the track output skips decoding and returns the samples in decode order. A non-`nil` value causes the track output to decode the samples and return them in presentation order.

## See Also

### Inspecting an output

- [track](track.md) — The track from which the output reads sample buffers.
