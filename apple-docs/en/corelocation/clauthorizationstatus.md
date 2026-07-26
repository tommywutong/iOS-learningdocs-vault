---
title: CLAuthorizationStatus
framework: Core Location
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clauthorizationstatus
source_url: 'https://developer.apple.com/documentation/corelocation/clauthorizationstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clauthorizationstatus.json'
content_hash: 'sha256:ef483becf170e3db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLAuthorizationStatus

<sub>Enumeration</sub>

Constants that indicate the app’s authorization to use location services.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CLAuthorizationStatus
```

## Overview

Handle changes to authorization status in your location manager’s delegate method, [- locationManager:didChangeAuthorizationStatus:](<cllocationmanagerdelegate/locationmanager(__didchangeauthorization_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the authorization status

- [kCLAuthorizationStatusNotDetermined](clauthorizationstatus/notdetermined.md) — The user has not chosen whether the app can use location services.
- [kCLAuthorizationStatusRestricted](clauthorizationstatus/restricted.md) — The app is not authorized to use location services.
- [kCLAuthorizationStatusDenied](clauthorizationstatus/denied.md) — The user denied the use of location services for the app or they are disabled globally in Settings.
- [kCLAuthorizationStatusAuthorized](clauthorizationstatus/authorized.md) — The user authorized the app to use location services. _(deprecated)_
- [kCLAuthorizationStatusAuthorizedAlways](clauthorizationstatus/authorizedalways.md) — The user authorized the app to start location services at any time.
- [kCLAuthorizationStatusAuthorizedWhenInUse](clauthorizationstatus/authorizedwheninuse.md) — The user authorized the app to start location services while it is in use.

### Initializers

- [init(rawValue:)](<clauthorizationstatus/init(rawvalue_).md>)

## See Also

### Authorization

- [Requesting authorization to use location services](requesting-authorization-to-use-location-services.md) — Obtain authorization to use location services and manage changes to your app’s authorization status.
- [Suspending authorization requests](suspending-authorization-requests.md) — Defer the system’s authorization request dialog until your app is ready.
- [CLAccuracyAuthorization](claccuracyauthorization.md) — Constants that indicate the level of location accuracy the app has authorization to use.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information at all times.
- [NSLocationWhenInUseUsageDescription](../bundleresources/information-property-list/nslocationwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationUsageDescription](../bundleresources/information-property-list/nslocationusagedescription.md) — A message that tells people why the app is requesting access to their location information. _(deprecated)_
- [NSLocationDefaultAccuracyReduced](../bundleresources/information-property-list/nslocationdefaultaccuracyreduced.md) — A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysUsageDescription](../bundleresources/information-property-list/nslocationalwaysusagedescription.md) — A message that tells people why the app is requesting access to their location at all times. _(deprecated)_
