---
title: NSLocationAlwaysUsageDescription
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/bundleresources/information-property-list/nslocationalwaysusagedescription
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription.json'
content_hash: 'sha256:08187dd54ef23f1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# NSLocationAlwaysUsageDescription

<sub>Property List Key</sub>

A message that tells people why the app is requesting access to their location at all times.

> [!warning] Deprecated
> For apps deployed to targets in iOS 11 and later, use [NSLocationAlwaysAndWhenInUseUsageDescription](nslocationalwaysandwheninuseusagedescription.md) instead.

## Discussion

Use this key if your iOS app accesses location information in the background, and you deploy to a target earlier than iOS 11. In that case, add both this key and [NSLocationAlwaysAndWhenInUseUsageDescription](nslocationalwaysandwheninuseusagedescription.md) to your app’s `Info.plist` file with the same message. Apps running on older versions of the OS use the message associated with [NSLocationAlwaysUsageDescription](nslocationalwaysusagedescription.md), while apps running on later versions use the one associated with [NSLocationAlwaysAndWhenInUseUsageDescription](nslocationalwaysandwheninuseusagedescription.md).

If your app only needs location information when in the foreground, use [NSLocationWhenInUseUsageDescription](nslocationwheninuseusagedescription.md) instead. For more information, see [Choosing the  Location Services Authorization to Request](../choosing-the-location-services-authorization-to-request.md).

If you need location information in a macOS app, use [NSLocationUsageDescription](nslocationusagedescription.md) instead.

> [!important] Important
> This key is required if your iOS app uses APIs that access the user’s location at all times and deploys to targets earlier than iOS 11.

## See Also

### Location

- [Choosing the  Location Services Authorization to Request](../choosing-the-location-services-authorization-to-request.md) — Determine the authorization your app needs to access location data.
- [NSLocationAlwaysAndWhenInUseUsageDescription](nslocationalwaysandwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information at all times.
- [NSLocationUsageDescription](nslocationusagedescription.md) — A message that tells people why the app is requesting access to their location information.
- [NSLocationWhenInUseUsageDescription](nslocationwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationTemporaryUsageDescriptionDictionary](nslocationtemporaryusagedescriptiondictionary.md) — A collection of messages that explain why the app is requesting temporary access to their location.
- [NSWidgetWantsLocation](nswidgetwantslocation.md) — A Boolean value that indicates a widget uses the user’s location information.
- [NSLocationDefaultAccuracyReduced](nslocationdefaultaccuracyreduced.md) — A Boolean value that indicates whether the app requests reduced location accuracy by default.
