---
title: Location and Maps Programming Guide
apple_id: TP40009497
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: User Experience
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/GettingHeadings/GettingHeadings.html
archived_at: '2026-07-18T02:12:01.625077Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Location and Maps Programming Guide](About%20Location%20Services%20and%20Maps.md)


[Next](Geocoding%20Location%20Data.md)[Previous](Region%20Monitoring%20and%20iBeacon.md)

# Getting the Heading and Course of a Device

Core Location supports two different ways to get direction-related information:

- Devices with a magnetometer can report the direction in which a device is pointing, also known as its _heading_.
- Devices with GPS hardware can report the direction in which a device is moving, also known as its _course_.

Heading and course information don’t represent the same information. The heading of a device reflects the actual orientation of the device relative to true north or magnetic north. The course of the device represents the direction of travel and doesn’t take into account the device orientation. Depending on your app, you might prefer one type of information over the other or use a combination of the two. For example, a navigation app might toggle between course and heading information depending on the user’s current speed. At walking speeds, heading information would be more useful for orienting the user to the current environment, whereas in a car, course information provides the general direction of the car’s movement.

If your iOS app requires direction-related information in order to function properly, include the `UIRequiredDeviceCapabilities` key in the app’s `Info.plist` file. This key contains an array of strings indicating the features that your app requires of the underlying iOS-based device. The App Store uses this information to prevent users from installing apps on a device without the minimum required hardware.

For direction-related events, you can associate two relevant strings with the `UIRequiredDeviceCapabilities` key:

- `magnetometer`—Include this string if your app requires heading information.
- `gps`—Include this string if your app requires course-related information.

In both cases, also include the `location-services` string in the array. For more information about the `UIRequiredDeviceCapabilities` key, see _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

Heading events are available to apps running on a device that contains a magnetometer. A magnetometer measures nearby magnetic fields emanating from the Earth and uses them to determine the precise orientation of the device. Although a magnetometer can be affected by local magnetic fields, such as those emanating from fixed magnets found in audio speakers, motors, and many other types of electronic devices, Core Location is smart enough to filter out fields that move with the device.

Heading values can be reported relative either to magnetic north or true north on the map. Magnetic north represents the point on the Earth’s surface from which the planet’s magnetic field emanates. This location is not the same as the North Pole, which represents true north. Depending on the location of the device, magnetic north may be good enough for many purposes, but the closer to the poles you get, the less useful this value becomes.

To get heading events:

1. Create a [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) object.
2. Determine whether heading events are available by calling the [headingAvailable](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423502-headingavailable) class method.
3. Assign a delegate to the location manager object.
4. If you want true north values, start location services.
5. Call the [startUpdatingHeading](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620558-startupdatingheading) method to begin the delivery of heading events.

Listing 3-1 shows a custom method that configures a location manager and starts the delivery of heading events. In this case, the object is a view controller that displays the current heading to the user. Because the view controller displays the true north heading value, it starts location updates in addition to heading updates.

__Listing 3-1__  Initiating the delivery of heading events

```objc
- (void)startHeadingEvents {
   if (!self.locManager) {
      CLLocationManager* theManager = [[[CLLocationManager alloc] init] autorelease];

      // Retain the object in a property.
      self.locManager = theManager;
      locManager.delegate = self;
   }

   // Start location services to get the true heading.
   locManager.distanceFilter = 1000;
   locManager.desiredAccuracy = kCLLocationAccuracyKilometer;
   [locManager startUpdatingLocation];

   // Start heading updates.
   if ([CLLocationManager headingAvailable]) {
      locManager.headingFilter = 5;
      [locManager startUpdatingHeading];
   }
}
```

The object you assign to the delegate property must conform to the [CLLocationManagerDelegate](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate) [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45). When a new heading event arrives, the location manager object calls the [locationManager:didUpdateHeading:](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621555-locationmanager) method to deliver that event to your app. Upon receiving a new event, check the [headingAccuracy](https://developer.apple.com/documentation/corelocation/clheading/1423705-headingaccuracy) property to ensure that the data you just received is valid, as shown in Listing 3-2. In addition, if you are using the true heading value, also check whether it contains a valid value before using it.

__Listing 3-2__  Processing heading events

```objc
- (void)locationManager:(CLLocationManager *)manager didUpdateHeading:(CLHeading *)newHeading {
   if (newHeading.headingAccuracy < 0)
      return;

   // Use the true heading if it is valid.
   CLLocationDirection  theHeading = ((newHeading.trueHeading > 0) ?
            newHeading.trueHeading : newHeading.magneticHeading);

   self.currentHeading = theHeading;
   [self updateHeadingDisplays];
}
```


Devices that include GPS hardware can generate information that represents the device’s current course and speed. Course information indicates the direction in which the device is moving and doesn’t necessarily reflect the orientation of the device itself. As a result, course information is primarily intended for apps that provide navigation information while the user is moving.

The actual course and speed information is returned to your app in the same [CLLocation](https://developer.apple.com/documentation/corelocation/cllocation) objects you use to get the user’s position. When you start location updates, Core Location automatically provides course and speed information when it’s available. The framework uses the incoming location events to compute the current direction of motion. For more information on how to start location updates, see [Getting the User’s Location](Getting%20the%20User%E2%80%99s%20Location.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqmrnknltc).

[Next](Geocoding%20Location%20Data.md)[Previous](Region%20Monitoring%20and%20iBeacon.md)

