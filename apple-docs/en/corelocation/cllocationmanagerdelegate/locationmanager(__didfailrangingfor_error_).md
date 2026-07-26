---
title: 'locationManager(_:didFailRangingFor:error:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didfailrangingfor:error:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didfailrangingfor:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Adidfailrangingfor%3Aerror%3A%29.json'
content_hash: 'sha256:3f6bbfe60edaadc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:didFailRangingFor:error:)

<sub>Instance Method</sub>

Tells the delegate that the location manager couldn’t detect any beacons that satisfy the provided constraint.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, didFailRangingFor beaconConstraint: CLBeaconIdentityConstraint, error: any Error)
```

## Parameters

- `manager` — The [CLLocationManager](../cllocationmanager.md) that corresponds to this delegate.

- `beaconConstraint` — The [CLBeaconIdentityConstraint](../clbeaconidentityconstraint.md) that describes the characteristics of the beacons the location manager is looking for.

- `error` — An [NSError](../../foundation/nserror.md) object that describes the error.

## See Also

### Receiving beacon-related updates

- [- locationManager:didRangeBeacons:satisfyingConstraint:](<locationmanager(__didrange_satisfying_).md>) — Tells the delegate that the location manager detected at least one beacon that satisfies the provided constraint.
- [- locationManager:didRangeBeacons:inRegion:](<locationmanager(__didrangebeacons_in_).md>) — Tells the delegate that one or more beacons are in range. _(deprecated)_
- [- locationManager:rangingBeaconsDidFailForRegion:withError:](<locationmanager(__rangingbeaconsdidfailfor_witherror_).md>) — Tells the delegate that an error occurred while gathering ranging information for a set of beacons. _(deprecated)_
