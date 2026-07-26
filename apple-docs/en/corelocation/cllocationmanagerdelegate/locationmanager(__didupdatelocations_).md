---
title: 'locationManager(_:didUpdateLocations:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didupdatelocations:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didupdatelocations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Adidupdatelocations%3A%29.json'
content_hash: 'sha256:164adb55f1c19797'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:didUpdateLocations:)

<sub>Instance Method</sub>

Tells the delegate that new location data is available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation])
```

## Parameters

- `manager` — The location manager object that generated the update event.

- `locations` — An array of [CLLocation](../cllocation.md) objects containing the location data. This array always contains at least one object representing the current location. If updates were deferred or if multiple locations arrived before they could be delivered, the array may contain additional entries. The objects in the array are organized in the order in which they occurred. Therefore, the most recent location update is at the end of the array.

## Discussion

Implementation of this method is optional but recommended.

## Topics

### Related Documentation

- [MapKit](../../mapkit.md) — Display map or satellite imagery within your app, call out points of interest, and determine placemark information for map coordinates.
- [MapKit JS](../../mapkitjs.md) — Embed interactive Apple Maps on your website, annotate points of interest, and perform georelated searches.

## See Also

### Receiving location updates

- [- locationManager:didUpdateToLocation:fromLocation:](<locationmanager(__didupdateto_from_).md>) — Tells the delegate that a new location value is available. _(deprecated)_
- [- locationManager:didFinishDeferredUpdatesWithError:](<locationmanager(__didfinishdeferredupdateswitherror_).md>) — Tells the delegate that updates will no longer be deferred.
