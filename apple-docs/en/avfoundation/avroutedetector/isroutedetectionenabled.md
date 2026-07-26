---
title: isRouteDetectionEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avroutedetector/isroutedetectionenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avroutedetector/isroutedetectionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avroutedetector/isroutedetectionenabled.json'
content_hash: 'sha256:122f6ed1d284570f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVRouteDetector](../avroutedetector.md)

# isRouteDetectionEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether route detection is in an enabled state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isRouteDetectionEnabled: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md).

> [!note] Note
> Enabling route detection significantly increases power consumption. Turn it off when you no longer need it.

## See Also

### Detecting routes

- [multipleRoutesDetected](multipleroutesdetected.md) — A Boolean value that indicates whether the object detects more than one playback route.
- [AVRouteDetectorMultipleRoutesDetectedDidChange](../../foundation/nsnotification/name-swift.struct/avroutedetectormultipleroutesdetecteddidchange.md) — A notification the system posts when changes occur to its detected routes.
