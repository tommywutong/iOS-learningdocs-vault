---
title: 'locationManager(_:didEnterRegion:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didenterregion:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didenterregion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Adidenterregion%3A%29.json'
content_hash: 'sha256:a7d746e2ad017c4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:didEnterRegion:)

<sub>Instance Method</sub>

Tells the delegate that the user entered the specified region.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, didEnterRegion region: CLRegion)
```

## Parameters

- `manager` — The location manager object reporting the event.

- `region` — An object containing information about the region that was entered.

## Discussion

Because regions are a shared application resource, every active location manager object delivers this message to its associated delegate. It doesn’t matter which location manager actually registered the specified region. If multiple location managers share a delegate object, that delegate receives the message multiple times.

The region object provided may not be the same one that was registered. As a result, you should never perform pointer-level comparisons to determine equality. Instead, use the region’s identifier string to determine if your delegate should respond.

## See Also

### Receiving region-related updates

- [- locationManager:didExitRegion:](<locationmanager(__didexitregion_).md>) — Tells the delegate that the user left the specified region.
- [- locationManager:didDetermineState:forRegion:](<locationmanager(__diddeterminestate_for_).md>) — Tells the delegate about the state of the specified region.
- [- locationManager:monitoringDidFailForRegion:withError:](<locationmanager(__monitoringdidfailfor_witherror_).md>) — Tells the delegate that a region monitoring error occurred.
- [- locationManager:didStartMonitoringForRegion:](<locationmanager(__didstartmonitoringfor_).md>) — Tells the delegate that a new region is being monitored.
- [CLRegionState](../clregionstate.md) — Constants that reflect the relationship of the current location to the region boundaries.
