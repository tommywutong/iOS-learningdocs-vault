---
title: NSLocationUsageDescription
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 6.0+（8.0 起废弃）, iPadOS 6.0+（8.0 起废弃）, macOS 10.14+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/nslocationusagedescription
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationusagedescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/nslocationusagedescription.json'
content_hash: 'sha256:6f3b7b50e8bec77a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# NSLocationUsageDescription

<sub>Property List Key</sub>

A message that tells people why the app is requesting access to their location information.

## Discussion

Use this key in a macOS app that accesses the user’s location information. In an iOS app, use [NSLocationWhenInUseUsageDescription](nslocationwheninuseusagedescription.md) or [NSLocationAlwaysAndWhenInUseUsageDescription](nslocationalwaysandwheninuseusagedescription.md) instead.

> [!important] Important
> This key is required if your macOS app uses APIs that access the user’s location information.

## See Also

### Location

- [Choosing the  Location Services Authorization to Request](../choosing-the-location-services-authorization-to-request.md) — Determine the authorization your app needs to access location data.
- [NSLocationAlwaysAndWhenInUseUsageDescription](nslocationalwaysandwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information at all times.
- [NSLocationWhenInUseUsageDescription](nslocationwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationTemporaryUsageDescriptionDictionary](nslocationtemporaryusagedescriptiondictionary.md) — A collection of messages that explain why the app is requesting temporary access to their location.
- [NSLocationAlwaysUsageDescription](nslocationalwaysusagedescription.md) — A message that tells people why the app is requesting access to their location at all times. _(deprecated)_
- [NSWidgetWantsLocation](nswidgetwantslocation.md) — A Boolean value that indicates a widget uses the user’s location information.
- [NSLocationDefaultAccuracyReduced](nslocationdefaultaccuracyreduced.md) — A Boolean value that indicates whether the app requests reduced location accuracy by default.
