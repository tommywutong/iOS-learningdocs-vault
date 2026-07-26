---
title: tracks
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/tracks-44ptx
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/tracks-44ptx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/tracks-44ptx.json'
content_hash: 'sha256:8003f97a697bb633'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# tracks

<sub>Type Property</sub>

The tracks an asset contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var tracks: AVAsyncProperty<Root, [AVAssetTrack]> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

## See Also

### Loading tracks

- [- findCompatibleTrackForCompositionTrack:completionHandler:](<../avurlasset/findcompatibletrack(for_completionhandler_).md>) — Loads an asset track from which you can insert any time range into the composition track.
