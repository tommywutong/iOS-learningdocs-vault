---
title: MKLaunchOptionsShowsTrafficKey
framework: MapKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklaunchoptionsshowstraffickey
source_url: 'https://developer.apple.com/documentation/mapkit/mklaunchoptionsshowstraffickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklaunchoptionsshowstraffickey.json'
content_hash: 'sha256:c6b23abd446c33eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKLaunchOptionsShowsTrafficKey

<sub>Global Variable</sub>

A Boolean value that indicates whether to display traffic information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let MKLaunchOptionsShowsTrafficKey: String
```

## Discussion

The value of this key is an [NSNumber](../foundation/nsnumber.md) object that contains a Boolean value. If you don’t specify this key, the Maps app uses its current settings to determine whether to display traffic.

## See Also

### Launch options

- [MKLaunchOptionsCameraKey](mklaunchoptionscamerakey.md) — The virtual camera to use for viewing the map.
- [MKLaunchOptionsDirectionsModeCycling](mklaunchoptionsdirectionsmodecycling.md) — Cycling directions between the specified start and end points.
- [MKLaunchOptionsDirectionsModeDefault](mklaunchoptionsdirectionsmodedefault.md) — Directions that match the user’s preferred transportation type.
- [MKLaunchOptionsDirectionsModeDriving](mklaunchoptionsdirectionsmodedriving.md) — Driving directions between the specified start and end points.
- [MKLaunchOptionsDirectionsModeKey](mklaunchoptionsdirectionsmodekey.md) — The mode of transportation.
- [MKLaunchOptionsDirectionsModeTransit](mklaunchoptionsdirectionsmodetransit.md) — Public transit directions between the specified start and end points.
- [MKLaunchOptionsDirectionsModeWalking](mklaunchoptionsdirectionsmodewalking.md) — Walking directions between the specified start and end points.
- [MKLaunchOptionsMapCenterKey](mklaunchoptionsmapcenterkey.md) — The coordinate value on which to center the map.
- [MKLaunchOptionsMapSpanKey](mklaunchoptionsmapspankey.md) — The amount of the map to display.
- [MKLaunchOptionsMapTypeKey](mklaunchoptionsmaptypekey.md) — The type of map (standard, satellite, or hybrid) to display.
