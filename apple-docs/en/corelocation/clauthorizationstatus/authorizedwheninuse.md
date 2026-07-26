---
title: CLAuthorizationStatus.authorizedWhenInUse
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clauthorizationstatus/authorizedwheninuse
source_url: 'https://developer.apple.com/documentation/corelocation/clauthorizationstatus/authorizedwheninuse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clauthorizationstatus/authorizedwheninuse.json'
content_hash: 'sha256:f0e4000c2606c22b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLAuthorizationStatus](../clauthorizationstatus.md)

# CLAuthorizationStatus.authorizedWhenInUse

<sub>Case</sub>

The user authorized the app to start location services while it is in use.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case authorizedWhenInUse
```

## Discussion

This authorization allows you to use all location services and receive location events only when your app is in use. To continue using location services in the background, enable Continuous Background Location Updates and start the services while the app is in use.

## See Also

### Getting the authorization status

- [kCLAuthorizationStatusNotDetermined](notdetermined.md) — The user has not chosen whether the app can use location services.
- [kCLAuthorizationStatusRestricted](restricted.md) — The app is not authorized to use location services.
- [kCLAuthorizationStatusDenied](denied.md) — The user denied the use of location services for the app or they are disabled globally in Settings.
- [kCLAuthorizationStatusAuthorized](authorized.md) — The user authorized the app to use location services. _(deprecated)_
- [kCLAuthorizationStatusAuthorizedAlways](authorizedalways.md) — The user authorized the app to start location services at any time.
