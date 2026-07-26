---
title: 'init(coordinate:altitude:horizontalAccuracy:verticalAccuracy:course:speed:timestamp:)'
framework: Core Location
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:speed:timestamp:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:speed:timestamp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/init%28coordinate%3Aaltitude%3Ahorizontalaccuracy%3Averticalaccuracy%3Acourse%3Aspeed%3Atimestamp%3A%29.json'
content_hash: 'sha256:21c0494fd87d0395'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# init(coordinate:altitude:horizontalAccuracy:verticalAccuracy:course:speed:timestamp:)

<sub>Initializer</sub>

Creates a location object with the specified coordinate, altitude, and course information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course: CLLocationDirection, speed: CLLocationSpeed, timestamp: Date)
```

## Parameters

- `coordinate` — A coordinate structure containing the latitude and longitude values.

- `altitude` — The altitude value for the location.

- `hAccuracy` — The radius of uncertainty for the geographical coordinate, measured in meters. Specify a negative number to indicate that the geographical coordinate is invalid.

- `vAccuracy` — The accuracy of the altitude value, measured in meters. Specify a negative number to indicate that the altitude is invalid.

- `course` — The direction of travel for the location, measured in degrees relative to due north and continuing clockwise around the compass.

- `speed` — The current speed associated with this location, measured in meters per second.

- `timestamp` — The time to associate with the location object. Typically, you specify the current time.

## Return Value

A location object initialized with the specified geographical coordinate, altitude, and course information.

## Discussion

Use this method to create location objects that aren’t necessarily based on the user’s current location.Typically, you acquire location objects from your [CLLocationManager](../cllocationmanager.md) object, which returns the user’s actual location. However, you might use this method when you want to represent any location on a map. For example, you might create an object to represent the user’s intended destination.

## See Also

### Creating a location object

- [- initWithLatitude:longitude:](<init(latitude_longitude_).md>) — Creates a location object with the specified latitude and longitude.
- [- initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:](<init(coordinate_altitude_horizontalaccuracy_verticalaccuracy_timestamp_).md>) — Creates a location object with the specified coordinate and altitude information.
- [- initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:courseAccuracy:speed:speedAccuracy:timestamp:](<init(coordinate_altitude_horizontalaccuracy_verticalaccuracy_course_courseaccuracy_speed_speedaccuracy_timestamp_).md>) — Creates a location object with the specified coordinate, altitude, course, and accuracy information.
- [- initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:courseAccuracy:speed:speedAccuracy:timestamp:sourceInfo:](<init(coordinate_altitude_horizontalaccuracy_verticalaccuracy_course_courseaccuracy_speed_speedaccuracy_timestamp_sourceinfo_).md>)
