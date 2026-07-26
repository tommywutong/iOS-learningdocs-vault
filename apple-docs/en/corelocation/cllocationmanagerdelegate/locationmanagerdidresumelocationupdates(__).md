---
title: 'locationManagerDidResumeLocationUpdates(_:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanagerdidresumelocationupdates(_:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanagerdidresumelocationupdates(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanagerdidresumelocationupdates%28_%3A%29.json'
content_hash: 'sha256:eb104e625636ed81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManagerDidResumeLocationUpdates(_:)

<sub>Instance Method</sub>

Tells the delegate that the delivery of location updates has resumed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func locationManagerDidResumeLocationUpdates(_ manager: CLLocationManager)
```

## Parameters

- `manager` — The location manager that resumed the delivery of events.

## Discussion

When you restart location services after an automatic pause, Core Location calls this method to notify your app that services have resumed. You are responsible for restarting location services in your app. Core Location does not resume updates automatically after it pauses them. For tips on how to restart location services when a pause occurs, see the discussion of the [- locationManagerDidPauseLocationUpdates:](<locationmanagerdidpauselocationupdates(__).md>) method.

## See Also

### Pausing location updates

- [- locationManagerDidPauseLocationUpdates:](<locationmanagerdidpauselocationupdates(__).md>) — Tells the delegate that location updates were paused.
