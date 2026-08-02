---
title: Location and Maps Programming Guide
apple_id: TP40009497
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: User Experience
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/CoreLocation/CoreLocation.html
archived_at: '2026-07-18T02:12:01.492494Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Location and Maps Programming Guide](About%20Location%20Services%20and%20Maps.md)


[Next](Region%20Monitoring%20and%20iBeacon.md)[Previous](About%20Location%20Services%20and%20Maps.md)

# Getting the User’s Location

Apps use location data for many purposes, ranging from social networking to turn-by-turn navigation services. They get location data through the classes of the Core Location [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56). This framework provides several services that you can use to get and monitor the device’s current location:

- The standard location service offers a highly configurable way to get the current location and track changes.
- Region monitoring lets you monitor boundary crossings for defined geographical regions and Bluetooth low-energy beacon regions. (Beacon region monitoring is available in iOS only.)
- The significant-change location service provides a way to get the current location and be notified when significant changes occur, but it’s critical to use it correctly to avoid using too much power.

To learn how to give users a great location-aware experience while conserving power, see [Reduce Location Accuracy and Duration](../../Performance/Energy%20Efficiency%20Guide%20for%20iOS%20Apps/LocationBestPractices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmru).

To use the features of the Core Location framework, you must link your app to `CoreLocation.framework` in your Xcode project. To access the classes and headers of the framework, include an `#import <CoreLocation/CoreLocation.h>` statement at the top of any relevant source files.

For general information about the classes of the Core Location framework, see _[Core Location Framework Reference](https://developer.apple.com/documentation/corelocation)_.

If your iOS app requires location services to function properly, include the `UIRequiredDeviceCapabilities` key in the app’s `Info.plist` file. The App Store uses the information in this key to prevent users from downloading apps to devices that don’t contain the listed features.

The value for the `UIRequiredDeviceCapabilities` is an array of strings indicating the features that your app requires. Two strings are relevant to location services:

- Include the `location-services` string if you require location services in general.
- Include the `gps` string if your app requires the accuracy offered only by GPS hardware.

For more information about the `UIRequiredDeviceCapabilities` key, see _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

The Core Location framework lets you locate the current position of the device and use that information in your app. The framework reports the device’s location to your code and, depending on how you configure the service, also provides periodic updates as it receives new or improved data.

Two services can give you the user’s current location:

- The _standard location service_ is a configurable, general-purpose solution for getting location data and tracking location changes for the specified level of accuracy.
- The _significant-change location service_ delivers updates only when there has been a significant change in the device’s location, such as 500 meters or more.

Gathering location data is a power-intensive operation. For most apps, it’s usually sufficient to establish an initial position fix and then acquire updates only periodically after that. Regardless of the importance of location data in your app, you should choose the appropriate location service and use it wisely to avoid draining a device’s battery. For example:

- If your iOS app must keep monitoring location even while it’s in the background, use the standard location service and specify the `location` value of the `[UIBackgroundModes](../../../../General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xvkskcmfrwwz3sn52w4zcnn5sgk4y)` key to continue running in the background and receiving location updates. (In this situation, you should also make sure the location manager’s [pausesLocationUpdatesAutomatically](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620553-pauseslocationupdatesautomatical) property is set to `YES` to help conserve power.) Examples of apps that might need this type of location updating are fitness or turn-by-turn navigation apps.
- If GPS-level accuracy isn’t critical for your app and you don’t need continuous tracking, you can use the significant-change location service. It’s crucial that you use the significant-change location service correctly, because these updates run continuously, around the clock, until you stop them, and can actually result in higher energy use if not employed effectively.

There are situations where location services may not be available. For example:

- The user disables location services in the Settings app or System Preferences.
- The user denies location services for a specific app.
- The device is in Airplane mode and unable to power up the necessary hardware.

For these reasons, it’s recommended that you always call the [locationServicesEnabled](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423648-locationservicesenabled) class method of `CLLocationManager` before attempting to start either the standard or significant-change location services. If it returns `NO` and you attempt to start location services anyway, the system prompts the user to confirm whether location services should be re-enabled. Because the user probably disabled location services on purpose, the prompt is likely to be unwelcome.

The standard location service is the most common way to get a user’s current location because it’s available on all devices and in both iOS and OS X. Before using this service, you configure it by specifying the desired accuracy of the location data and the distance that must be traveled before reporting a new location. When you start the service, it uses the specified parameters to determine the hardware to enable and then proceeds to report location events to your app. Because this service takes into account these parameters, it’s most appropriate for apps that need more fine-grained control over the delivery of location events. The precision of the standard location service is needed by navigation apps or any app that requires high-precision location data or a regular stream of updates. Because this service typically requires the location-tracking hardware to be enabled for longer periods of time, higher power usage can result.

To use the standard location service, [create an instance](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) of the [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) class and configure its [desiredAccuracy](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423836-desiredaccuracy) and [distanceFilter](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423500-distancefilter) properties. To begin receiving location notifications, assign a [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) to the object and call the [startUpdatingLocation](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423750-startupdatinglocation) method. As location data becomes available, the location manager notifies its assigned delegate object. If a location update has already been delivered, you can also get the most recent location data directly from the `CLLocationManager` object without waiting for a new event to be delivered. To stop the delivery of location updates, call the [stopUpdatingLocation](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423695-stopupdatinglocation) method of the location manager object.

Listing 1-1 shows a sample method that configures a location manager for use. The sample method is part of a class that caches its location manager object in a member variable for later use. (The class also conforms to the [CLLocationManagerDelegate](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate) [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45) and so acts as the delegate for the location manager.) Because the app doesn’t need precise location data, it configures the location service to report the user’s general area and send notifications only when the user moves at least half a kilometer.

__Listing 1-1__  Starting the standard location service

```objc
- (void)startStandardUpdates
{
    // Create the location manager if this object does not
    // already have one.
    if (nil == locationManager)
        locationManager = [[CLLocationManager alloc] init];

    locationManager.delegate = self;
    locationManager.desiredAccuracy = kCLLocationAccuracyKilometer;

    // Set a movement threshold for new events.
    locationManager.distanceFilter = 500; // meters

    [locationManager startUpdatingLocation];
}
```

The code for receiving location updates from this service is shown in [Receiving Location Data from a Service](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqmrnknlte).

To use the significant-change location service, [create an instance](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) of the [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) class, assign a [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) to it, and call the [startMonitoringSignificantLocationChanges](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423531-startmonitoringsignificantlocati) method as shown in Listing 1-2. As location data becomes available, the location manager notifies its assigned delegate object. If a location update has already been delivered, you can also get the most recent location data directly from the `CLLocationManager` object without waiting for a new event to be delivered.

__Listing 1-2__  Starting the significant-change location service

```objc
- (void)startSignificantChangeUpdates
{
    // Create the location manager if this object does not
    // already have one.
    if (nil == locationManager)
        locationManager = [[CLLocationManager alloc] init];

    locationManager.delegate = self;
    [locationManager startMonitoringSignificantLocationChanges];
}
```

As with the standard location service, location data is delivered to the delegate object as described in [Receiving Location Data from a Service](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqmrnknlte). To stop the significant change location service, call the [stopMonitoringSignificantLocationChanges](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423679-stopmonitoringsignificantlocatio) method.

If you leave the significant-change location service running and your iOS app is subsequently suspended or terminated, the service automatically wakes up your app when new location data arrives. At wake-up time, the app is put into the background and you are given a small amount of time (around 10 seconds) to manually restart location services and process the location data. (You must manually restart location services in the background before any pending location updates can be delivered, as described in [Knowing When to Start Location Services](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqmrnknltcnq).) Because your app is in the background, it must do minimal work and avoid any tasks (such as querying the network) that might prevent it from returning before the allocated time expires. If it does not, your app will be terminated. If an iOS app needs more time to process the location data, it can request more background execution time using the [beginBackgroundTaskWithName:expirationHandler:](https://developer.apple.com/documentation/uikit/uiapplication/1623051-beginbackgroundtask) method of the `UIApplication` class.

The way you receive location events is the same whether you use the standard or the significant-change location service to get them. Beginning in OS X v10.9 and iOS 6, the location manager reports events to the [locationManager:didUpdateLocations:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423615-locationmanager) method of its delegate when they become available. (In earlier versions of both operating systems, the location manager reports events to the [locationManager:didUpdateToLocation:fromLocation:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423716-locationmanager) method.) If there is an error retrieving an event, the location manager calls the [locationManager:didFailWithError:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423786-locationmanager) method of its delegate instead.

Listing 1-3 shows the delegate method for receiving location events. Because the location manager object sometimes returns cached events, it’s recommended that you check the timestamp of any location events you receive. (It can take several seconds to obtain a rough location fix, so the old data simply serves as a way to reflect the last known location.) In this example, the method throws away any events that are more than fifteen seconds old under the assumption that events up to that age are likely to be good enough. If you are implementing a navigation app, you might want to lower the threshold.

__Listing 1-3__  Processing an incoming location event

```objc
// Delegate method from the CLLocationManagerDelegate protocol.
- (void)locationManager:(CLLocationManager *)manager
      didUpdateLocations:(NSArray *)locations {
    // If it's a relatively recent event, turn off updates to save power.
   CLLocation* location = [locations lastObject];
   NSDate* eventDate = location.timestamp;
   NSTimeInterval howRecent = [eventDate timeIntervalSinceNow];
   if (abs(howRecent) < 15.0) {
      // If the event is recent, do something with it.
      NSLog(@"latitude %+.6f, longitude %+.6f\n",
              location.coordinate.latitude,
              location.coordinate.longitude);
   }
}
```

In addition to a location object’s timestamp, you can also use the accuracy reported by that object to determine whether you want to accept an event. As it receives more accurate data, the location service may return additional events, with the accuracy values reflecting the improvements accordingly. Throwing away less accurate events means your app wastes less time on events that can’t be used effectively anyway.

Apps that use location services should not start those services until they’re needed. With a few exceptions, avoid starting location services immediately at launch time or before such services might reasonably be used. Otherwise you might raise questions in the user’s head about how your app uses location data. The user knows when your app starts location services, because the system prompts the user for permission as soon as your app starts the service. Waiting until the user performs a task that actually requires those services helps build trust that your app is using them appropriately. To build trust between the user and an app, an app that uses Core Location must include the [NSLocationAlwaysUsageDescription](../../General/Information%20Property%20List%20Key%20Reference/Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjy) or [NSLocationWhenInUseUsageDescription](../../General/Information%20Property%20List%20Key%20Reference/Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomrw) key in its `Info.plist` file and set the value of that key to a string that describes how the app intends to use location data. If you call the [requestWhenInUseAuthorization](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620562-requestwheninuseauthorization) method without including one of these keys, the system ignores your request.

If you are monitoring regions or using the significant-change location service in your app, there are situations where you must start location services at launch time. Apps using those services can be terminated and subsequently relaunched when new location events arrive. Although the app itself is relaunched, location services are not started automatically. When an app is relaunched because of a location update, the launch options dictionary passed to your [application:willFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623032-application) or [application:didFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) method contains the [UIApplicationLaunchOptionsLocationKey](https://developer.apple.com/documentation/uikit/uiapplicationlaunchoptionslocationkey) key. The presence of that key signals that new location data is waiting to be delivered to your app. To obtain that data, you must create a new [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) object and restart the location services that you had running prior to your app’s termination. When you restart those services, the location manager delivers all pending location updates to its delegate.

iOS supports the delivery of location events to apps that are suspended or no longer running. The delivery of location events in the background supports apps whose functionality would be impaired without them, so configure your app to receive background events only when doing so provides a tangible benefit to the user. For example, a turn-by-turn navigation app needs to track the user’s position at all times and notify the user when it’s time to make the next turn. If your app can make do with alternate means, such as region monitoring, it should do so.

You have multiple options for obtaining background location events, and each has advantages and disadvantages with regard to power consumption and location accuracy. Whenever possible, apps should use the significant-change location service (described in [Starting the Significant-Change Location Service](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqmrnknltq)), which can use Wi-Fi to determine the user’s position and consumes the least amount of power. But if your app requires higher precision location data, you can configure it as a background location app and use the standard location service.

iOS apps can use the standard location service in the background if they provide services that require continuous location updates. As a result, this capability is most appropriate for apps that assist the user in navigation- and fitness-related activities. To enable this capability in your app, enable the Background Modes capability in your Xcode project (located in the Capabilities tab of your project) and enable the Location updates mode. The code you write to start and stop the standard location services is unchanged. Table 1-1 lists the APIs for which you can enable the Location updates mode of the Background Modes capability.

__Table 1-1__  APIs and technologies for which an iOS app can specify location updates

| API | Requires location updates in background mode | Can use location updates in background mode |
| [startUpdatingLocation](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423750-startupdatinglocation) | Yes | Yes |
| [CLVisit](https://developer.apple.com/documentation/corelocation/clvisit) | No | Yes |
| [CLRegion](https://developer.apple.com/documentation/corelocation/clregion) | No | Yes |
| [startMonitoringSignificantLocationChanges](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423531-startmonitoringsignificantlocati) | No | Yes |
| [CLBeaconRegion](https://developer.apple.com/documentation/corelocation/clbeaconregion) | No | Yes, on a case-by-case basis |

The system delivers location updates to background location apps when the app is in the foreground, is running in the background, or is suspended. In the case of a suspended app, the system wakes up the app, delivers the update to the location manager’s delegate, and then returns the app to the suspended state as soon as possible. While it is running in the background, your app should do as little work as possible to process the new location data.

When location services are enabled, iOS must keep the location hardware powered up so that it can gather new data. Keeping the location hardware running degrades battery life, and you should always stop location services in your app whenever you do not need the resulting location data.

If you must use location services in the background, you can help Core Location maintain good battery life for the user’s device by taking additional steps when you configure your location manager object:

- Make sure the location manager’s [pausesLocationUpdatesAutomatically](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620553-pauseslocationupdatesautomatical) property is set to `YES`. When this property is set to `YES`, Core Location pauses location updates (and powers down the location hardware) whenever it makes sense to do so, such as when the user is unlikely to be moving anyway. (Core Location also pauses updates when it can’t obtain a location fix.)
- Assign an appropriate value to the location manager’s [activityType](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620567-activitytype) property. The value in this property helps the location manager determine when it is safe to pause location updates. For an app that provides turn-by-turn automobile navigation, setting the property to [CLActivityTypeAutomotiveNavigation](https://developer.apple.com/documentation/corelocation/clactivitytype/clactivitytypeautomotivenavigation) causes the location manager to pause events only when the user does not move a significant distance over a period of time.
- Call the [allowDeferredLocationUpdatesUntilTraveled:timeout:](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620547-allowdeferredlocationupdatesunti) method whenever possible to defer the delivery of updates until a later time, as described in [Deferring Location Updates While Your App Is in the Background](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqmrnknltcna).

When the location manager pauses location updates, it notifies its delegate object by calling its [locationManagerDidPauseLocationUpdates:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621553-locationmanagerdidpauselocationu) method. When the location manager resumes updates, it calls the delegate’s [locationManagerDidResumeLocationUpdates:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621512-locationmanagerdidresumelocation) method. You can use these delegate methods to perform tasks or adjust the behavior of your app. For example, when location updates are paused, you might use the delegate notification to save data to disk or stop location updates altogether. A navigation app in the middle of turn-by-turn directions might prompt the user and ask whether navigation should be disabled temporarily.

In iOS 6 and later, you can defer the delivery of location updates when your app is in the background. It’s recommended that you use this feature when your app could process the location data later without any problems. For example, a fitness app that tracks the user’s location on a hiking trail could defer updates until the user hikes a certain distance or until a certain amount of time has elapsed and then process the updates all at once. Deferring updates saves power by letting your app sleep for longer periods of time. Because deferring location updates requires the presence of GPS hardware on the target device, be sure to call the [deferredLocationUpdatesAvailable](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423830-deferredlocationupdatesavailable) class method of the `CLLocationManager` class to determine whether the device supports deferred location updates.

Call the [allowDeferredLocationUpdatesUntilTraveled:timeout:](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620547-allowdeferredlocationupdatesunti) method of the `CLLocationManager` class to begin deferring location updates. As shown in Listing 1-4, the usual place to call this method is in the [locationManager:didUpdateLocations:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423615-locationmanager) method of your location manager delegate object. This method shows how a sample hiking app might defer location updates until the user hikes a minimum distance. To prevent itself from calling the `allowDeferredLocationUpdatesUntilTraveled:timeout:` method multiple times, the delegate uses an internal property to track whether updates have already been deferred. It sets the property to `YES` in this method and sets it back to `NO` when deferred updates end.

__Listing 1-4__  Deferring location updates

```objc
// Delegate method from the CLLocationManagerDelegate protocol.
- (void)locationManager:(CLLocationManager *)manager
      didUpdateLocations:(NSArray *)locations {
   // Add the new locations to the hike
   [self.hike addLocations:locations];

   // Defer updates until the user hikes a certain distance
   // or when a certain amount of time has passed.
   if (!self.deferringUpdates) {
      CLLocationDistance distance = self.hike.goal - self.hike.distance;
      NSTimeInterval time = [self.nextAudible timeIntervalSinceNow];
      [locationManager allowDeferredLocationUpdatesUntilTraveled:distance
                                                         timeout:time];
   self.deferringUpdates = YES;
   }
}
```

When a condition you specified in the `allowDeferredLocationUpdatesUntilTraveled:timeout:` method is met, the location manager calls the [locationManager:didFinishDeferredUpdatesWithError:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423537-locationmanager) method of its delegate object to let you know that it has stopped deferring the delivery of location updates. The location manager calls this delegate method exactly once for each time your app calls the `allowDeferredLocationUpdatesUntilTraveled:timeout:` method. After deferred updates end, the location manager proceeds to deliver any location updates to your delegate’s `locationManager:didUpdateLocations:` method.

You can stop the deferral of location updates explicitly by calling the [disallowDeferredLocationUpdates](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620565-disallowdeferredlocationupdates) method of the `CLLocationManager` class. When you call this method, or stop location updates altogether using the [stopUpdatingLocation](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423695-stopupdatinglocation) method, the location manager calls your delegate’s `locationManager:didFinishDeferredUpdatesWithError:` method to let you know that deferred updates have indeed stopped.

If the location manager encounters an error and can’t defer location updates, you can access the cause of the error when you implement the `locationManager:didFinishDeferredUpdatesWithError:` delegate method. For a list of the possible errors that may be returned—and what, if anything, you can to resolve them—see the [CLError](https://developer.apple.com/documentation/corelocation/clerror/code) constants in _Core Location Constants Reference_.

[Next](Region%20Monitoring%20and%20iBeacon.md)[Previous](About%20Location%20Services%20and%20Maps.md)

