---
title: CLAuthorizationStatus.denied
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clauthorizationstatus/denied
source_url: 'https://developer.apple.com/documentation/corelocation/clauthorizationstatus/denied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clauthorizationstatus/denied.json'
content_hash: 'sha256:a4897fa1e4786307'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLAuthorizationStatus](../clauthorizationstatus.md)

# CLAuthorizationStatus.denied

<sub>Case</sub>

The user denied the use of location services for the app or they are disabled globally in Settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case denied
```

## Discussion

When the authorization status is denied, your app can’t use location services. The status can be denied when:

- The user denied location permissions for your app.
- The user turned off location services for the device in Settings.
- Location services are unavailable because the device is in Airplane mode.

If the user re-enables location services in Settings, your app’s authorization returns to its previous state. The status change is reported to your delegate’s [- locationManager:didChangeAuthorizationStatus:](<../cllocationmanagerdelegate/locationmanager(__didchangeauthorization_).md>) method.

You may call [+ locationServicesEnabled](<../cllocationmanager/locationservicesenabled().md>) if you wish to determine whether location services are available globally on the device.

## See Also

### Getting the authorization status

- [kCLAuthorizationStatusNotDetermined](notdetermined.md) — The user has not chosen whether the app can use location services.
- [kCLAuthorizationStatusRestricted](restricted.md) — The app is not authorized to use location services.
- [kCLAuthorizationStatusAuthorized](authorized.md) — The user authorized the app to use location services. _(deprecated)_
- [kCLAuthorizationStatusAuthorizedAlways](authorizedalways.md) — The user authorized the app to start location services at any time.
- [kCLAuthorizationStatusAuthorizedWhenInUse](authorizedwheninuse.md) — The user authorized the app to start location services while it is in use.
