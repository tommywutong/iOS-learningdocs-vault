---
title: 'init(initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:badgePosition:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/lookaroundpreview/init(initialscene:allowsnavigation:showsroadlabels:pointsofinterest:badgeposition:)'
source_url: 'https://developer.apple.com/documentation/mapkit/lookaroundpreview/init(initialscene:allowsnavigation:showsroadlabels:pointsofinterest:badgeposition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/lookaroundpreview/init%28initialscene%3Aallowsnavigation%3Ashowsroadlabels%3Apointsofinterest%3Abadgeposition%3A%29.json'
content_hash: 'sha256:9721f55186c0d696'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [LookAroundPreview](../lookaroundpreview.md)

# init(initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:badgePosition:)

<sub>Initializer</sub>

Creates a Look Around preview with an initial scene, navigation, road label, points of interest, and badge position you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency init(initialScene: MKLookAroundScene?, allowsNavigation: Bool = true, showsRoadLabels: Bool = true, pointsOfInterest: PointOfInterestCategories = .all, badgePosition: MKLookAroundBadgePosition = .topLeading)
```

## Parameters

- `initialScene` — The Look Around scene to display.

- `allowsNavigation` — A Boolean value that indicates whether the Look Around scene allows navigation after the user taps the Look Around preview to enter the full screen Look Around viewer. MapKit never allows navigation on the Look Around preview itself.

- `showsRoadLabels` — A Boolean value that indicates whether the Look Around scene shows road labels after the user taps the Look Around preview to enter the full screen Look Around viewer. MapKit never shows road labels on the Look Around preview itself.

- `pointsOfInterest` — The categories of points of interest to display after the user taps the Look Around preview to enter the full screen Look Around viewer. MapKit never displays points of interest on the Look Around preview itself. By default, MapKit displays all points of interest categories.

- `badgePosition` — A value that controls the position of a badge on the Look Around preview.

## Discussion

Navigation refers to the ability to tap-to-navigate to a different vantage point in the Look Around scene and what a person can control through the use of the `allowsNavigation` property. The framework refers to the ability to pan and zoom around the Look Around scene is as _exploring_ and you can’t restrict it while in the Look Around viewer.

The Look Around viewer isn’t available on macOS and `allowsNavigation` has no effect; in iOS, exploration is always available in the Look Around viewer and you can’t disable it.

## See Also

### Creating a Look Around preview

- [init(scene:allowsNavigation:showsRoadLabels:pointsOfInterest:badgePosition:)](<init(scene_allowsnavigation_showsroadlabels_pointsofinterest_badgeposition_).md>) — Creates a Look Around preview with a binding to a scene, navigation, road label, points of interest, and badge position you specify.
