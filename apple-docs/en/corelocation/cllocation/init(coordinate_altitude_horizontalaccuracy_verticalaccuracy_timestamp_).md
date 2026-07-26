---
title: 'init(coordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:)'
framework: Core Location
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:timestamp:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:timestamp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/init%28coordinate%3Aaltitude%3Ahorizontalaccuracy%3Averticalaccuracy%3Atimestamp%3A%29.json'
content_hash: 'sha256:b2e9f29cd7d4d5eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# init(coordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:)

<sub>Initializer</sub>

Creates a location object with the specified coordinate and altitude information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp: Date)
```

## Parameters

- `coordinate` — A coordinate structure containing the latitude and longitude values.

- `altitude` — The altitude value for the location.

- `hAccuracy` — The radius of uncertainty for the geographical coordinate, measured in meters. Specify a negative number to indicate that the geographical coordinate is invalid.

- `vAccuracy` — The accuracy of the altitude value, measured in meters. Specify a negative number to indicate that the altitude is invalid.

- `timestamp` — The time to associate with the location object. Typically, you specify the current time.

## Return Value

A location object initialized with the specified geographical coordinate and altitude information.

## Discussion

Use this method to create location objects that are not necessarily based on the user’s current location.Typically, you acquire location objects from your [CLLocationManager](../cllocationmanager.md) object, which returns the user’s actual location. However, you might use this method when you want to represent any location on a map. For example, you might create an object to represent the user’s intended destination.

This method records the values you provide, and it initializes other properties to appropriate default values. Specifically, this method sets the speed and course values to `-1`.

## See Also

### Creating a location object

- [- initWithLatitude:longitude:](<init(latitude_longitude_).md>) — Creates a location object with the specified latitude and longitude.
- [- initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:speed:timestamp:](<init(coordinate_altitude_horizontalaccuracy_verticalaccuracy_course_speed_timestamp_).md>) — Creates a location object with the specified coordinate, altitude, and course information.
- [- initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:courseAccuracy:speed:speedAccuracy:timestamp:](<init(coordinate_altitude_horizontalaccuracy_verticalaccuracy_course_courseaccuracy_speed_speedaccuracy_timestamp_).md>) — Creates a location object with the specified coordinate, altitude, course, and accuracy information.
- [- initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:courseAccuracy:speed:speedAccuracy:timestamp:sourceInfo:](<init(coordinate_altitude_horizontalaccuracy_verticalaccuracy_course_courseaccuracy_speed_speedaccuracy_timestamp_sourceinfo_).md>)
