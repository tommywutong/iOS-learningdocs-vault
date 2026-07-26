---
title: 'locationManager(_:didUpdateTo:from:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didupdateto:from:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didupdateto:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Adidupdateto%3Afrom%3A%29.json'
content_hash: 'sha256:72385f9d5f2be2a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:didUpdateTo:from:)

<sub>Instance Method</sub>

Tells the delegate that a new location value is available.

<sub>macOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, didUpdateTo newLocation: CLLocation, from oldLocation: CLLocation)
```

## Parameters

- `manager` — The location manager object that generated the update event.

- `newLocation` — The new location data.

- `oldLocation` — The location data from the previous update. If this is the first update event delivered by this location manager, this parameter is `nil`.

## Discussion

By the time this message is delivered to your delegate, the new location data is also available directly from the [CLLocationManager](../cllocationmanager.md) object. The `newLocation` parameter may contain the data that was cached from a previous usage of the location service. You can use the [timestamp](../cllocation/timestamp.md) property of the location object to determine how recent the location data is.

## See Also

### Receiving location updates

- [- locationManager:didUpdateLocations:](<locationmanager(__didupdatelocations_).md>) — Tells the delegate that new location data is available.
- [- locationManager:didFinishDeferredUpdatesWithError:](<locationmanager(__didfinishdeferredupdateswitherror_).md>) — Tells the delegate that updates will no longer be deferred.
