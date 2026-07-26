---
title: AVRouteDetector
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avroutedetector
source_url: 'https://developer.apple.com/documentation/avfoundation/avroutedetector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avroutedetector.json'
content_hash: 'sha256:763dba45a4e5f38f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVRouteDetector

<sub>Class</sub>

An object that detects available media playback routes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVRouteDetector
```

## Overview

If you enable route detection, the object reports whether it detects multiple playback routes. If it does, use [AVRoutePickerView](../avkit/avroutepickerview.md) to present the UI for the user to select an appropriate route.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Detecting routes

- [routeDetectionEnabled](avroutedetector/isroutedetectionenabled.md) — A Boolean value that indicates whether route detection is in an enabled state.
- [multipleRoutesDetected](avroutedetector/multipleroutesdetected.md) — A Boolean value that indicates whether the object detects more than one playback route.
- [AVRouteDetectorMultipleRoutesDetectedDidChange](../foundation/nsnotification/name-swift.struct/avroutedetectormultipleroutesdetecteddidchange.md) — A notification the system posts when changes occur to its detected routes.

### Deprecated

- [detectsCustomRoutes](avroutedetector/detectscustomroutes.md) — A Boolean value that indicates whether route detection includes custom routes. _(deprecated)_
