---
title: CLRegionState
framework: Core Location
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clregionstate
source_url: 'https://developer.apple.com/documentation/corelocation/clregionstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clregionstate.json'
content_hash: 'sha256:77150cfe7dbba1db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLRegionState

<sub>Enumeration</sub>

Constants that reflect the relationship of the current location to the region boundaries.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@frozen enum CLRegionState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Region States

- [CLRegionStateUnknown](clregionstate/unknown.md) — It is unknown whether the location is inside or outside of the region.
- [CLRegionStateInside](clregionstate/inside.md) — The location is inside of the given region.
- [CLRegionStateOutside](clregionstate/outside.md) — The location is outside of the given region.

### Initializers

- [init(rawValue:)](<clregionstate/init(rawvalue_).md>)

## See Also

### Receiving region-related updates

- [- locationManager:didEnterRegion:](<cllocationmanagerdelegate/locationmanager(__didenterregion_).md>) — Tells the delegate that the user entered the specified region.
- [- locationManager:didExitRegion:](<cllocationmanagerdelegate/locationmanager(__didexitregion_).md>) — Tells the delegate that the user left the specified region.
- [- locationManager:didDetermineState:forRegion:](<cllocationmanagerdelegate/locationmanager(__diddeterminestate_for_).md>) — Tells the delegate about the state of the specified region.
- [- locationManager:monitoringDidFailForRegion:withError:](<cllocationmanagerdelegate/locationmanager(__monitoringdidfailfor_witherror_).md>) — Tells the delegate that a region monitoring error occurred.
- [- locationManager:didStartMonitoringForRegion:](<cllocationmanagerdelegate/locationmanager(__didstartmonitoringfor_).md>) — Tells the delegate that a new region is being monitored.
