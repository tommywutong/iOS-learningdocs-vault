---
title: providesPreciseDurationAndTiming
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/providesprecisedurationandtiming
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/providesprecisedurationandtiming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/providesprecisedurationandtiming.json'
content_hash: 'sha256:f296af1748ebf018'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# providesPreciseDurationAndTiming

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset provides precise duration and timing.

> [!warning] Deprecated
> Load the value of  [providesPreciseDurationAndTiming](../avpartialasyncproperty/providesprecisedurationandtiming.md)  asynchronously instead. ## Discussion This property value is [true](../../swift/true.md) if you initialized the asset with the [AVURLAssetPreferPreciseDurationAndTimingKey](../avurlassetpreferprecisedurationandtimingkey.md) initialization option, otherwise it’s [false](../../swift/false.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var providesPreciseDurationAndTiming: Bool { get }
```
