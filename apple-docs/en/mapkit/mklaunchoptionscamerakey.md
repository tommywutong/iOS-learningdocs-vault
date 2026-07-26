---
title: MKLaunchOptionsCameraKey
framework: MapKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.1+, iPadOS 7.1+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklaunchoptionscamerakey
source_url: 'https://developer.apple.com/documentation/mapkit/mklaunchoptionscamerakey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklaunchoptionscamerakey.json'
content_hash: 'sha256:044788bcbe0a3214'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKLaunchOptionsCameraKey

<sub>Global Variable</sub>

The virtual camera to use for viewing the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
let MKLaunchOptionsCameraKey: String
```

## Discussion

The value of this key is an [MKMapCamera](mkmapcamera.md) object that describes a virtual camera that can specify a 3D perspective for the map. If you don’t specify this key, the Maps app uses its current settings to define the appearance of the map.

## See Also

### Launch options

- [MKLaunchOptionsDirectionsModeCycling](mklaunchoptionsdirectionsmodecycling.md) — Cycling directions between the specified start and end points.
- [MKLaunchOptionsDirectionsModeDefault](mklaunchoptionsdirectionsmodedefault.md) — Directions that match the user’s preferred transportation type.
- [MKLaunchOptionsDirectionsModeDriving](mklaunchoptionsdirectionsmodedriving.md) — Driving directions between the specified start and end points.
- [MKLaunchOptionsDirectionsModeKey](mklaunchoptionsdirectionsmodekey.md) — The mode of transportation.
- [MKLaunchOptionsDirectionsModeTransit](mklaunchoptionsdirectionsmodetransit.md) — Public transit directions between the specified start and end points.
- [MKLaunchOptionsDirectionsModeWalking](mklaunchoptionsdirectionsmodewalking.md) — Walking directions between the specified start and end points.
- [MKLaunchOptionsMapCenterKey](mklaunchoptionsmapcenterkey.md) — The coordinate value on which to center the map.
- [MKLaunchOptionsMapSpanKey](mklaunchoptionsmapspankey.md) — The amount of the map to display.
- [MKLaunchOptionsMapTypeKey](mklaunchoptionsmaptypekey.md) — The type of map (standard, satellite, or hybrid) to display.
- [MKLaunchOptionsShowsTrafficKey](mklaunchoptionsshowstraffickey.md) — A Boolean value that indicates whether to display traffic information.
