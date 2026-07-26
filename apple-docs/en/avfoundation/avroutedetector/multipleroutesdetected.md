---
title: multipleRoutesDetected
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avroutedetector/multipleroutesdetected
source_url: 'https://developer.apple.com/documentation/avfoundation/avroutedetector/multipleroutesdetected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avroutedetector/multipleroutesdetected.json'
content_hash: 'sha256:3ee88e53ac3e1fd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVRouteDetector](../avroutedetector.md)

# multipleRoutesDetected

<sub>Instance Property</sub>

A Boolean value that indicates whether the object detects more than one playback route.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var multipleRoutesDetected: Bool { get }
```

## Discussion

The system posts a [AVRouteDetectorMultipleRoutesDetectedDidChangeNotification](../avroutedetectormultipleroutesdetecteddidchangenotification.md) notification when this property value changes.

## See Also

### Detecting routes

- [routeDetectionEnabled](isroutedetectionenabled.md) — A Boolean value that indicates whether route detection is in an enabled state.
- [AVRouteDetectorMultipleRoutesDetectedDidChange](../../foundation/nsnotification/name-swift.struct/avroutedetectormultipleroutesdetecteddidchange.md) — A notification the system posts when changes occur to its detected routes.
