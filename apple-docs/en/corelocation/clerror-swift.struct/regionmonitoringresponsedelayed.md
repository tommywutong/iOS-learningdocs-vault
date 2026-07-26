---
title: regionMonitoringResponseDelayed
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clerror-swift.struct/regionmonitoringresponsedelayed
source_url: 'https://developer.apple.com/documentation/corelocation/clerror-swift.struct/regionmonitoringresponsedelayed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clerror-swift.struct/regionmonitoringresponsedelayed.json'
content_hash: 'sha256:690bbd1f006cdf57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLError](../clerror-swift.struct.md)

# regionMonitoringResponseDelayed

<sub>Type Property</sub>

A constant that indicates Core Location will deliver events but they may be delayed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var regionMonitoringResponseDelayed: CLError.Code { get }
```

## Discussion

The user information dictionary might contain an alternate region that you can monitor instead. Use the [alternateRegion](alternateregion.md) property to retrieve the [CLRegion](../clregion.md) object.

## See Also

### Getting region monitoring errors

- [regionMonitoringDenied](regionmonitoringdenied.md) — A constant that indicates the user denied access to the region monitoring service.
- [regionMonitoringFailure](regionmonitoringfailure.md) — A constant that indicates the location manager failed to monitor a registered region.
- [regionMonitoringSetupDelayed](regionmonitoringsetupdelayed.md) — A constant that indicates Core Location couldn’t initialize the region monitoring feature immediately.
