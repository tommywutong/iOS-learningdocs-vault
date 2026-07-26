---
title: maximumRegionMonitoringDistance
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/maximumregionmonitoringdistance
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/maximumregionmonitoringdistance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/maximumregionmonitoringdistance.json'
content_hash: 'sha256:e226b9c2d0f82db9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# maximumRegionMonitoringDistance

<sub>Instance Property</sub>

The largest boundary distance that can be assigned to a region.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var maximumRegionMonitoringDistance: CLLocationDistance { get }
```

## Discussion

This property defines the largest boundary distance allowed from a region’s center point. Attempting to monitor a region with a distance larger than this value causes the location manager to send a [kCLErrorRegionMonitoringFailure](../clerror-swift.struct/code/regionmonitoringfailure.md) error to the delegate.

If region monitoring is unavailable or not supported, the value in this property is `-1`.

## See Also

### Running the region-monitoring service

- [monitoredRegions](monitoredregions.md) — The set of shared regions monitored by all location-manager objects.
