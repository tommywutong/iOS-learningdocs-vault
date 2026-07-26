---
title: startMonitoringSignificantLocationChanges()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/startmonitoringsignificantlocationchanges()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoringsignificantlocationchanges()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/startmonitoringsignificantlocationchanges%28%29.json'
content_hash: 'sha256:c374f8ae948db3dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# startMonitoringSignificantLocationChanges()

<sub>Instance Method</sub>

Starts the generation of updates based on significant location changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func startMonitoringSignificantLocationChanges()
```

## Discussion

This method initiates the delivery of location events asynchronously, returning shortly after you call it. Location events are delivered to your delegate’s [- locationManager:didUpdateLocations:](<../cllocationmanagerdelegate/locationmanager(__didupdatelocations_).md>) method. The first event to be delivered is usually the most recently cached location event (if any) but may be a newer event in some circumstances. Obtaining a current location fix may take several additional seconds, so be sure to check the timestamps on the location events in your delegate method.

After returning a current location fix, the receiver generates update events only when a significant change in the user’s location is detected. It does not rely on the value in the [distanceFilter](distancefilter.md) property to generate events. Calling this method several times in succession does not automatically result in new events being generated. Calling [- stopMonitoringSignificantLocationChanges](<stopmonitoringsignificantlocationchanges().md>) in between, however, does cause a new initial event to be sent the next time you call this method.

If you start this service and your app is subsequently terminated, the system automatically relaunches the app into the background if a new event arrives. In such a case, the options dictionary passed to the [application(_:willFinishLaunchingWithOptions:)](<../../uikit/uiapplicationdelegate/application(__willfinishlaunchingwithoptions_).md>) and [application(_:didFinishLaunchingWithOptions:)](<../../uikit/uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) methods of your app delegate contains the key [location](../../uikit/uiapplication/launchoptionskey/location.md) to indicate that your app was launched because of a location event. Upon relaunch, you must still configure a location manager object and call this method to continue receiving location events. When you restart location services, the current event is delivered to your delegate immediately. In addition, the [location](location.md) property of your location manager object is populated with the most recent location object even before you start location services.

In addition to your delegate object implementing the [- locationManager:didUpdateLocations:](<../cllocationmanagerdelegate/locationmanager(__didupdatelocations_).md>) method, it should also implement the [- locationManager:didFailWithError:](<../cllocationmanagerdelegate/locationmanager(__didfailwitherror_).md>) method to respond to potential errors.

> [!note] Note
> Apps can expect a notification as soon as the device moves 500 meters or more from its previous notification. It should not expect notifications more frequently than once every five minutes. If the device is able to retrieve data from the network, the location manager is much more likely to deliver notifications in a timely manner.

If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

### Running the significant change location service

- [- stopMonitoringSignificantLocationChanges](<stopmonitoringsignificantlocationchanges().md>) — Stops the delivery of location events based on significant location changes.
