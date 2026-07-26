---
title: 'locationManager(_:didStartMonitoringFor:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didstartmonitoringfor:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didstartmonitoringfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Adidstartmonitoringfor%3A%29.json'
content_hash: 'sha256:a6c22ae4372c0a7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:didStartMonitoringFor:)

<sub>Instance Method</sub>

Tells the delegate that a new region is being monitored.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, didStartMonitoringFor region: CLRegion)
```

## Parameters

- `manager` — The location manager object reporting the event.

- `region` — The region that is being monitored.

## See Also

### Receiving region-related updates

- [- locationManager:didEnterRegion:](<locationmanager(__didenterregion_).md>) — Tells the delegate that the user entered the specified region.
- [- locationManager:didExitRegion:](<locationmanager(__didexitregion_).md>) — Tells the delegate that the user left the specified region.
- [- locationManager:didDetermineState:forRegion:](<locationmanager(__diddeterminestate_for_).md>) — Tells the delegate about the state of the specified region.
- [- locationManager:monitoringDidFailForRegion:withError:](<locationmanager(__monitoringdidfailfor_witherror_).md>) — Tells the delegate that a region monitoring error occurred.
- [CLRegionState](../clregionstate.md) — Constants that reflect the relationship of the current location to the region boundaries.
