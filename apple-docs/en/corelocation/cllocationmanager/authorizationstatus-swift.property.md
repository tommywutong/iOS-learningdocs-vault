---
title: authorizationStatus
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/authorizationstatus-swift.property
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/authorizationstatus-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/authorizationstatus-swift.property.json'
content_hash: 'sha256:53b0612c84860ed1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# authorizationStatus

<sub>Instance Property</sub>

The current authorization status for the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var authorizationStatus: CLAuthorizationStatus { get }
```

## Return Value

A value indicating whether the app is authorized to use location services.

## Discussion

Check this value when the [- locationManagerDidChangeAuthorization:](<../cllocationmanagerdelegate/locationmanagerdidchangeauthorization(__).md>) delegate callback indicates that the authorization status has changed.

The system is guaranteed to call the delegate method with the app’s initial authorization state and all authorization status changes.

The system manages the authorization status of a given app according to several factors. Users must authorize the app to use location services explicitly, and location services must be enabled in Settings \> Privacy. See [Choosing the  Location Services Authorization to Request](../../bundleresources/choosing-the-location-services-authorization-to-request.md) for more information.

## See Also

### Requesting authorization for location services

- [- requestWhenInUseAuthorization](<requestwheninuseauthorization().md>) — Requests the user’s permission to use location services while the app is in use.
- [- requestAlwaysAuthorization](<requestalwaysauthorization().md>) — Requests the user’s permission to use location services regardless of whether the app is in use.
- [- requestTemporaryFullAccuracyAuthorizationWithPurposeKey:completion:](<requesttemporaryfullaccuracyauthorization(withpurposekey_completion_).md>) — Requests permission to temporarily use location services with full accuracy and reports the results to the provided completion handler.
- [- requestTemporaryFullAccuracyAuthorizationWithPurposeKey:](<requesttemporaryfullaccuracyauthorization(withpurposekey_).md>) — Requests permission to temporarily use location services with full accuracy.
- [CLAuthorizationStatus](../clauthorizationstatus.md) — Constants that indicate the app’s authorization to use location services.
- [NSLocationDefaultAccuracyReduced](../../bundleresources/information-property-list/nslocationdefaultaccuracyreduced.md) — A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../../bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information at all times.
