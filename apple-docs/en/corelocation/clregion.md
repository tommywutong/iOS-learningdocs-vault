---
title: CLRegion
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clregion
source_url: 'https://developer.apple.com/documentation/corelocation/clregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clregion.json'
content_hash: 'sha256:fea7e505ac032200'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLRegion

<sub>Class</sub>

A base class representing an area that can be monitored.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
class CLRegion
```

## Overview

This is an abstract base class. Instantiate one of the provided subclasses that define specific types of regions. After you create a region, register it with a [CLLocationManager](cllocationmanager.md) object with the [- startMonitoringForRegion:](<cllocationmanager/startmonitoring(for_).md>) method. The location manager generates appropriate events whenever the user crosses the boundaries of the region.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [CLBeaconRegion](clbeaconregion.md), [CLCircularRegion](clcircularregion.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Getting the region identifier

- [identifier](clregion/identifier.md) — The identifier for the region object.

### Specifying the notification conditions

- [notifyOnEntry](clregion/notifyonentry.md) — A Boolean indicating that notifications are generated upon entry into the region.
- [notifyOnExit](clregion/notifyonexit.md) — A Boolean indicating that notifications are generated upon exit from the region.

### Deprecated

- [- initCircularRegionWithCenter:radius:identifier:](<clregion/init(circularregionwithcenter_radius_identifier_).md>) — Initializes and returns a region object defining a circular area. _(deprecated)_
- [- containsCoordinate:](<clregion/contains(__).md>) — Returns a Boolean value indicating whether the region contains the specified coordinate. _(deprecated)_
- [center](clregion/center.md) — The center point of the region. _(deprecated)_
- [radius](clregion/radius.md) — The radius (measured in meters) that defines the region’s outer boundary. _(deprecated)_

### Initializers

- [init(coder:)](<clregion/init(coder_).md>)

## See Also

### Region monitoring

- [Monitoring the user’s proximity to geographic regions](monitoring-the-user-s-proximity-to-geographic-regions.md) — Use condition monitoring to determine when the user enters or leaves a geographic region.
