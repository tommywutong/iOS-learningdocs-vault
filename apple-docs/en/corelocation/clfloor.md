---
title: CLFloor
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clfloor
source_url: 'https://developer.apple.com/documentation/corelocation/clfloor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clfloor.json'
content_hash: 'sha256:ddbdd055a963d7c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLFloor

<sub>Class</sub>

The floor of a building on which the user’s device is located.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CLFloor
```

## Overview

A [CLFloor](clfloor.md) object specifies the floor of the building on which the device is located. In places where floor information can be determined, a [CLLocation](cllocation.md) object may include a floor object along with the regular location data.

You do not create instances of this class directly, nor should you subclass it.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Getting the floor level

- [level](clfloor/level.md) — The logical floor of the building.

### Initializers

- [init(coder:)](<clfloor/init(coder_).md>)

## See Also

### Location updates

- [Getting the current location of a device](getting-the-current-location-of-a-device.md) — Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](handling-location-updates-in-the-background.md) — Configure your app to receive location updates when it isn’t running in the foreground.
- [Creating a location push service extension](creating-a-location-push-service-extension.md) — Add and configure an extension to enable your location-sharing app to access a person’s location in response to a request from someone else.
- [CLLocation](cllocation.md) — The latitude, longitude, and course information reported by the system.
- [CLLocationCoordinate2D](cllocationcoordinate2d.md) — The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
- [CLVisit](clvisit.md) — Information about the user’s location during a specific period of time.
- [CLLocationSourceInformation](cllocationsourceinformation.md) — Information about the source that provides a location.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md) — Define boundaries and act on user location updates.
- [CLServiceSession](clservicesession-pt7n.md) — An object that provides diagnostics about an app’s authorization to use location services.
