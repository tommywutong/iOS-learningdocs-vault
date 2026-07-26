---
title: 'locationManagerDidChangeAuthorization(_:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanagerdidchangeauthorization(_:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanagerdidchangeauthorization(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanagerdidchangeauthorization%28_%3A%29.json'
content_hash: 'sha256:a92e6539a358f07d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManagerDidChangeAuthorization(_:)

<sub>Instance Method</sub>

Tells the delegate when the app creates the location manager and when the authorization status changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func locationManagerDidChangeAuthorization(_ manager: CLLocationManager)
```

## Parameters

- `manager` — The location manager object reporting the event.

## Discussion

The system calls this method when the app creates the related object’s [CLLocationManager](../cllocationmanager.md) instance, and when the app’s authorization status changes. The status informs the app whether it can access the user’s location.

Use this delegate method to manage your app’s state changes in response to its ability to use location information. For example, you may wish to enable or disable your app’s location-related features, as appropriate. To determine the app’s current authorization, read the new value of the [authorizationStatus](../cllocationmanager/authorizationstatus-swift.property.md) and [accuracyAuthorization](../cllocationmanager/accuracyauthorization.md) properties of the location manager.

> [!important] Important
> Core Location always calls [- locationManagerDidChangeAuthorization:](<locationmanagerdidchangeauthorization(__).md>) when the user’s action results in an authorization status change, and when your app creates an instance of [CLLocationManager](../cllocationmanager.md), whether your app runs in the foreground or in the background.

If the user’s choice doesn’t change the authorization status after you call the [- requestWhenInUseAuthorization](<../cllocationmanager/requestwheninuseauthorization().md>) or [- requestAlwaysAuthorization](<../cllocationmanager/requestalwaysauthorization().md>) method, the location manager doesn’t report the current authorization status to this method—the location manager only reports changes. For example, the location manager calls this method when the status changes from [kCLAuthorizationStatusNotDetermined](../clauthorizationstatus/notdetermined.md) to [kCLAuthorizationStatusAuthorizedWhenInUse](../clauthorizationstatus/authorizedwheninuse.md).

### Events that Cause Authorization Status Changes

An app’s authorization status changes in response to users’ actions. Users can change permission for apps to use location information at any time. The user can:

- Change an app’s location authorization in Settings \> Privacy \> Location Services, or in Settings \> (the app) \> Location Services.
- Turn location services on or off globally in Settings \> Privacy \> Location Services.
- Choose Reset Location & Privacy in Settings \> General \> Reset.

A user’s response to location manager prompts can also change authorization status. For instance, users may change the authorization status by responding to the prompts initiated by calls to [- requestWhenInUseAuthorization](<../cllocationmanager/requestwheninuseauthorization().md>) or [- requestAlwaysAuthorization](<../cllocationmanager/requestalwaysauthorization().md>) methods. For apps with Always authorization, users may change the authorization status to When In Use when responding to the location usage reminder alert.

When an app has temporary authorization, the authorization changes when the user ceases to use the app.

## See Also

### Responding to authorization changes

- [- locationManager:didChangeAuthorizationStatus:](<locationmanager(__didchangeauthorization_).md>) — Tells the delegate its authorization status when the app creates the location manager and when the authorization status changes. _(deprecated)_
