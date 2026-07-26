---
title: MKUserTrackingBarButtonItem
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkusertrackingbarbuttonitem
source_url: 'https://developer.apple.com/documentation/mapkit/mkusertrackingbarbuttonitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkusertrackingbarbuttonitem.json'
content_hash: 'sha256:ade4166e7be2aea4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKUserTrackingBarButtonItem

<sub>Class</sub>

A specialized bar button item that allows the user to toggle whether the map tracks to the heading the user is facing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class MKUserTrackingBarButtonItem
```

## Overview

Tapping the button lets the user toggles between modes for displaying the map with and without the current heading applied. The button also reflects the current user tracking mode if set elsewhere. This bar button item is associated to a single map view.

## Relationships

- **Inherits From**: [UIBarButtonItem](../uikit/uibarbuttonitem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md), [UIAppearance](../uikit/uiappearance.md), [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md), [UISpringLoadedInteractionSupporting](../uikit/uispringloadedinteractionsupporting.md)

## Topics

### Creating a user tracking bar button item

- [- initWithMapView:](<mkusertrackingbarbuttonitem/init(mapview_).md>) — Initializes a newly created bar button item with the specified map view.

### Accessing the owning map

- [mapView](mkusertrackingbarbuttonitem/mapview.md) — The map view associated with this bar button item.

## See Also

### Map customization

- [MKMapCamera](mkmapcamera.md) — A virtual camera for defining the appearance of the map.
- [MKCompassButton](mkcompassbutton.md) — A specialized view that displays the compass heading for its associated map.
- [MKScaleView](mkscaleview.md) — A specialized view that displays the scale information for its associated map.
- [MKZoomControl](mkzoomcontrol.md) — A specialized view that displays and controls the zoom level of the map view.
- [MKPitchControl](mkpitchcontrol.md) — A specialized view that displays and controls the pitch angle of the map view.
- [MKUserTrackingButton](mkusertrackingbutton.md) — A specialized button that allows the user to toggle whether the map tracks to the heading the user is facing.
