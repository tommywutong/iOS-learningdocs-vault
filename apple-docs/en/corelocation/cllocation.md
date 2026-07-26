---
title: CLLocation
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocation
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation.json'
content_hash: 'sha256:56fd677f8dfe490b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLLocation

<sub>Class</sub>

The latitude, longitude, and course information reported by the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CLLocation
```

## Overview

A [CLLocation](cllocation.md) object contains the geographical location and altitude of a device, along with values indicating the accuracy of those measurements and when they were collected. In iOS, a location object also contains course information — that is, the speed and heading in which the device was moving.

Typically, you don’t create location objects yourself. After you request location updates from your [CLLocationManager](cllocationmanager.md) object, the system uses onboard sensors to gather location data and report that data to your app. Some services also return previously collected location data, which you can use as context to improve your services. You can always retrieve the most recently collected location from the [location](cllocationmanager/location.md) property of your [CLLocationManager](cllocationmanager.md) object. You may create location objects yourself when you want to cache custom location data or calculate the distance between two geographical coordinates.

Use [CLLocation](cllocation.md) objects as-is, and don’t subclass them.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CKRecordValue](../cloudkit/ckrecordvalue-c.protocol.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a location object

- [- initWithLatitude:longitude:](<cllocation/init(latitude_longitude_).md>) — Creates a location object with the specified latitude and longitude.
- [- initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:](<cllocation/init(coordinate_altitude_horizontalaccuracy_verticalaccuracy_timestamp_).md>) — Creates a location object with the specified coordinate and altitude information.
- [- initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:speed:timestamp:](<cllocation/init(coordinate_altitude_horizontalaccuracy_verticalaccuracy_course_speed_timestamp_).md>) — Creates a location object with the specified coordinate, altitude, and course information.
- [- initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:courseAccuracy:speed:speedAccuracy:timestamp:](<cllocation/init(coordinate_altitude_horizontalaccuracy_verticalaccuracy_course_courseaccuracy_speed_speedaccuracy_timestamp_).md>) — Creates a location object with the specified coordinate, altitude, course, and accuracy information.
- [- initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:courseAccuracy:speed:speedAccuracy:timestamp:sourceInfo:](<cllocation/init(coordinate_altitude_horizontalaccuracy_verticalaccuracy_course_courseaccuracy_speed_speedaccuracy_timestamp_sourceinfo_).md>)

### Getting the location attributes

- [coordinate](cllocation/coordinate.md) — The geographical coordinate information.
- [altitude](cllocation/altitude.md) — The altitude above mean sea level associated with a location, measured in meters.
- [ellipsoidalAltitude](cllocation/ellipsoidalaltitude.md) — The altitude as a height above the World Geodetic System 1984 (WGS84) ellipsoid, measured in meters.
- [CLLocationDistance](cllocationdistance.md) — A distance in meters from an existing location.
- [floor](cllocation/floor.md) — The logical floor of the building in which the user is located.
- [timestamp](cllocation/timestamp.md) — The time at which this location was determined.
- [sourceInformation](cllocation/sourceinformation.md) — Information about the source that provides the location.

### Getting the location accuracy

- [horizontalAccuracy](cllocation/horizontalaccuracy.md) — The radius of uncertainty for the location, measured in meters.
- [verticalAccuracy](cllocation/verticalaccuracy.md) — The validity of the altitude values, and their estimated uncertainty, measured in meters.
- [CLLocationAccuracy](cllocationaccuracy.md) — The accuracy of a geographical coordinate.

### Measuring the distance between coordinates

- [- distanceFromLocation:](<cllocation/distance(from_).md>) — Returns the distance (measured in meters) from the current object’s location to the specified location.
- [- getDistanceFrom:](<cllocation/getdistancefrom(__).md>) — Returns the distance (measured in meters) from the current object’s location to the specified location. _(deprecated)_

### Getting speed and course information

- [speed](cllocation/speed.md) — The instantaneous speed of the device, measured in meters per second.
- [speedAccuracy](cllocation/speedaccuracy.md) — The accuracy of the speed value, measured in meters per second.
- [course](cllocation/course.md) — The direction in which the device is traveling, measured in degrees and relative to due north.
- [courseAccuracy](cllocation/courseaccuracy.md) — The accuracy of the course value, measured in degrees.
- [CLLocationSpeed](cllocationspeed.md) — The velocity (measured in meters per second) at which the device is moving.
- [CLLocationDirection](cllocationdirection.md) — An azimuth that is measured in degrees relative to true north.
- [CLLocationSpeedAccuracy](cllocationspeedaccuracy.md) — The accuracy of a speed.
- [CLLocationDirectionAccuracy](cllocationdirectionaccuracy.md) — The accuracy of a compass heading.

### Initializers

- [init(coder:)](<cllocation/init(coder_).md>)

## See Also

### Location updates

- [Getting the current location of a device](getting-the-current-location-of-a-device.md) — Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](handling-location-updates-in-the-background.md) — Configure your app to receive location updates when it isn’t running in the foreground.
- [Creating a location push service extension](creating-a-location-push-service-extension.md) — Add and configure an extension to enable your location-sharing app to access a person’s location in response to a request from someone else.
- [CLLocationCoordinate2D](cllocationcoordinate2d.md) — The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
- [CLFloor](clfloor.md) — The floor of a building on which the user’s device is located.
- [CLVisit](clvisit.md) — Information about the user’s location during a specific period of time.
- [CLLocationSourceInformation](cllocationsourceinformation.md) — Information about the source that provides a location.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md) — Define boundaries and act on user location updates.
- [CLServiceSession](clservicesession-pt7n.md) — An object that provides diagnostics about an app’s authorization to use location services.
