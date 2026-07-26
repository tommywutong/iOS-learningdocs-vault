---
title: MKLaunchOptionsMapSpanKey
framework: MapKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklaunchoptionsmapspankey
source_url: 'https://developer.apple.com/documentation/mapkit/mklaunchoptionsmapspankey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklaunchoptionsmapspankey.json'
content_hash: 'sha256:edffc00dcb909579'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKLaunchOptionsMapSpanKey

<sub>Global Variable</sub>

The amount of the map to display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
let MKLaunchOptionsMapSpanKey: String
```

## Discussion

The value of this key is an [NSValue](../foundation/nsvalue.md) object that contains an encoded [MKCoordinateSpan](mkcoordinatespan.md) structure.

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
- [MKLaunchOptionsMapTypeKey](mklaunchoptionsmaptypekey.md) — The type of map (standard, satellite, or hybrid) to display.
- [MKLaunchOptionsShowsTrafficKey](mklaunchoptionsshowstraffickey.md) — A Boolean value that indicates whether to display traffic information.
