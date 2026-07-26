---
title: CLAccuracyAuthorization
framework: Core Location
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/claccuracyauthorization
source_url: 'https://developer.apple.com/documentation/corelocation/claccuracyauthorization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/claccuracyauthorization.json'
content_hash: 'sha256:4c818699d637e271'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLAccuracyAuthorization

<sub>Enumeration</sub>

Constants that indicate the level of location accuracy the app has authorization to use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CLAccuracyAuthorization
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the location accuracy

- [CLAccuracyAuthorizationFullAccuracy](claccuracyauthorization/fullaccuracy.md) — The user authorized the app to access location data with full accuracy.
- [CLAccuracyAuthorizationReducedAccuracy](claccuracyauthorization/reducedaccuracy.md) — The user authorized the app to access location data with reduced accuracy.

### Initializers

- [init(rawValue:)](<claccuracyauthorization/init(rawvalue_).md>)

## See Also

### Authorization

- [Requesting authorization to use location services](requesting-authorization-to-use-location-services.md) — Obtain authorization to use location services and manage changes to your app’s authorization status.
- [Suspending authorization requests](suspending-authorization-requests.md) — Defer the system’s authorization request dialog until your app is ready.
- [CLAuthorizationStatus](clauthorizationstatus.md) — Constants that indicate the app’s authorization to use location services.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information at all times.
- [NSLocationWhenInUseUsageDescription](../bundleresources/information-property-list/nslocationwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationUsageDescription](../bundleresources/information-property-list/nslocationusagedescription.md) — A message that tells people why the app is requesting access to their location information. _(deprecated)_
- [NSLocationDefaultAccuracyReduced](../bundleresources/information-property-list/nslocationdefaultaccuracyreduced.md) — A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysUsageDescription](../bundleresources/information-property-list/nslocationalwaysusagedescription.md) — A message that tells people why the app is requesting access to their location at all times. _(deprecated)_
