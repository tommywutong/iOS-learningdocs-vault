---
title: Launch options dictionary keys
framework: MapKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/launch-options-dictionary-keys
source_url: 'https://developer.apple.com/documentation/mapkit/launch-options-dictionary-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/launch-options-dictionary-keys.json'
content_hash: 'sha256:747aad999ccae5df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md) · [MapKit for AppKit and UIKit](mapkit-for-appkit-and-uikit.md) · [MKMapItem](mkmapitem.md)

# Launch options dictionary keys

<sub>API Collection</sub>

Launch options to specify when opening map items in the Maps app.

## Overview

You specify these keys in the launch options dictionary for the [+ openMapsWithItems:launchOptions:](<mkmapitem/openmaps(with_launchoptions_).md>) or [- openInMapsWithLaunchOptions:](<mkmapitem/openinmaps(launchoptions_).md>) method.

## Topics

### Launch options

- [MKLaunchOptionsDirectionsModeKey](mklaunchoptionsdirectionsmodekey.md) — The mode of transportation.
- [MKLaunchOptionsMapTypeKey](mklaunchoptionsmaptypekey.md) — The type of map (standard, satellite, or hybrid) to display.
- [MKLaunchOptionsMapCenterKey](mklaunchoptionsmapcenterkey.md) — The coordinate value on which to center the map.
- [MKLaunchOptionsMapSpanKey](mklaunchoptionsmapspankey.md) — The amount of the map to display.
- [MKLaunchOptionsShowsTrafficKey](mklaunchoptionsshowstraffickey.md) — A Boolean value that indicates whether to display traffic information.
- [MKLaunchOptionsCameraKey](mklaunchoptionscamerakey.md) — The virtual camera to use for viewing the map.

## See Also

### Opening items at launch time

- [Directions mode values](directions-mode-values.md) — Strings that represent the possible values of the launch options direction mode key.
