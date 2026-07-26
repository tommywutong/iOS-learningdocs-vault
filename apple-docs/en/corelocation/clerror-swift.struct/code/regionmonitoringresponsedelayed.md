---
title: CLError.Code.regionMonitoringResponseDelayed
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clerror-swift.struct/code/regionmonitoringresponsedelayed
source_url: 'https://developer.apple.com/documentation/corelocation/clerror-swift.struct/code/regionmonitoringresponsedelayed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clerror-swift.struct/code/regionmonitoringresponsedelayed.json'
content_hash: 'sha256:de54460f612ebdb5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Location](../../../corelocation.md) · [CLError](../../clerror-swift.struct.md) · [Code](../code.md)

# CLError.Code.regionMonitoringResponseDelayed

<sub>Case</sub>

A constant that indicates Core Location will deliver events but they may be delayed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case regionMonitoringResponseDelayed
```

## Discussion

The user information dictionary might contain an alternate region that you can monitor instead. Use [kCLErrorUserInfoAlternateRegionKey](../../kclerroruserinfoalternateregionkey.md) to retrieve the [CLRegion](../../clregion.md) object.

## See Also

### Getting region monitoring errors

- [kCLErrorRegionMonitoringDenied](regionmonitoringdenied.md) — A constant that indicates the user denied access to the region monitoring service.
- [kCLErrorRegionMonitoringFailure](regionmonitoringfailure.md) — A constant that indicates the location manager failed to monitor a registered region.
- [kCLErrorRegionMonitoringSetupDelayed](regionmonitoringsetupdelayed.md) — A constant that indicates Core Location failed to initialize the region monitoring feature.
