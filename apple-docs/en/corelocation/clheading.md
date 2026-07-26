---
title: CLHeading
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.7+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clheading
source_url: 'https://developer.apple.com/documentation/corelocation/clheading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clheading.json'
content_hash: 'sha256:7c4203686317d84b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLHeading

<sub>Class</sub>

The orientation of the user’s device, relative to true or magnetic north.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
class CLHeading
```

## Overview

A [CLHeading](clheading.md) object contains computed values for the device’s azimuth (orientation) relative to true or magnetic north. It also includes the raw data for the three-dimensional vector used to compute those values. A navigation app might use the information to rotate a map so that it reflects the direction that the user is facing.

Typically, you don’t create instances of this class yourself, nor do you subclass it. Instead, you receive instances of this class through the delegate assigned to the [CLLocationManager](cllocationmanager.md) object whose [- startUpdatingHeading](<cllocationmanager/startupdatingheading().md>) method you called.

> [!note] Note
> If you want heading objects to contain valid data for the [trueHeading](clheading/trueheading.md) property, configure your location manager object to deliver location updates. You can start the delivery of these updates by calling the location manager object’s [- startUpdatingLocation](<cllocationmanager/startupdatinglocation().md>) method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Getting the heading values

- [magneticHeading](clheading/magneticheading.md) — The heading (measured in degrees) relative to magnetic north.
- [trueHeading](clheading/trueheading.md) — The heading (measured in degrees) relative to true north.
- [headingAccuracy](clheading/headingaccuracy.md) — The maximum deviation (measured in degrees) between the reported heading and the true geomagnetic heading.

### Getting the raw heading data

- [x](clheading/x.md) — The geomagnetic data (measured in microteslas) for the x-axis.
- [y](clheading/y.md) — The geomagnetic data (measured in microteslas) for the y-axis.
- [z](clheading/z.md) — The geomagnetic data (measured in microteslas) for the z-axis.
- [CLHeadingComponentValue](clheadingcomponentvalue.md) — A type used to report magnetic differences reported by the onboard hardware.

### Getting the event timestamp

- [timestamp](clheading/timestamp.md) — The time at which this heading was determined.

### Initializers

- [init(coder:)](<clheading/init(coder_).md>)

## See Also

### Compass headings

- [Getting heading and course information](getting-heading-and-course-information.md) — Use a device’s orientation and course information for navigation.
