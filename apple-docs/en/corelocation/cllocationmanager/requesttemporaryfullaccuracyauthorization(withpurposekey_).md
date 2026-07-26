---
title: 'requestTemporaryFullAccuracyAuthorization(withPurposeKey:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanager/requesttemporaryfullaccuracyauthorization(withpurposekey:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/requesttemporaryfullaccuracyauthorization(withpurposekey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/requesttemporaryfullaccuracyauthorization%28withpurposekey%3A%29.json'
content_hash: 'sha256:5192f4608e475f7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# requestTemporaryFullAccuracyAuthorization(withPurposeKey:)

<sub>Instance Method</sub>

Requests permission to temporarily use location services with full accuracy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func requestTemporaryFullAccuracyAuthorization(withPurposeKey purposeKey: String)
```

## Parameters

- `purposeKey` — A key in the [NSLocationTemporaryUsageDescriptionDictionary](../../bundleresources/information-property-list/nslocationtemporaryusagedescriptiondictionary.md) dictionary of the app’s `Info.plist` file.  The value for this key is an app-provided string that describes the reason for accessing location data with full accuracy.  To localize a usage description, add an entry to your `InfoPlist.strings` file with the same key you provide for this parameter.

## Discussion

This method behaves the same as calling the [- requestTemporaryFullAccuracyAuthorizationWithPurposeKey:completion:](<requesttemporaryfullaccuracyauthorization(withpurposekey_completion_).md>) method, passing `nil` as the completion closure. Use this method if your app’s logic to respond to changes in location data accuracy is already handled by the [- locationManagerDidChangeAuthorization:](<../cllocationmanagerdelegate/locationmanagerdidchangeauthorization(__).md>) delegate method, and your app doesn’t have any work to do in the closure.

## See Also

### Requesting authorization for location services

- [- requestWhenInUseAuthorization](<requestwheninuseauthorization().md>) — Requests the user’s permission to use location services while the app is in use.
- [- requestAlwaysAuthorization](<requestalwaysauthorization().md>) — Requests the user’s permission to use location services regardless of whether the app is in use.
- [- requestTemporaryFullAccuracyAuthorizationWithPurposeKey:completion:](<requesttemporaryfullaccuracyauthorization(withpurposekey_completion_).md>) — Requests permission to temporarily use location services with full accuracy and reports the results to the provided completion handler.
- [authorizationStatus](authorizationstatus-swift.property.md) — The current authorization status for the app.
- [CLAuthorizationStatus](../clauthorizationstatus.md) — Constants that indicate the app’s authorization to use location services.
- [NSLocationDefaultAccuracyReduced](../../bundleresources/information-property-list/nslocationdefaultaccuracyreduced.md) — A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../../bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information at all times.
