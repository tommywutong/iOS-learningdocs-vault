---
title: 'locationManagerDidPauseLocationUpdates(_:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanagerdidpauselocationupdates(_:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanagerdidpauselocationupdates(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanagerdidpauselocationupdates%28_%3A%29.json'
content_hash: 'sha256:56904476bf8f324e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManagerDidPauseLocationUpdates(_:)

<sub>Instance Method</sub>

Tells the delegate that location updates were paused.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func locationManagerDidPauseLocationUpdates(_ manager: CLLocationManager)
```

## Parameters

- `manager` — The location manager object that paused the delivery of events.

## Discussion

When the location manager detects that the device’s location is not changing, it can pause the delivery of updates in order to shut down the appropriate hardware and save power. When it does this, it calls this method to let your app know that this has happened.

After a pause occurs, it is your responsibility to restart location services again at an appropriate time. You might use your implementation of this method to start region monitoring at the user’s current location or enable the visits location service to determine when the user starts moving again. Another alternative is to restart location services immediately with a reduced accuracy (which can save power) and then return to a greater accuracy only after the user starts moving again.

## See Also

### Pausing location updates

- [- locationManagerDidResumeLocationUpdates:](<locationmanagerdidresumelocationupdates(__).md>) — Tells the delegate that the delivery of location updates has resumed.
