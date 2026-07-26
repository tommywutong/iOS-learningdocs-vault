---
title: duration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/duration
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/duration.json'
content_hash: 'sha256:5d598b450a05a4a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# duration

<sub>Instance Property</sub>

A time value that indicates the asset’s duration.

> [!warning] Deprecated
> Load the value of [duration](../avpartialasyncproperty/duration.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var duration: CMTime { get }
```

## Discussion

If you initialized the asset by passing the [AVURLAssetPreferPreciseDurationAndTimingKey](../avurlassetpreferprecisedurationandtimingkey.md) initialization option, this property value provides the asset’s precise duration; otherwise, it provides a best-available estimate. You can determine the value’s accuracy by querying the asset’s [providesPreciseDurationAndTiming](providesprecisedurationandtiming.md) property.
