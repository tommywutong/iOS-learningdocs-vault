---
title: CLAuthorizationStatus.restricted
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clauthorizationstatus/restricted
source_url: 'https://developer.apple.com/documentation/corelocation/clauthorizationstatus/restricted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clauthorizationstatus/restricted.json'
content_hash: 'sha256:7088ab4881926ab0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLAuthorizationStatus](../clauthorizationstatus.md)

# CLAuthorizationStatus.restricted

<sub>Case</sub>

The app is not authorized to use location services.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case restricted
```

## Discussion

The user cannot change this app’s status, possibly due to active restrictions such as parental controls being in place.

## See Also

### Getting the authorization status

- [kCLAuthorizationStatusNotDetermined](notdetermined.md) — The user has not chosen whether the app can use location services.
- [kCLAuthorizationStatusDenied](denied.md) — The user denied the use of location services for the app or they are disabled globally in Settings.
- [kCLAuthorizationStatusAuthorized](authorized.md) — The user authorized the app to use location services. _(deprecated)_
- [kCLAuthorizationStatusAuthorizedAlways](authorizedalways.md) — The user authorized the app to start location services at any time.
- [kCLAuthorizationStatusAuthorizedWhenInUse](authorizedwheninuse.md) — The user authorized the app to start location services while it is in use.
