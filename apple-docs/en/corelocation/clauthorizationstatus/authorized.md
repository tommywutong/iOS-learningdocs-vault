---
title: authorized
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.6+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clauthorizationstatus/authorized
source_url: 'https://developer.apple.com/documentation/corelocation/clauthorizationstatus/authorized'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clauthorizationstatus/authorized.json'
content_hash: 'sha256:86ab384e3245da74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLAuthorizationStatus](../clauthorizationstatus.md)

# authorized

<sub>Type Property</sub>

The user authorized the app to use location services.

> [!warning] Deprecated
> For iOS, use [kCLAuthorizationStatusAuthorizedAlways](authorizedalways.md) or [kCLAuthorizationStatusAuthorizedWhenInUse](authorizedwheninuse.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
static var authorized: CLAuthorizationStatus { get }
```

## See Also

### Getting the authorization status

- [kCLAuthorizationStatusNotDetermined](notdetermined.md) — The user has not chosen whether the app can use location services.
- [kCLAuthorizationStatusRestricted](restricted.md) — The app is not authorized to use location services.
- [kCLAuthorizationStatusDenied](denied.md) — The user denied the use of location services for the app or they are disabled globally in Settings.
- [kCLAuthorizationStatusAuthorizedAlways](authorizedalways.md) — The user authorized the app to start location services at any time.
- [kCLAuthorizationStatusAuthorizedWhenInUse](authorizedwheninuse.md) — The user authorized the app to start location services while it is in use.
