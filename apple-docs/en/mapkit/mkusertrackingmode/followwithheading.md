---
title: MKUserTrackingMode.followWithHeading
framework: MapKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkusertrackingmode/followwithheading
source_url: 'https://developer.apple.com/documentation/mapkit/mkusertrackingmode/followwithheading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkusertrackingmode/followwithheading.json'
content_hash: 'sha256:b62b17757d6eb847'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKUserTrackingMode](../mkusertrackingmode.md)

# MKUserTrackingMode.followWithHeading

<sub>Case</sub>

The map follows the user’s location and rotates when the heading changes.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case followWithHeading
```

## Discussion

This mode requires the device to have an available magnetometer. This mode isn’t available for compatible iPad or iPhone apps running in visionOS.

## See Also

### Constants

- [MKUserTrackingModeNone](none.md) — The map doesn’t follow the user’s location.
- [MKUserTrackingModeFollow](follow.md) — The map follows the user location.
