---
title: CLAuthorizationStatus.notDetermined
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clauthorizationstatus/notdetermined
source_url: 'https://developer.apple.com/documentation/corelocation/clauthorizationstatus/notdetermined'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clauthorizationstatus/notdetermined.json'
content_hash: 'sha256:958286b7aa607145'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLAuthorizationStatus](../clauthorizationstatus.md)

# CLAuthorizationStatus.notDetermined

<sub>Case</sub>

The user has not chosen whether the app can use location services.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case notDetermined
```

## Discussion

When the authorization status is Not Determined, request authorization causes the location manager to prompt the user for permission if the app is in the foreground. See [- requestWhenInUseAuthorization](<../cllocationmanager/requestwheninuseauthorization().md>) and [- requestAlwaysAuthorization](<../cllocationmanager/requestalwaysauthorization().md>) for more information.

## See Also

### Getting the authorization status

- [kCLAuthorizationStatusRestricted](restricted.md) — The app is not authorized to use location services.
- [kCLAuthorizationStatusDenied](denied.md) — The user denied the use of location services for the app or they are disabled globally in Settings.
- [kCLAuthorizationStatusAuthorized](authorized.md) — The user authorized the app to use location services. _(deprecated)_
- [kCLAuthorizationStatusAuthorizedAlways](authorizedalways.md) — The user authorized the app to start location services at any time.
- [kCLAuthorizationStatusAuthorizedWhenInUse](authorizedwheninuse.md) — The user authorized the app to start location services while it is in use.
