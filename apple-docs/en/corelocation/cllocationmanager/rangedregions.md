---
title: rangedRegions
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, Mac Catalyst 14.0+（14.0 起废弃）, macOS 10.15+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/cllocationmanager/rangedregions
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/rangedregions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/rangedregions.json'
content_hash: 'sha256:b4dc372fc3b248c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# rangedRegions

<sub>Instance Property</sub>

The set of regions currently being tracked using ranging.

> [!warning] Deprecated
> Use [rangedBeaconConstraints](rangedbeaconconstraints.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var rangedRegions: Set<CLRegion> { get }
```

## Discussion

The objects in the set are instances of the [CLBeaconRegion](../clbeaconregion.md) class.

## Topics

### Related Documentation

- [- startRangingBeaconsInRegion:](<startrangingbeacons(in_).md>) — Starts the delivery of notifications for the specified beacon region. _(deprecated)_

## See Also

### Properties

- [headingAvailable](headingavailable-swift.property.md) — A Boolean value indicating whether the location manager is able to generate heading-related events. _(deprecated)_
- [locationServicesEnabled](locationservicesenabled-swift.property.md) — A Boolean value indicating whether location services are enabled on the device. _(deprecated)_
- [purpose](purpose.md) — An app-provided string that describes the reason for using location services. _(deprecated)_
