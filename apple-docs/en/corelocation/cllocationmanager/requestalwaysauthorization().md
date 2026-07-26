---
title: requestAlwaysAuthorization()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/requestalwaysauthorization()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/requestalwaysauthorization()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/requestalwaysauthorization%28%29.json'
content_hash: 'sha256:1f0954ac782f67fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# requestAlwaysAuthorization()

<sub>Instance Method</sub>

Requests the user’s permission to use location services regardless of whether the app is in use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
func requestAlwaysAuthorization()
```

## Discussion

You must call this or the [- requestWhenInUseAuthorization](<requestwheninuseauthorization().md>) method before your app can receive location information. To call this method, you must have both [NSLocationAlwaysUsageDescription](../../bundleresources/information-property-list/nslocationalwaysusagedescription.md) and [NSLocationWhenInUseUsageDescription](../../bundleresources/information-property-list/nslocationwheninuseusagedescription.md) keys in your app’s `Info.plist` file. You may call [- requestAlwaysAuthorization](<requestalwaysauthorization().md>) when the current authorization state is either:

- Not Determined — [kCLAuthorizationStatusNotDetermined](../clauthorizationstatus/notdetermined.md)
- When In Use — [kCLAuthorizationStatusAuthorizedWhenInUse](../clauthorizationstatus/authorizedwheninuse.md)

Use the [- locationManager:didUpdateLocations:](<../cllocationmanagerdelegate/locationmanager(__didupdatelocations_).md>) method on the [CLLocationManager](../cllocationmanager.md) delegate to receive updates when the user makes permission choices.

Core Location limits calls to [- requestAlwaysAuthorization](<requestalwaysauthorization().md>). After your app calls this method, further calls have no effect. If a compatible iPad or iPhone app calls this method when running in visionOS, the method treats it as a request for When in Use authorization instead.

### Request Always Authorization After Getting When In Use

To obtain Always authorization, your app must first request When In Use permission followed by requesting Always authorization.

If the user grants When In Use permission after your app calls [- requestWhenInUseAuthorization](<requestwheninuseauthorization().md>), then calling [- requestAlwaysAuthorization](<requestalwaysauthorization().md>) immediately prompts the user to request Always permission. If the user responded to [- requestWhenInUseAuthorization](<requestwheninuseauthorization().md>) with Allow Once, then Core Location ignores further calls to [- requestAlwaysAuthorization](<requestalwaysauthorization().md>) due to the temporary authorization.

> [!note] Note
> In iOS 16 and later, apps that actively track a user’s location or that have recently enabled Core Location display an indicator in Control Center. Be mindful of battery use and user privacy by monitoring the device’s location only when necessary and when the user expects it.

Core Location prompts the user to grant permission with the string from [NSLocationAlwaysUsageDescription](../../bundleresources/information-property-list/nslocationalwaysusagedescription.md). The user prompt displays the following options, which determine the authorization your app can receive:

| Option | Authorization |
|---|---|
| Keep Only While Using | Core Location leaves the authorization as When In Use. The delegate doesn’t receive any updates. |
| Change to Always Allow | Core Location grants your app Always authorization. The delegate receives [kCLAuthorizationStatusAuthorizedAlways](../clauthorizationstatus/authorizedalways.md). |

### Request Always Authorization Directly

If your app’s current state is [kCLAuthorizationStatusNotDetermined](../clauthorizationstatus/notdetermined.md) and you call [- requestAlwaysAuthorization](<requestalwaysauthorization().md>), Core Location uses two prompts before it fully enables Always authorization.

The first prompt displays immediately with the string from [NSLocationWhenInUseUsageDescription](../../bundleresources/information-property-list/nslocationwheninuseusagedescription.md). The user prompt displays the following options, which determine the authorization your app receives:

| Option | Authorization |
|---|---|
| Allow While Using App | Core Location grants your app a Provisional Always authorization. The delegate receives [kCLAuthorizationStatusAuthorizedAlways](../clauthorizationstatus/authorizedalways.md). |
| Allow Once | Core Location grants your app a Temporary When in Use authorization. The delegate receives [kCLAuthorizationStatusAuthorizedWhenInUse](../clauthorizationstatus/authorizedwheninuse.md). This authorization expires when your app is no longer in use, reverting to [kCLAuthorizationStatusNotDetermined](../clauthorizationstatus/notdetermined.md). |
| Don’t Allow | Core Location marks your app with Denied authorization. The delegate receives [kCLAuthorizationStatusDenied](../clauthorizationstatus/denied.md). |

The second prompt displays when Core Location prepares to deliver an event to your app requiring [kCLAuthorizationStatusAuthorizedAlways](../clauthorizationstatus/authorizedalways.md). If the app is in the Provisional Always state, the system displays the second prompt with the string from [NSLocationAlwaysUsageDescription](../../bundleresources/information-property-list/nslocationalwaysusagedescription.md). Core Location will typically display the second prompt when your app isn’t running.

Your app receives permanent Always authorization if the user chooses to grant permission when the second prompt appears while in the Provisional Always state. When the user responds, your app receives either the location event or a call to your delegate with the modified authorization.

When displaying the second prompt, the user sees one of the following options:

| Option | Authorization |
|---|---|
| Keep Only While Using | Core Location changes the authorization to When In Use. The delegate receives [kCLAuthorizationStatusAuthorizedWhenInUse](../clauthorizationstatus/authorizedwheninuse.md). |
| Change to Always Allow | Core Location removes the provisional status, making the Always authorization permanent. The delegate doesn’t receive a callback. |

If the user responds to the prompt near the time it was delivered and chooses to allow the Always permission, the location event will be delivered to your app.

## Topics

### Related Documentation

- [NSLocationAlwaysUsageDescription](../../bundleresources/information-property-list/nslocationalwaysusagedescription.md) — A message that tells people why the app is requesting access to their location at all times. _(deprecated)_

## See Also

### Requesting authorization for location services

- [- requestWhenInUseAuthorization](<requestwheninuseauthorization().md>) — Requests the user’s permission to use location services while the app is in use.
- [- requestTemporaryFullAccuracyAuthorizationWithPurposeKey:completion:](<requesttemporaryfullaccuracyauthorization(withpurposekey_completion_).md>) — Requests permission to temporarily use location services with full accuracy and reports the results to the provided completion handler.
- [- requestTemporaryFullAccuracyAuthorizationWithPurposeKey:](<requesttemporaryfullaccuracyauthorization(withpurposekey_).md>) — Requests permission to temporarily use location services with full accuracy.
- [authorizationStatus](authorizationstatus-swift.property.md) — The current authorization status for the app.
- [CLAuthorizationStatus](../clauthorizationstatus.md) — Constants that indicate the app’s authorization to use location services.
- [NSLocationDefaultAccuracyReduced](../../bundleresources/information-property-list/nslocationdefaultaccuracyreduced.md) — A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../../bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information at all times.
