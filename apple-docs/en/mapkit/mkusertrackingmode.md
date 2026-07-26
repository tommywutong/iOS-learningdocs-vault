---
title: MKUserTrackingMode
framework: MapKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkusertrackingmode
source_url: 'https://developer.apple.com/documentation/mapkit/mkusertrackingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkusertrackingmode.json'
content_hash: 'sha256:c81e83853ef5ccbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKUserTrackingMode

<sub>Enumeration</sub>

The mode to use for tracking the user’s location on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MKUserTrackingMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [MKUserTrackingModeNone](mkusertrackingmode/none.md) — The map doesn’t follow the user’s location.
- [MKUserTrackingModeFollow](mkusertrackingmode/follow.md) — The map follows the user location.
- [MKUserTrackingModeFollowWithHeading](mkusertrackingmode/followwithheading.md) — The map follows the user’s location and rotates when the heading changes.

### Initializers

- [init(rawValue:)](<mkusertrackingmode/init(rawvalue_).md>)

## See Also

### Displaying the user’s location

- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md) — Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [showsUserLocation](mkmapview/showsuserlocation.md) — A Boolean value that indicates whether the map tries to display the user’s location.
- [userLocationVisible](mkmapview/isuserlocationvisible.md) — A Boolean value that indicates whether the user’s location is visible in the map view.
- [userLocation](mkmapview/userlocation.md) — The annotation object that represents the user’s location.
- [userTrackingMode](mkmapview/usertrackingmode.md) — The mode to use for tracking the user’s location.
- [- setUserTrackingMode:animated:](<mkmapview/setusertrackingmode(__animated_).md>) — Sets the mode to use for tracking the user’s location, with optional animation.
