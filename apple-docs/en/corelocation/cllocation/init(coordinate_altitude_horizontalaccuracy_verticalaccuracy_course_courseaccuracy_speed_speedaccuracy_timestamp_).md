---
title: 'init(coordinate:altitude:horizontalAccuracy:verticalAccuracy:course:courseAccuracy:speed:speedAccuracy:timestamp:)'
framework: Core Location
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 13.4+, visionOS 1.0+, watchOS 6.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:courseaccuracy:speed:speedaccuracy:timestamp:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:courseaccuracy:speed:speedaccuracy:timestamp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/init%28coordinate%3Aaltitude%3Ahorizontalaccuracy%3Averticalaccuracy%3Acourse%3Acourseaccuracy%3Aspeed%3Aspeedaccuracy%3Atimestamp%3A%29.json'
content_hash: 'sha256:7e526580c1df265a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# init(coordinate:altitude:horizontalAccuracy:verticalAccuracy:course:courseAccuracy:speed:speedAccuracy:timestamp:)

<sub>Initializer</sub>

Creates a location object with the specified coordinate, altitude, course, and accuracy information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course: CLLocationDirection, courseAccuracy: CLLocationDirectionAccuracy, speed: CLLocationSpeed, speedAccuracy: CLLocationSpeedAccuracy, timestamp: Date)
```

## Parameters

- `coordinate` — A coordinate structure containing the latitude and longitude values.

- `altitude` — The altitude value for the location.

- `hAccuracy` — The radius of uncertainty for the geographical coordinate, measured in meters. Specify a negative number to indicate that the geographical coordinate is invalid.

- `vAccuracy` — The accuracy of the altitude value, measured in meters. Specify a negative number to indicate that the altitude is invalid.

- `course` — The direction of travel for the location, measured in degrees relative to due north and continuing clockwise around the compass.

- `courseAccuracy` — The accuracy of the course value, measured in degrees. Specify a negative number to indicate that the course is invalid.

- `speed` — The current speed associated with this location, measured in meters per second.

- `speedAccuracy` — The accuracy of the speed value, measured in meters per second. Specify a negative number to indicate that the speed is invalid.

- `timestamp` — The time to associate with the location object. Typically, you specify the current time.

## See Also

### Creating a location object

- [- initWithLatitude:longitude:](<init(latitude_longitude_).md>) — Creates a location object with the specified latitude and longitude.
- [- initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:](<init(coordinate_altitude_horizontalaccuracy_verticalaccuracy_timestamp_).md>) — Creates a location object with the specified coordinate and altitude information.
- [- initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:speed:timestamp:](<init(coordinate_altitude_horizontalaccuracy_verticalaccuracy_course_speed_timestamp_).md>) — Creates a location object with the specified coordinate, altitude, and course information.
- [- initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:courseAccuracy:speed:speedAccuracy:timestamp:sourceInfo:](<init(coordinate_altitude_horizontalaccuracy_verticalaccuracy_course_courseaccuracy_speed_speedaccuracy_timestamp_sourceinfo_).md>)
