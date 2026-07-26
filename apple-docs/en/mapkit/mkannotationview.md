---
title: MKAnnotationView
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview.json'
content_hash: 'sha256:d876e04d0c5f0131'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKAnnotationView

<sub>Class</sub>

The visual representation of one of your annotation objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKAnnotationView
```

## Overview

_Annotation views_ are loosely coupled to a corresponding _annotation object_, which is an object that conforms to the [MKAnnotation](mkannotation.md) protocol. When an annotation’s coordinate point is in the map’s visible region, the map view asks its delegate to provide a corresponding annotation view. MapKit may recycle annotation views and put them into a reuse queue that the map view maintains.

The most efficient way to provide the content for an annotation view is to set its [image](mkannotationview/image.md) property. The annotation view sizes itself automatically to the image you specify and draws that image for its contents. Because it’s a view, you can also override the [draw(_:)](<../uikit/uiview/draw(__).md>) method and draw your view’s content manually. If you choose to override [draw(_:)](<../uikit/uiview/draw(__).md>) directly and you don’t specify a custom image in the [image](mkannotationview/image.md) property, the annotation view sets the width and height of the annotation view’s frame to `0` by default. Before the framework can draw your custom content, you need to set the width and height to nonzero values by modifying the view’s [frame](../uikit/uiview/frame.md) property. In general, if your content consists entirely of static images, it’s more efficient to set the [image](mkannotationview/image.md) property and change it as necessary than to draw the images yourself.

Annotation views anchor to the map at the point that their associated annotation object specifies. Although they scroll with the map contents, annotation views reside in a separate display layer and don’t scale when the size of the visible map region changes.

Additionally, annotation views support the concept of a _selection state_, which determines whether the map displays the annotation view as unselected, selected, or selected and displaying a standard callout view. The user toggles between the selection states through interactions with the annotation view. In the unselected state, the map displays the annotation view, but doesn’t highlight it. In the selected state, the framework highlights the annotation, but doesn’t display the callout. Finally, the map view can display the annotation with both a highlight and a callout. The callout view displays additional information, such as a title string and controls for viewing more information. The annotation object provides the title information, but your annotation view is responsible for providing any custom controls. For more information, see the [Subclassing notes](mkannotationview.md#Subclassing-notes) section below.

### Reuse annotation views

The design of annotation views enables their reuse as the user (or your app) changes the visible map region. The reuse of annotation views provides significant performance improvements during scrolling by avoiding the creation of new view objects during this time-critical operation. For this reason, don’t tightly couple annotation views to the contents of their associated annotation. Instead, use the properties of an annotation view (or setter methods) to configure the view for a new annotation object.

Whenever you initialize a new annotation view, specify a reuse identifier for that view. When the framework no longer needs annotation views, the map view may put them into a reuse queue. As the framework adds new annotations to the map view, the delegate object can then dequeue and reconfigure an existing view (rather than create a new one) using the [- dequeueReusableAnnotationViewWithIdentifier:](<mkmapview/dequeuereusableannotationview(withidentifier_).md>) method of [MKMapView](mkmapview.md).

### Subclassing notes

You can use the `MKAnnotationView` class as-is or subclass it to provide custom behavior as necessary. The [image](mkannotationview/image.md) property of the class lets you set the appearance of the annotation view without subclassing directly. You might also create custom subclasses as a convenience and use them to put the annotation view in a known state.

There are no special requirements for subclassing `MKAnnotationView`. However, the following list includes some reasons you might want to subclass, and the methods to override to implement the desired behavior:

- To put the annotation view into a consistent state, provide a custom initialization method. Your custom initialization method then calls [- initWithAnnotation:reuseIdentifier:](<mkannotationview/init(annotation_reuseidentifier_).md>) to initialize the superclass.
- To provide custom callout views, override the [leftCalloutAccessoryView](mkannotationview/leftcalloutaccessoryview.md) method and use it to return the views.

If you support draggable annotation views in iOS, your subclass is responsible for changing the value in the [dragState](mkannotationview/dragstate-swift.property.md) property to appropriate values at key transition points in the drag operation. For more information, see the description of that property.

## Relationships

- **Inherits From**: [NSView](../appkit/nsview.md), [UIView](../uikit/uiview.md)

- **Inherited By**: [MKMarkerAnnotationView](mkmarkerannotationview.md), [MKPinAnnotationView](mkpinannotationview.md), [MKUserLocationView](mkuserlocationview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md), [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md), [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md), [NSAppearanceCustomization](../appkit/nsappearancecustomization.md), [NSCoding](../foundation/nscoding.md), [NSDraggingDestination](../appkit/nsdraggingdestination.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearance](../uikit/uiappearance.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UICoordinateSpace](../uikit/uicoordinatespace.md), [UIDynamicItem](../uikit/uidynamicitem.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIFocusItem](../uikit/uifocusitem.md), [UIFocusItemContainer](../uikit/uifocusitemcontainer.md), [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Creating and preparing an annotation view

- [- initWithAnnotation:reuseIdentifier:](<mkannotationview/init(annotation_reuseidentifier_).md>) — Creates and returns a new annotation view.
- [- initWithCoder:](<mkannotationview/init(coder_).md>) — Creates an annotation view using data from the specified unarchiver.
- [- prepareForReuse](<mkannotationview/prepareforreuse().md>) — Calls this method when removing the view from the reuse queue.
- [- prepareForDisplay](<mkannotationview/preparefordisplay().md>) — Notifies the annotation view that the map view is about to display it.

### Setting the priority for display

- [displayPriority](mkannotationview/displaypriority.md) — The display priority of the annotation view.
- [MKFeatureDisplayPriority](mkfeaturedisplaypriority.md) — Constants that indicates the display priority for annotations.
- [zPriority](mkannotationview/zpriority.md) — The relative importance of the annotation view when in an unselected state with respect to its ordering along the z-axis.
- [selectedZPriority](mkannotationview/selectedzpriority.md) — The relative importance of the annotation view when in a selected state with respect to its ordering along the z-axis.
- [MKAnnotationViewZPriority](mkannotationviewzpriority.md) — Constants that indicates the priority for ordering overlapping annotation views.

### Getting and setting attributes

- [enabled](mkannotationview/isenabled.md) — A Boolean value that indicates whether the annotation is in an enabled state.
- [image](mkannotationview/image.md) — The image the annotation view displays.
- [highlighted](mkannotationview/ishighlighted.md) — A Boolean value that indicates whether the map view highlights the annotation view.
- [annotation](mkannotationview/annotation.md) — The annotation object associated with the view.
- [centerOffset](mkannotationview/centeroffset.md) — The offset (in points) at which to display the view.
- [calloutOffset](mkannotationview/calloutoffset.md) — The offset (in points) at which to place the callout.
- [reuseIdentifier](mkannotationview/reuseidentifier.md) — The string that identifies that the annotation view is reusable.

### Managing the selection state

- [- setSelected:animated:](<mkannotationview/setselected(__animated_).md>) — Sets the selection state of the annotation view.
- [selected](mkannotationview/isselected.md) — A Boolean value that indicates whether the annotation view is in a selected state.

### Managing callout views

- [accessoryOffset](mkannotationview/accessoryoffset.md) — An offset that changes the accessory’s default anchor point.
- [canShowCallout](mkannotationview/canshowcallout.md) — A Boolean value that indicates whether the annotation view is able to display extra information in a callout.
- [leftCalloutAccessoryView](mkannotationview/leftcalloutaccessoryview.md) — The view to display on the left side of the standard callout.
- [rightCalloutAccessoryView](mkannotationview/rightcalloutaccessoryview.md) — The view to display on the right side of the standard callout.
- [detailCalloutAccessoryView](mkannotationview/detailcalloutaccessoryview.md) — The detail accessory view to use in the standard callout.
- [leftCalloutOffset](mkannotationview/leftcalloutoffset.md) — The offset in points from the middle-left of the annotation view.
- [rightCalloutOffset](mkannotationview/rightcalloutoffset.md) — The offset in points from the middle-right of the annotation view.

### Supporting drag operations

- [draggable](mkannotationview/isdraggable.md) — A Boolean value that indicates whether the annotation view is draggable.
- [- setDragState:animated:](<mkannotationview/setdragstate(__animated_).md>) — Sets the drag state for the annotation view.
- [dragState](mkannotationview/dragstate-swift.property.md) — The drag state of the annotation view.

### Managing collisions between annotation views

- [collisionMode](mkannotationview/collisionmode-swift.property.md) — The collision mode to use when interpreting the collision frame rectangle.
- [CollisionMode](mkannotationview/collisionmode-swift.enum.md) — Constants that indicates how to interpret the collision frame rectangle of an annotation view.

### Clustering annotation views

- [Decluttering a Map with MapKit Annotation Clustering](decluttering-a-map-with-mapkit-annotation-clustering.md) — Enhance the readability of a map by replacing overlapping annotations with a clustering annotation view.
- [clusteringIdentifier](mkannotationview/clusteringidentifier.md) — An identifier that determines whether the annotation view participates in clustering.
- [clusterAnnotationView](mkannotationview/cluster.md) — The clustering annotation view that replaces the annotation view.

### Constants

- [DragState](mkannotationview/dragstate-swift.enum.md) — Constants that indicate the drag state of an annotation view.

## See Also

### Shared behavior

- [MKPlacemark](mkplacemark.md) — A user-friendly description of a location on the map. _(deprecated)_
- [MKAnnotation](mkannotation.md) — An interface for associating your content with a specific map location.
