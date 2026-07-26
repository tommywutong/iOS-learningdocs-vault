---
title: MKMapViewDelegate
framework: MapKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapviewdelegate
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate.json'
content_hash: 'sha256:424bd9add32667b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapViewDelegate

<sub>Protocol</sub>

Optional methods that you use to receive map-related update messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor protocol MKMapViewDelegate : NSObjectProtocol
```

## Overview

Because many map operations require the [MKMapView](mkmapview.md) class to load data asynchronously, the map view calls these methods to notify your app when specific operations complete. The map view also uses these methods to request annotation and overlay views, and to manage interactions with those views.

Before releasing an [MKMapView](mkmapview.md) object that you set a delegate for, remember to set that object’s [delegate](mkmapview/delegate.md) property to `nil`. MapKit calls all of your delegate methods on the app’s main thread.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to map position changes

- [- mapView:regionWillChangeAnimated:](<mkmapviewdelegate/mapview(__regionwillchangeanimated_).md>) — Tells the delegate when the region the map view is displaying is about to change.
- [- mapViewDidChangeVisibleRegion:](<mkmapviewdelegate/mapviewdidchangevisibleregion(__).md>) — Tells the delegate when the map view’s visible region changes.
- [- mapView:regionDidChangeAnimated:](<mkmapviewdelegate/mapview(__regiondidchangeanimated_).md>) — Tells the delegate when the region the map view is displaying changes.

### Loading the map data

- [- mapViewWillStartLoadingMap:](<mkmapviewdelegate/mapviewwillstartloadingmap(__).md>) — Tells the delegate that the specified map view is about to retrieve some map data.
- [- mapViewDidFinishLoadingMap:](<mkmapviewdelegate/mapviewdidfinishloadingmap(__).md>) — Tells the delegate when the specified map view successfully loads the needed map data.
- [- mapViewDidFailLoadingMap:withError:](<mkmapviewdelegate/mapviewdidfailloadingmap(__witherror_).md>) — Tells the delegate that the specified view is unable to load the map data.
- [- mapViewWillStartRenderingMap:](<mkmapviewdelegate/mapviewwillstartrenderingmap(__).md>) — Tells the delegate that the map view is about to start rendering some of its tiles.
- [- mapViewDidFinishRenderingMap:fullyRendered:](<mkmapviewdelegate/mapviewdidfinishrenderingmap(__fullyrendered_).md>) — Tells the delegate when the map view finishes rendering all visible tiles.

### Tracking the user’s location

- [- mapViewWillStartLocatingUser:](<mkmapviewdelegate/mapviewwillstartlocatinguser(__).md>) — Tells the delegate that the map view is about to start tracking the user’s location.
- [- mapViewDidStopLocatingUser:](<mkmapviewdelegate/mapviewdidstoplocatinguser(__).md>) — Tells the delegate when the map view stops tracking the user’s location.
- [- mapView:didUpdateUserLocation:](<mkmapviewdelegate/mapview(__didupdate_).md>) — Tells the delegate when the map view updates the user’s location.
- [- mapView:didFailToLocateUserWithError:](<mkmapviewdelegate/mapview(__didfailtolocateuserwitherror_).md>) — Tells the delegate when an attempt to locate the user’s location fails.
- [- mapView:didChangeUserTrackingMode:animated:](<mkmapviewdelegate/mapview(__didchange_animated_).md>) — Tells the delegate when the user-tracking mode changes.

### Managing annotation views

- [- mapView:viewForAnnotation:](<mkmapviewdelegate/mapview(__viewfor_)-8humz.md>) — Returns the view associated with the specified annotation object.
- [- mapView:didAddAnnotationViews:](<mkmapviewdelegate/mapview(__didadd_)-44xon.md>) — Tells the delegate when the map view adds one or more annotation views to the map.
- [- mapView:annotationView:calloutAccessoryControlTapped:](<mkmapviewdelegate/mapview(__annotationview_calloutaccessorycontroltapped_).md>) — Tells the delegate when the user taps one of the annotation view’s accessory buttons.
- [- mapView:clusterAnnotationForMemberAnnotations:](<mkmapviewdelegate/mapview(__clusterannotationformemberannotations_).md>) — Asks the delegate to provide a cluster annotation object for the specified annotations.

### Dragging an annotation view

- [- mapView:annotationView:didChangeDragState:fromOldState:](<mkmapviewdelegate/mapview(__annotationview_didchange_fromoldstate_).md>) — Tells the delegate when the drag state of one of its annotation views changes.

### Selecting annotations and annotations views

- [- mapView:didSelectAnnotationView:](<mkmapviewdelegate/mapview(__didselect_)-41by3.md>) — Tells the delegate when the user selects one or more of its annotation views.
- [- mapView:didDeselectAnnotationView:](<mkmapviewdelegate/mapview(__diddeselect_)-yo7q.md>) — Tells the delegate when the user deselects one or more of its annotation views.
- [- mapView:didDeselectAnnotation:](<mkmapviewdelegate/mapview(__diddeselect_)-4ldss.md>) — Tells the delegate when the user deselects one or more annotations.
- [- mapView:didSelectAnnotation:](<mkmapviewdelegate/mapview(__didselect_)-9km43.md>) — Tells the delegate when the user selects one or more annotations.
- [selectableMapFeatures](mkmapview/selectablemapfeatures.md) — The property that describes which selectable features the map responds to.

### Managing the display of overlays

- [- mapView:selectionAccessoryForAnnotation:](<mkmapviewdelegate/mapview(__selectionaccessoryfor_).md>) — Specifies the accessory to display for a selected annotation
- [- mapView:rendererForOverlay:](<mkmapviewdelegate/mapview(__rendererfor_).md>) — Asks the delegate for a renderer object to use when drawing the specified overlay.
- [- mapView:didAddOverlayRenderers:](<mkmapviewdelegate/mapview(__didadd_)-793gj.md>) — Tells the delegate when the map view adds one or more renderer objects to the map.
- [- mapView:viewForOverlay:](<mkmapviewdelegate/mapview(__viewfor_)-6j267.md>) — Asks the delegate for the overlay view to use when displaying the specified overlay object. _(deprecated)_
- [- mapView:didAddOverlayViews:](<mkmapviewdelegate/mapview(__didaddoverlayviews_).md>) — Tells the delegate when the map adds one or more overlay views to the map. _(deprecated)_

## See Also

### Customizing the map view behavior

- [delegate](mkmapview/delegate.md) — The receiver’s delegate.
