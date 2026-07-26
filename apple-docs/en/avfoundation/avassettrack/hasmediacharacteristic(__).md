---
title: 'hasMediaCharacteristic(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassettrack/hasmediacharacteristic(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/hasmediacharacteristic(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/hasmediacharacteristic%28_%3A%29.json'
content_hash: 'sha256:820c8bebe60dd1c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# hasMediaCharacteristic(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the track references media with the specified media characteristic.

> [!warning] Deprecated
> Load the value of [mediaCharacteristics](../avpartialasyncproperty/mediacharacteristics.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hasMediaCharacteristic(_ mediaCharacteristic: AVMediaCharacteristic) -> Bool
```

## Parameters

- `mediaCharacteristic` — The media characteristic of interest.

## Return Value

[true](../../swift/true.md) if the track references media with the specified characteristic, otherwise [false](../../swift/false.md).
