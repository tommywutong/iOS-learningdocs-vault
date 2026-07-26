---
title: monitoredRegions
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/monitoredregions
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/monitoredregions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/monitoredregions.json'
content_hash: 'sha256:a0ff9022f28582e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# monitoredRegions

<sub>Instance Property</sub>

The set of shared regions monitored by all location-manager objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var monitoredRegions: Set<CLRegion> { get }
```

## Discussion

You cannot add regions to this property directly. Instead, you must register regions by calling the [- startMonitoringForRegion:](<startmonitoring(for_).md>) method. The regions in this property are shared by all instances of the [CLLocationManager](../cllocationmanager.md) class in your app.

The objects in this set may not necessarily be the same objects you specified at registration time. Only the region data itself is maintained by the system. Therefore, the only way to uniquely identify a registered region is using its [identifier](../clregion/identifier.md) property.

The location manager persists region data between launches of your app. If your app is terminated and then relaunched, the contents of this property are repopulated with region objects that contain the previously registered data.

In a compatible iPad or iPhone app running in visionOS, the property contains an empty set.

## See Also

### Running the region-monitoring service

- [maximumRegionMonitoringDistance](maximumregionmonitoringdistance.md) — The largest boundary distance that can be assigned to a region.
