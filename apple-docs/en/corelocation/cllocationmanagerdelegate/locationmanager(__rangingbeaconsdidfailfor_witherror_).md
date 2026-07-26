---
title: 'locationManager(_:rangingBeaconsDidFailFor:withError:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.15+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:rangingbeaconsdidfailfor:witherror:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:rangingbeaconsdidfailfor:witherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Arangingbeaconsdidfailfor%3Awitherror%3A%29.json'
content_hash: 'sha256:c389d7214c5a3690'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:rangingBeaconsDidFailFor:withError:)

<sub>Instance Method</sub>

Tells the delegate that an error occurred while gathering ranging information for a set of beacons.

> [!warning] Deprecated
> Use [- locationManager:didFailRangingBeaconsForConstraint:error:](<locationmanager(__didfailrangingfor_error_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, rangingBeaconsDidFailFor region: CLBeaconRegion, withError error: any Error)
```

## Parameters

- `manager` — The location manager object reporting the event.

- `region` — The region object that encountered the error.

- `error` — An error object containing the error code that indicates why ranging failed.

## Discussion

Errors occur most often when registering a beacon region failed. If the region object itself is invalid or if it contains invalid data, the location manager calls this method to report the problem.

## See Also

### Receiving beacon-related updates

- [- locationManager:didRangeBeacons:satisfyingConstraint:](<locationmanager(__didrange_satisfying_).md>) — Tells the delegate that the location manager detected at least one beacon that satisfies the provided constraint.
- [- locationManager:didFailRangingBeaconsForConstraint:error:](<locationmanager(__didfailrangingfor_error_).md>) — Tells the delegate that the location manager couldn’t detect any beacons that satisfy the provided constraint.
- [- locationManager:didRangeBeacons:inRegion:](<locationmanager(__didrangebeacons_in_).md>) — Tells the delegate that one or more beacons are in range. _(deprecated)_
