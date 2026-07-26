---
title: Explore a location with a highly detailed map and Look Around
framework: MapKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 16.0+, iPadOS 16.0+, Xcode 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapkit_for_appkit_and_uikit/explore_a_location_with_a_highly_detailed_map_and_look_around
source_url: 'https://developer.apple.com/documentation/mapkit/mapkit_for_appkit_and_uikit/explore_a_location_with_a_highly_detailed_map_and_look_around'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapkit_for_appkit_and_uikit/explore_a_location_with_a_highly_detailed_map_and_look_around.json'
content_hash: 'sha256:a16a822607f81c8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapKit for AppKit and UIKit](../mapkit-for-appkit-and-uikit.md)

# Explore a location with a highly detailed map and Look Around

<sub>Sample Code</sub>

Display a richly detailed map, and use Look Around to experience an interactive view of landmarks.

## Overview

This sample code project takes the user on a tour of landmarks in San Francisco, using MapKit to do the following:

- Show a highly detailed map, including trees, realistic elevation, and detailed building renderings for landmark locations
- Navigate between landmarks, with the navigation route following the elevation of the roads and blending with landscape features
- Animate the map between landmarks
- Display the landmark using an interactive `MKLookAroundViewController`, as well as a snapshot of the landmark with `MKLookAroundSnapshotter`

> [!note] Note
> This sample code project is associated with WWDC22 session [10035: What’s new in MapKit](../../https_/developer.apple.com/wwdc22/10035.md).

## See Also

### Exploring at street level

- [MKLookAroundScene](../mklookaroundscene.md) — A utility class that encapsulates information the framework requires to retrieve and display a specific Look Around location’s imagery.
- [MKLookAroundSceneRequest](../mklookaroundscenerequest.md) — A class you use to request a LookAround scene at the location you specify.
- [MKLookAroundViewController](../mklookaroundviewcontroller.md) — A class that manages the presentation and display of a LookAround view.
- [MKLookAroundSnapshotter](../mklookaroundsnapshotter.md) — A utility class that you use to create a static image from a LookAround scene.

## Download

- [ExploreALocationWithAHighlyDetailedMapAndLookAround.zip](https://docs-assets.developer.apple.com/published/693676fe6d/ExploreALocationWithAHighlyDetailedMapAndLookAround.zip)
