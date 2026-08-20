---
title: Location and Maps Programming Guide
apple_id: TP40009497
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: User Experience
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
archived_at: '2026-07-18T02:12:07.540414Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Location and Maps Programming Guide](About%20Location%20Services%20and%20Maps.md)


[Next](Getting%20the%20Heading%20and%20Course%20of%20a%20Device.md)[Previous](Getting%20the%20User%E2%80%99s%20Location.md)

# Region Monitoring and iBeacon

The Core Location framework provides two ways to detect a user’s entry and exit into specific regions: geographical region monitoring (iOS 4.0 and later and OS X v10.8 and later) and beacon region monitoring (iOS 7.0 and later). A _geographical region_ is an area defined by a circle of a specified radius around a known point on the Earth’s surface. In contrast, a _beacon region_ is an area defined by the device’s proximity to Bluetooth low-energy beacons. Beacons themselves are simply devices that advertise a particular Bluetooth low-energy payload—you can even turn your iOS device into a beacon with some assistance from the Core Bluetooth framework.

Apps can use region monitoring to be notified when a user crosses geographic boundaries or when a user enters or exits the vicinity of a beacon. While a beacon is in range of an iOS device, apps can also monitor for the relative distance to the beacon. You can use these capabilities to develop many types of innovative location-based apps. Because geographical regions and beacon regions differ, the type of region monitoring you decide to use will likely depend on the use case of your app.

In iOS, regions associated with your app are tracked at all times, including when the app isn’t running. If a region boundary is crossed while an app isn’t running, that app is relaunched into the background to handle the event. Similarly, if the app is suspended when the event occurs, it’s woken up and given a short amount of time (around 10 seconds) to handle the event. When necessary, an app can request more background execution time using the [beginBackgroundTaskWithExpirationHandler:](https://developer.apple.com/documentation/uikit/uiapplication/1623031-beginbackgroundtaskwithexpiratio) method of the [UIApplication](https://developer.apple.com/documentation/uikit/uiapplication) class.

In OS X, region monitoring works only while the app is running (either in the foreground or background) and the user’s system is awake. As a result, the system doesn’t launch apps to deliver region-related notifications.

Before attempting to monitor any regions, your app should check whether region monitoring is supported on the current device. Here are some reasons why region monitoring might not be available:

- The device doesn’t have the necessary hardware to support region monitoring.
- The user denied the app the authorization to use region monitoring.
- The user disabled location services in the Settings app.
- The user disabled Background App Refresh in the Settings app, either for the device or for your app.
- The device is in Airplane mode and can’t power up the necessary hardware.

In iOS 7.0 and later, always call the [isMonitoringAvailableForClass:](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423654-ismonitoringavailable) and [authorizationStatus](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423523-authorizationstatus) class methods of `CLLocationManager` before attempting to monitor regions. (In OS X v10.8 and later and in previous versions of iOS, use the [regionMonitoringAvailable](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423564-regionmonitoringavailable) class instead.) The [isMonitoringAvailableForClass:](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423654-ismonitoringavailable) method tells you whether the underlying hardware supports region monitoring for the specified class at all. If that method returns `NO`, your app can’t use region monitoring on the device. If it returns `YES`, call the `authorizationStatus` method to determine whether the app is currently authorized to use location services. If the authorization status is [kCLAuthorizationStatusAuthorized](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/kclauthorizationstatusauthorized), your app can receive boundary crossing notifications for any regions it registered. If the authorization status is set to any other value, the app doesn’t receive those notifications.

Finally, if your app needs to process location updates in the background, be sure to check the [backgroundRefreshStatus](https://developer.apple.com/documentation/uikit/uiapplication/1622994-backgroundrefreshstatus) property of the [UIApplication](https://developer.apple.com/documentation/uikit/uiapplication) class. You can use the value of this property to determine if doing so is possible and to warn the user if it is not. Note that the system doesn’t wake your app for region notifications when the Background App Refresh setting is disabled globally or specifically for your app.

Geographical region monitoring uses location services to detect entry and exit into known geographical locations (learn more about location services in [Getting the User’s Location](Getting%20the%20User%E2%80%99s%20Location.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqmrnknltc)). You can use this capability to generate alerts when the user gets close to a specific location or to provide other relevant information. For example, upon approaching a specific dry cleaners, an app could notify the user to pick up any clothes that are now ready.

To begin monitoring a geographical region, you must define the region and register it with the system. In iOS 7.0 and later, you define geographical regions using the [CLCircularRegion](https://developer.apple.com/documentation/corelocation/clcircularregion) class. (In OS X v10.8 and later and in previous versions of iOS, you use the [CLRegion](https://developer.apple.com/documentation/corelocation/clregion) class instead.) Each region you create must include both the data that defines the desired geographic area and a unique identifier string. The identifier string is the only guaranteed way for your app to identify a region later. To register a region, call the [startMonitoringForRegion:](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423656-startmonitoringforregion) method of your [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) object.

Listing 2-1 shows a sample method that creates a new geographic region based on a circular overlay region. The overlay’s center point and radius form the boundary for the region, although if the radius is too large to be monitored, it is reduced automatically. You don’t need to save strong references to the regions you create but might want to store the region’s identifier if you plan to access the region information later.

__Listing 2-1__  Creating and registering a geographical region based on a Map Kit overlay

```objc
- (void)registerRegionWithCircularOverlay:(MKCircle*)overlay andIdentifier:(NSString*)identifier {

   // If the overlay's radius is too large, registration fails automatically,
   // so clamp the radius to the max value.
   CLLocationDistance radius = overlay.radius;
   if (radius > self.locManager.maximumRegionMonitoringDistance) {
      radius = self.locManager.maximumRegionMonitoringDistance;
   }

   // Create the geographic region to be monitored.
   CLCircularRegion *geoRegion = [[CLCircularRegion alloc]
      initWithCenter:overlay.coordinate
              radius:radius
          identifier:identifier];
   [self.locManager startMonitoringForRegion:geoRegion];
}
```

Monitoring of a geographical region begins immediately after registration for authorized apps. However, don’t expect to receive an event right away, because only boundary crossings generate an event. In particular, if the user’s location is already inside the region at registration time, the location manager doesn’t automatically generate an event. Instead, your app must wait for the user to cross the region boundary before an event is generated and sent to the delegate. To check whether the user is already inside the boundary of a region, use the [requestStateForRegion:](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423804-requeststate) method of the [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) class.

Be judicious when specifying the set of regions to monitor. Regions are a shared system resource, and the total number of regions available systemwide is limited. For this reason, Core Location limits to 20 the number of regions that may be simultaneously monitored by a single app. To work around this limit, consider registering only those regions in the user’s immediate vicinity. As the user’s location changes, you can remove regions that are now farther way and add regions coming up on the user’s path. If you attempt to register a region and space is unavailable, the location manager calls the [locationManager:monitoringDidFailForRegion:withError:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423720-locationmanager) method of its delegate with the [kCLErrorRegionMonitoringFailure](https://developer.apple.com/documentation/corelocation/clerror/code/regionmonitoringfailure) error code.

By default, every time a user’s current location crosses a boundary region, the system generates an appropriate region event for your app. Apps can implement the following methods to handle boundary crossings:

- [locationManager:didEnterRegion:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423560-locationmanager)
- [locationManager:didExitRegion:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423630-locationmanager)

You can customize which boundary-crossing events notify your app by explicitly setting the [notifyOnEntry](https://developer.apple.com/documentation/corelocation/clregion/1423566-notifyonentry) and [notifyOnExit](https://developer.apple.com/documentation/corelocation/clregion/1423595-notifyonexit) properties of the [CLRegion](https://developer.apple.com/documentation/corelocation/clregion) class when you define and register a region. (The default value of both properties is `YES`.) For example, if you want to be notified only when the user exits the boundary of a region, you can set the value of the region’s [notifyOnEntry](https://developer.apple.com/documentation/corelocation/clregion/1423566-notifyonentry) property to `NO`.

The system doesn’t report boundary crossings until the boundary plus a system-defined cushion distance is exceeded. This cushion value prevents the system from generating numerous entered and exited events in quick succession while the user is traveling close the edge of the boundary.

When a region boundary is crossed, the most likely response is to alert the user of the proximity to the target item. If your app is running in the background, you can use local notifications to alert the user; otherwise, you can simply post an alert.

Beacon region monitoring uses an iOS device’s onboard radio to detect when the user is in the vicinity of Bluetooth low-energy devices that are advertising iBeacon information. As with geographical region monitoring, you can use this capability to generate alerts or to provide other relevant information when the user enters or exits a beacon region. Rather than being identified by fixed geographical coordinates, however, a beacon region is identified by the device’s proximity to Bluetooth low-energy beacons that advertise a combination of the following values:

- A _proximity UUID_ (universally unique identifier), which is a 128-bit value that uniquely identifies one or more beacons as a certain type or from a certain organization
- A _major_ value, which is a 16-bit unsigned integer that can be used to group related beacons that have the same proximity UUID
- A _minor_ value, which is a 16-bit unsigned integer that differentiates beacons with the same proximity UUID and major value

Because a single beacon region can represent multiple beacons, beacon region monitoring supports several interesting use cases. For example, an app dedicated to enhancing the experience of customers at a particular department store can use the same proximity UUID to monitor all stores in the department store chain. When the user approaches a store, the app detects the store’s beacons and uses the major and minor values of those beacons to determine additional information, such as which specific store was encountered or which section of the store the user is in. (Note that although every beacon must advertise a proximity UUID, major and minor values are optional.)

To begin monitoring a beacon region, define the region and register it with the system. You define a beacon region with the appropriate initialization method of the [CLBeaconRegion](https://developer.apple.com/documentation/corelocation/clbeaconregion) class. When you create a [CLBeaconRegion](https://developer.apple.com/documentation/corelocation/clbeaconregion) object, you specify the [proximityUUID](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621556-proximityuuid), [major](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621536-major), and [minor](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621414-minor) properties of the beacons you want to monitor (the proximity UUID is required; the major and minor values are optional). You must also supply a string that uniquely identifies the region so that you can refer to it in your code. Note that a region’s identifier is unrelated to the identifying information that a beacon advertises.

To register a beacon region, call the [startMonitoringForRegion:](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423656-startmonitoringforregion) method of your [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) object. Listing 2-2 shows a sample method that creates and registers a beacon region.

__Listing 2-2__  Creating and registering a beacon region

```objc
- (void)registerBeaconRegionWithUUID:(NSUUID *)proximityUUID andIdentifier:(NSString*)identifier {

   // Create the beacon region to be monitored.
   CLBeaconRegion *beaconRegion = [[CLBeaconRegion alloc]
      initWithProximityUUID:proximityUUID
                 identifier:identifier];

   // Register the beacon region with the location manager.
   [self.locManager startMonitoringForRegion:beaconRegion];
}
```

As with geographical region monitoring, monitoring of a beacon region begins immediately after registration for authorized apps. When a user’s device detects a beacon that is advertising the identifying information defined by the registered beacon region (proximity UUID, major value, and minor value), the system generates an appropriate region event for your app.

When a user enters the registered beacon region, the location manager calls the [locationManager:didEnterRegion:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423560-locationmanager) of its delegate object. Similarly, when a user is no longer in range of any beacons in the registered beacon region, the location manager calls the [locationManager:didExitRegion:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423630-locationmanager) of its delegate object. Note that a user must cross the region’s boundary to trigger one of these calls; in particular, the location manager doesn’t call `locationManager:didEnterRegion:` if the user is already within the region. You can implement these delegate methods to alert the user appropriately or to present location-specific UI.

You can specify which boundary-crossing events should notify your app by setting the [notifyOnEntry](https://developer.apple.com/documentation/corelocation/clregion/1423566-notifyonentry) and [notifyOnExit](https://developer.apple.com/documentation/corelocation/clregion/1423595-notifyonexit) properties of the beacon region. (The default value of both properties is `YES`.) For example, if you want to be notified only when the user exits the boundary of a region, you can set the value of the region’s [notifyOnEntry](https://developer.apple.com/documentation/corelocation/clregion/1423566-notifyonentry) property to `NO`.

You can also postpone notifying a user upon entering a beacon region until the user turns on the device’s display. To do so, simply set the value of the beacon region’s [notifyEntryStateOnDisplay](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621552-notifyentrystateondisplay) property value to `YES` and set the region’s [notifyOnEntry](https://developer.apple.com/documentation/corelocation/clregion/1423566-notifyonentry) property to `NO` when you register the beacon region. To prevent redundant notifications from being delivered to the user, post a local notification only once per region entry.

While a user’s device is inside a registered beacon region, apps can use the [startRangingBeaconsInRegion:](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620554-startrangingbeacons) method of the [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) class to determine the relative proximity of one or more beacons in the region and to be notified when that distance changes. (Always call the [isRangingAvailable](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620549-israngingavailable) class method of the [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) class before attempting to range beacons in a beacon region.) Knowing the relative distance to a beacon can be useful for many apps. For example, imagine a museum that places a beacon at each exhibit. A museum-specific app could use a particular exhibit’s proximity as a cue to provide information about that exhibit rather than another.

The location manager calls the [locationManager:didRangeBeacons:inRegion:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621501-locationmanager) of its delegate object whenever beacons in the specified beacon region come within range, go out of range, or their proximity changes. This delegate method provides an array of [CLBeacon](https://developer.apple.com/documentation/corelocation/clbeacon) objects that represent the beacons currently in range. The array of beacons is ordered by approximate distance from the device, with the closest beacon at the beginning of the array. You can use the information in these objects to determine the proximity of the user to each beacon. The value in the [proximity](https://developer.apple.com/documentation/corelocation/clbeacon/1621554-proximity) property of the `CLBeacon` object gives a general sense of the relative distance to a beacon.

Inspired by the sample museum app described earlier in this section, Listing 2-3 shows how to use a beacon’s [proximity](https://developer.apple.com/documentation/corelocation/clbeacon/1621554-proximity) property to determine its relative distance from the user’s device. The code presents a UI that provides more information about a particular museum exhibit when the proximity of the closest beacon in the array is relatively close to the user (as defined by the [CLProximityNear](https://developer.apple.com/documentation/corelocation/clproximity/clproximitynear) constant).

__Listing 2-3__  Determining the relative distance between a beacon and a device

```objc
// Delegate method from the CLLocationManagerDelegate protocol.
- (void)locationManager:(CLLocationManager *)manager
        didRangeBeacons:(NSArray *)beacons
               inRegion:(CLBeaconRegion *)region {

   if ([beacons count] > 0) {
      CLBeacon *nearestExhibit = [beacons firstObject];

      // Present the exhibit-specific UI only when
      // the user is relatively close to the exhibit.
      if (CLProximityNear == nearestExhibit.proximity) {
         [self presentExhibitInfoWithMajorValue:nearestExhibit.major.integerValue];
      } else {
         [self dismissExhibitInfo];
   }
}
```

To promote consistent results in your app, use beacon ranging only while your app is in the foreground. If your app is in the foreground, it is likely that the device is in the user’s hand and that the device’s view to the target beacon has fewer obstructions. Running in the foreground also promotes better battery life by processing incoming beacon signals only while the user is actively using the device.

Any iOS device that supports sharing data using Bluetooth low energy can be used as an iBeacon. Because the app you write must run in the foreground, iBeacon support on iOS devices is intended for testing purposes and for apps that always run in the foreground anyway, such as point-of sale apps. For other types of iBeacon implementations, you need to acquire dedicated beacon hardware from third-party manufacturers.

Because turning your iOS device into a beacon requires the use of the Core Bluetooth framework, be sure to link your app to `CoreBluetooth.framework` in your Xcode project. To access the classes and headers of the framework, include an `#import <CoreBluetooth/CoreBluetooth.h>` statement at the top of any relevant source files.

To use your iOS device as a beacon, you first generate a 128-bit UUID that will be your beacon region’s proximity UUID. Open Terminal and type `uuidgen` on the command line. You receive a unique 128-bit value in an ASCII string that is punctuated by hyphens, as in this example.

```
$ uuidgen
39ED98FF-2900-441A-802F-9C398FC199D2
```

Next, create a beacon region with the UUID you generated for the beacon’s proximity UUID, defining the major and minor values as needed. Be sure to also use a unique string identifier for the new region. This code shows how to create a new beacon region using the example UUID above.

```
   NSUUID *proximityUUID = [[NSUUID alloc]
      initWithUUIDString:@"39ED98FF-2900-441A-802F-9C398FC199D2"];

   // Create the beacon region.
   CLBeaconRegion *beaconRegion = [[CLBeaconRegion alloc]
      initWithProximityUUID:proximityUUID
                 identifier:@"com.mycompany.myregion"
```

Now that you have created a beacon region, you need to advertise your beacon’s proximity UUID (and any major or minor value you specified) using the [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) class of the Core Bluetooth framework. In Core Bluetooth, a _peripheral_ is a device that advertises and shares data using Bluetooth low energy. Advertising your beacon’s data is the only way other devices can detect and range your beacon.

To advertise peripheral data in Core Bluetooth, you call the [startAdvertising:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393252-startadvertising) method of the [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) class on an instance of a [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) object. This method expects a dictionary (an instance of [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary)) of advertisement data. As the next example shows, use the [peripheralDataWithMeasuredPower:](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621494-peripheraldatawithmeasuredpower) method of the [CLBeaconRegion](https://developer.apple.com/documentation/corelocation/clbeaconregion) class to receive a dictionary that encodes your beacon’s identifying information along with other information needed for Core Bluetooth to advertise the beacon as a peripheral.

```
   // Create a dictionary of advertisement data.
   NSDictionary *beaconPeripheralData =
      [beaconRegion peripheralDataWithMeasuredPower:nil];
```

Next, create an instance of the [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) class, and ask it to advertise your beacon for other devices to detect, as shown in the code below.

```
   // Create the peripheral manager.
   CBPeripheralManager *peripheralManager = [[CBPeripheralManager alloc]
      initWithDelegate:selfqueue:nil options:nil];

   // Start advertising your beacon's data.
   [peripheralManager startAdvertising:beaconPeripheralData];
```

After advertising your app as a beacon, your app must continue running in the foreground to broadcast the needed Bluetooth signals. If the user quits the app, the system stops advertising your device as a peripheral.

For more information about how to use a peripheral manager to advertise data using Bluetooth low energy, see _[CBPeripheralManager Class Reference](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager)_ and _[Core Bluetooth Programming Guide](../../Networking%20Internet%20Web/Core%20Bluetooth%20Programming%20Guide/About%20Core%20Bluetooth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjx)_.

When testing your region monitoring code in iOS Simulator or on a device, realize that region events may not happen immediately after a region boundary is crossed. To prevent spurious notifications, iOS doesn’t deliver region notifications until certain threshold conditions are met. Specifically, the user’s location must cross the region boundary, move away from the boundary by a minimum distance, and remain at that minimum distance for at least 20 seconds before the notifications are reported.

The specific threshold distances are determined by the hardware and the location technologies that are currently available. For example, if Wi-Fi is disabled, region monitoring is significantly less accurate. However, for testing purposes, you can assume that the minimum distance is approximately 200 meters.

[Next](Getting%20the%20Heading%20and%20Course%20of%20a%20Device.md)[Previous](Getting%20the%20User%E2%80%99s%20Location.md)

