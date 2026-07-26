---
title: 'locationManager(_:didDetermineState:for:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:diddeterminestate:for:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:diddeterminestate:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Adiddeterminestate%3Afor%3A%29.json'
content_hash: 'sha256:cf6cd8596cc87e89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:didDetermineState:for:)

<sub>Instance Method</sub>

Tells the delegate about the state of the specified region.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, didDetermineState state: CLRegionState, for region: CLRegion)
```

## Parameters

- `manager` — The location manager object reporting the event.

- `state` — The state of the specified region. For a list of possible values, see the [CLRegionState](../clregionstate.md) type.

- `region` — The region whose state was determined.

## Discussion

The location manager calls this method whenever there is a boundary transition for a region. It calls this method in addition to calling the  [- locationManager:didEnterRegion:](<locationmanager(__didenterregion_).md>) and [- locationManager:didExitRegion:](<locationmanager(__didexitregion_).md>) methods. The location manager also calls this method in response to a call to its [- requestStateForRegion:](<../cllocationmanager/requeststate(for_).md>) method, which runs asynchronously.

## See Also

### Receiving region-related updates

- [- locationManager:didEnterRegion:](<locationmanager(__didenterregion_).md>) — Tells the delegate that the user entered the specified region.
- [- locationManager:didExitRegion:](<locationmanager(__didexitregion_).md>) — Tells the delegate that the user left the specified region.
- [- locationManager:monitoringDidFailForRegion:withError:](<locationmanager(__monitoringdidfailfor_witherror_).md>) — Tells the delegate that a region monitoring error occurred.
- [- locationManager:didStartMonitoringForRegion:](<locationmanager(__didstartmonitoringfor_).md>) — Tells the delegate that a new region is being monitored.
- [CLRegionState](../clregionstate.md) — Constants that reflect the relationship of the current location to the region boundaries.
