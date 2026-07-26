---
title: startMonitoringVisits()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/startmonitoringvisits()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoringvisits()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/startmonitoringvisits%28%29.json'
content_hash: 'sha256:919c967982069858'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# startMonitoringVisits()

<sub>Instance Method</sub>

Starts the delivery of visit-related events.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func startMonitoringVisits()
```

## Discussion

Calling this method begins the delivery of visit-related events to your app. Enabling visit events for one location manager enables visit events for all other location manager objects in your app. When a new visit event arrives, the location manager object delivers the event to the [- locationManager:didVisit:](<../cllocationmanagerdelegate/locationmanager(__didvisit_).md>) method of its delegate.

Your app can monitor for visit events without calling `requestTemporaryPreciseLocationAuthorization(withPurposeKey:)`. In that case, the visit events use reduced accuracy, as reflected by the [horizontalAccuracy](../clvisit/horizontalaccuracy.md) property of [CLVisit](../clvisit.md).

If your app is terminated while this service is active, the system relaunches your app when new visit events are ready to be delivered. Upon relaunch, recreate your location manager object and assign a delegate to begin receiving visit events. You don’t need to call this method again to restart the delivery of visit events, but calling it does no harm.

If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

### Running the visits location service

- [- stopMonitoringVisits](<stopmonitoringvisits().md>) — Stops the delivery of visit-related events.
