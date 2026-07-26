---
title: regionMonitoringFailure
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clerror-swift.struct/regionmonitoringfailure
source_url: 'https://developer.apple.com/documentation/corelocation/clerror-swift.struct/regionmonitoringfailure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clerror-swift.struct/regionmonitoringfailure.json'
content_hash: 'sha256:bcba0ed2fd5e70b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLError](../clerror-swift.struct.md)

# regionMonitoringFailure

<sub>Type Property</sub>

A constant that indicates the location manager failed to monitor a registered region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var regionMonitoringFailure: CLError.Code { get }
```

## Discussion

Monitoring can fail if the app exceeds the maximum number of regions that it can monitor simultaneously. Monitoring can also fail if the region’s radius distance is too large.

## See Also

### Getting region monitoring errors

- [regionMonitoringDenied](regionmonitoringdenied.md) — A constant that indicates the user denied access to the region monitoring service.
- [regionMonitoringSetupDelayed](regionmonitoringsetupdelayed.md) — A constant that indicates Core Location couldn’t initialize the region monitoring feature immediately.
- [regionMonitoringResponseDelayed](regionmonitoringresponsedelayed.md) — A constant that indicates Core Location will deliver events but they may be delayed.
