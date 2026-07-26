---
title: CLAuthorizationStatus.authorizedAlways
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 9.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clauthorizationstatus/authorizedalways
source_url: 'https://developer.apple.com/documentation/corelocation/clauthorizationstatus/authorizedalways'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clauthorizationstatus/authorizedalways.json'
content_hash: 'sha256:45c88e3708bc2afc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLAuthorizationStatus](../clauthorizationstatus.md)

# CLAuthorizationStatus.authorizedAlways

<sub>Case</sub>

The user authorized the app to start location services at any time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
case authorizedAlways
```

## Discussion

This authorization allows you to use all location services and receive location events whether or not your app is in use.

## See Also

### Getting the authorization status

- [kCLAuthorizationStatusNotDetermined](notdetermined.md) — The user has not chosen whether the app can use location services.
- [kCLAuthorizationStatusRestricted](restricted.md) — The app is not authorized to use location services.
- [kCLAuthorizationStatusDenied](denied.md) — The user denied the use of location services for the app or they are disabled globally in Settings.
- [kCLAuthorizationStatusAuthorized](authorized.md) — The user authorized the app to use location services. _(deprecated)_
- [kCLAuthorizationStatusAuthorizedWhenInUse](authorizedwheninuse.md) — The user authorized the app to start location services while it is in use.
