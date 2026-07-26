---
title: CLLocationCoordinate2D
framework: Core Location
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationcoordinate2d
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationcoordinate2d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationcoordinate2d.json'
content_hash: 'sha256:7a83c9b9fc1ad6c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLLocationCoordinate2D

<sub>Structure</sub>

The latitude and longitude associated with a location, specified using the WGS 84 reference frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CLLocationCoordinate2D
```

## Relationships

- **Conforms To**: [Animatable](../swiftui/animatable.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a location coordinate

- [init()](<cllocationcoordinate2d/init().md>) — Creates a location coordinate object.
- [init(latitude:longitude:)](<cllocationcoordinate2d/init(latitude_longitude_).md>) — Creates a location coordination object with the specified latitude and longitude values.
- [CLLocationCoordinate2DMake](<cllocationcoordinate2dmake(____).md>) — Formats a latitude and longitude value into a coordinate data structure format.

### Getting the geographic coordinates

- [latitude](cllocationcoordinate2d/latitude.md) — The latitude in degrees.
- [longitude](cllocationcoordinate2d/longitude.md) — The longitude in degrees.

### Validating a coordinate

- [CLLocationCoordinate2DIsValid](<cllocationcoordinate2disvalid(__).md>) — Returns a Boolean value indicating whether the specified coordinate is valid.
- [kCLLocationCoordinate2DInvalid](kcllocationcoordinate2dinvalid.md) — An invalid coordinate value.

## See Also

### Location updates

- [Getting the current location of a device](getting-the-current-location-of-a-device.md) — Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](handling-location-updates-in-the-background.md) — Configure your app to receive location updates when it isn’t running in the foreground.
- [Creating a location push service extension](creating-a-location-push-service-extension.md) — Add and configure an extension to enable your location-sharing app to access a person’s location in response to a request from someone else.
- [CLLocation](cllocation.md) — The latitude, longitude, and course information reported by the system.
- [CLFloor](clfloor.md) — The floor of a building on which the user’s device is located.
- [CLVisit](clvisit.md) — Information about the user’s location during a specific period of time.
- [CLLocationSourceInformation](cllocationsourceinformation.md) — Information about the source that provides a location.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md) — Define boundaries and act on user location updates.
- [CLServiceSession](clservicesession-pt7n.md) — An object that provides diagnostics about an app’s authorization to use location services.
