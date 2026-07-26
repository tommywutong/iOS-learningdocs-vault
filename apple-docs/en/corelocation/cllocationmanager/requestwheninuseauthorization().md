---
title: requestWhenInUseAuthorization()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/requestwheninuseauthorization()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/requestwheninuseauthorization()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/requestwheninuseauthorization%28%29.json'
content_hash: 'sha256:aaaa34ccf2d88172'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# requestWhenInUseAuthorization()

<sub>Instance Method</sub>

Requests the user’s permission to use location services while the app is in use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func requestWhenInUseAuthorization()
```

## Discussion

You must call this method or [- requestAlwaysAuthorization](<requestalwaysauthorization().md>) before you can receive location-related information. You may call [- requestWhenInUseAuthorization](<requestwheninuseauthorization().md>) whenever the current authorization status is not determined ([kCLAuthorizationStatusNotDetermined](../clauthorizationstatus/notdetermined.md)).

> [!important] Important
> Your app must be in the foreground to show a location authorization prompt.

This method runs asynchronously and prompts the user to grant permission to the app to use location services. The user prompt contains the text from the [NSLocationWhenInUseUsageDescription](../../bundleresources/information-property-list/nslocationwheninuseusagedescription.md) key in your app `Info.plist` file, and the presence of that key is required when calling this method. The user prompt displays the following options, which determine the authorization your app can receive.

| Option | Authorization |
|---|---|
| Allow While Using App | When In Use authorization that does not expire. |
| Allow Once | Temporary When In Use authorization that expires when the app is no longer in use. |
| Don’t Allow | Denied; no further authorization requests are allowed. |

After the user makes a selection and determines the status, the location manager delivers the results to the delegate’s [- locationManager:didChangeAuthorizationStatus:](<../cllocationmanagerdelegate/locationmanager(__didchangeauthorization_).md>) method. If the initial authorization status is anything other than [kCLAuthorizationStatusNotDetermined](../clauthorizationstatus/notdetermined.md), this method does nothing and doesn’t call the [- locationManager:didChangeAuthorizationStatus:](<../cllocationmanagerdelegate/locationmanager(__didchangeauthorization_).md>) method.

If the user’s choice grants When In Use authorization to your app, your app can start any location service and is eligible to receive the results while it’s in use. If the user’s choice grants temporary When In Use authorization, the authorization expires when the app is no longer in use, reverting to Not Determined status ([kCLAuthorizationStatusNotDetermined](../clauthorizationstatus/notdetermined.md)). For information about when an app is considered to be in use, see [Choosing the  Location Services Authorization to Request](../../bundleresources/choosing-the-location-services-authorization-to-request.md).

When your app starts standard location services in the foreground, they continue to run in the background if your app has enabled background location updates in the Capabilities tab of your Xcode project. Attempts to start location updates while your app runs in the background will fail. The system displays a location services indicator in the status bar when your app moves to the background with active location services.

> [!note] Note
> In iOS 16 and later, apps that actively track a user’s location or that have recently enabled Core Location display an indicator in Control Center. Be mindful of battery use and user privacy by monitoring the device’s location only when necessary and when the user expects it.

## Topics

### Related Documentation

- [Handling location updates in the background](../handling-location-updates-in-the-background.md) — Configure your app to receive location updates when it isn’t running in the foreground.
- [NSLocationWhenInUseUsageDescription](../../bundleresources/information-property-list/nslocationwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information while the app is running in the foreground.

## See Also

### Requesting authorization for location services

- [- requestAlwaysAuthorization](<requestalwaysauthorization().md>) — Requests the user’s permission to use location services regardless of whether the app is in use.
- [- requestTemporaryFullAccuracyAuthorizationWithPurposeKey:completion:](<requesttemporaryfullaccuracyauthorization(withpurposekey_completion_).md>) — Requests permission to temporarily use location services with full accuracy and reports the results to the provided completion handler.
- [- requestTemporaryFullAccuracyAuthorizationWithPurposeKey:](<requesttemporaryfullaccuracyauthorization(withpurposekey_).md>) — Requests permission to temporarily use location services with full accuracy.
- [authorizationStatus](authorizationstatus-swift.property.md) — The current authorization status for the app.
- [CLAuthorizationStatus](../clauthorizationstatus.md) — Constants that indicate the app’s authorization to use location services.
- [NSLocationDefaultAccuracyReduced](../../bundleresources/information-property-list/nslocationdefaultaccuracyreduced.md) — A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../../bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information at all times.
