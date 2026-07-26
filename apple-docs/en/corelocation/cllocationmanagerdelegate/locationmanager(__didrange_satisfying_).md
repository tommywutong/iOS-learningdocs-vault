---
title: 'locationManager(_:didRange:satisfying:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didrange:satisfying:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didrange:satisfying:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Adidrange%3Asatisfying%3A%29.json'
content_hash: 'sha256:e2b500c78f201be5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:didRange:satisfying:)

<sub>Instance Method</sub>

Tells the delegate that the location manager detected at least one beacon that satisfies the provided constraint.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, didRange beacons: [CLBeacon], satisfying beaconConstraint: CLBeaconIdentityConstraint)
```

## Parameters

- `manager` — The [CLLocationManager](../cllocationmanager.md) that corresponds to this delegate.

- `beacons` — An array of [CLBeacon](../clbeacon.md) objects.

- `beaconConstraint` — The [CLBeaconIdentityConstraint](../clbeaconidentityconstraint.md) that describes the characteristics of the beacons the location manager is looking for.

## See Also

### Receiving beacon-related updates

- [- locationManager:didFailRangingBeaconsForConstraint:error:](<locationmanager(__didfailrangingfor_error_).md>) — Tells the delegate that the location manager couldn’t detect any beacons that satisfy the provided constraint.
- [- locationManager:didRangeBeacons:inRegion:](<locationmanager(__didrangebeacons_in_).md>) — Tells the delegate that one or more beacons are in range. _(deprecated)_
- [- locationManager:rangingBeaconsDidFailForRegion:withError:](<locationmanager(__rangingbeaconsdidfailfor_witherror_).md>) — Tells the delegate that an error occurred while gathering ranging information for a set of beacons. _(deprecated)_
