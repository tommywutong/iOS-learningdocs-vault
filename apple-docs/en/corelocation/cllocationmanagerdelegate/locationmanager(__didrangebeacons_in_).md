---
title: 'locationManager(_:didRangeBeacons:in:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.15+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didrangebeacons:in:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didrangebeacons:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Adidrangebeacons%3Ain%3A%29.json'
content_hash: 'sha256:15c274f73eaa8950'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:didRangeBeacons:in:)

<sub>Instance Method</sub>

Tells the delegate that one or more beacons are in range.

> [!warning] Deprecated
> Use [- locationManager:didRangeBeacons:satisfyingConstraint:](<locationmanager(__didrange_satisfying_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, didRangeBeacons beacons: [CLBeacon], in region: CLBeaconRegion)
```

## Parameters

- `manager` — The location manager object reporting the event.

- `beacons` — An array of [CLBeacon](../clbeacon.md) objects representing the beacons currently in range. If `beacons` is empty, you can assume that no beacons matching the specified region are in range. When a specific beacon is no longer in `beacons`, that beacon is no longer received by the device. You can use the information in the [CLBeacon](../clbeacon.md) objects to determine the range of each beacon and its identifying information.

- `region` — The region object containing the parameters that were used to locate the beacons.

## Discussion

The location manager calls this method when a new set of beacons becomes available in the specified region or when a beacon goes out of range. The location manager also calls this method when the range of a beacon changes; for example, when a beacon gets closer.

## See Also

### Receiving beacon-related updates

- [- locationManager:didRangeBeacons:satisfyingConstraint:](<locationmanager(__didrange_satisfying_).md>) — Tells the delegate that the location manager detected at least one beacon that satisfies the provided constraint.
- [- locationManager:didFailRangingBeaconsForConstraint:error:](<locationmanager(__didfailrangingfor_error_).md>) — Tells the delegate that the location manager couldn’t detect any beacons that satisfy the provided constraint.
- [- locationManager:rangingBeaconsDidFailForRegion:withError:](<locationmanager(__rangingbeaconsdidfailfor_witherror_).md>) — Tells the delegate that an error occurred while gathering ranging information for a set of beacons. _(deprecated)_
