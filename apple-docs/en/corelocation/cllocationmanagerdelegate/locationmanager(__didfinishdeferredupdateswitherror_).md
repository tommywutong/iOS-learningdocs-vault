---
title: 'locationManager(_:didFinishDeferredUpdatesWithError:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didfinishdeferredupdateswitherror:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didfinishdeferredupdateswitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Adidfinishdeferredupdateswitherror%3A%29.json'
content_hash: 'sha256:88655056ccb6edee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:didFinishDeferredUpdatesWithError:)

<sub>Instance Method</sub>

Tells the delegate that updates will no longer be deferred.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, didFinishDeferredUpdatesWithError error: (any Error)?)
```

## Parameters

- `manager` — The location manager object that generated the update event.

- `error` — The error object containing the reason deferred location updates could not be delivered.

## Discussion

The location manager object calls this method to let you know that it has stopped deferring the delivery of location events. The manager may call this method for any number of reasons. For example, it calls it when you stop location updates altogether, when you ask the location manager to disallow deferred updates, or when a condition for deferring updates (such as exceeding a timeout or distance parameter) is met.

## See Also

### Receiving location updates

- [- locationManager:didUpdateLocations:](<locationmanager(__didupdatelocations_).md>) — Tells the delegate that new location data is available.
- [- locationManager:didUpdateToLocation:fromLocation:](<locationmanager(__didupdateto_from_).md>) — Tells the delegate that a new location value is available. _(deprecated)_
