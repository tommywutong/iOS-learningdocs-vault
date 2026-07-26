---
title: NSLocationAlwaysAndWhenInUseUsageDescription
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 11.0+, iPadOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription.json'
content_hash: 'sha256:24acb31261ff38f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# NSLocationAlwaysAndWhenInUseUsageDescription

<sub>Property List Key</sub>

A message that tells people why the app is requesting access to their location information at all times.

## Discussion

Use this key if your iOS app accesses location information while running in the background. If your app only needs location information when in the foreground, use [NSLocationWhenInUseUsageDescription](nslocationwheninuseusagedescription.md) instead. For more information, see [Choosing the  Location Services Authorization to Request](../choosing-the-location-services-authorization-to-request.md).

If you need location information in a macOS app, use [NSLocationUsageDescription](nslocationusagedescription.md) instead. If your iOS app deploys to versions earlier than iOS 11, see [NSLocationAlwaysUsageDescription](nslocationalwaysusagedescription.md).

> [!important] Important
> This key is required if your iOS app uses APIs that access the user’s location information at all times.

## See Also

### Location

- [Choosing the  Location Services Authorization to Request](../choosing-the-location-services-authorization-to-request.md) — Determine the authorization your app needs to access location data.
- [NSLocationUsageDescription](nslocationusagedescription.md) — A message that tells people why the app is requesting access to their location information.
- [NSLocationWhenInUseUsageDescription](nslocationwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationTemporaryUsageDescriptionDictionary](nslocationtemporaryusagedescriptiondictionary.md) — A collection of messages that explain why the app is requesting temporary access to their location.
- [NSLocationAlwaysUsageDescription](nslocationalwaysusagedescription.md) — A message that tells people why the app is requesting access to their location at all times. _(deprecated)_
- [NSWidgetWantsLocation](nswidgetwantslocation.md) — A Boolean value that indicates a widget uses the user’s location information.
- [NSLocationDefaultAccuracyReduced](nslocationdefaultaccuracyreduced.md) — A Boolean value that indicates whether the app requests reduced location accuracy by default.
