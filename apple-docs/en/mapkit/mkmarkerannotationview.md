---
title: MKMarkerAnnotationView
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmarkerannotationview
source_url: 'https://developer.apple.com/documentation/mapkit/mkmarkerannotationview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmarkerannotationview.json'
content_hash: 'sha256:2d793c6ff0a3d06d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMarkerAnnotationView

<sub>Class</sub>

An annotation view that displays a balloon-shaped marker at the designated location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKMarkerAnnotationView
```

## Overview

Return an instance of this class from the [- mapView:viewForAnnotation:](<mkmapviewdelegate/mapview(__viewfor_)-8humz.md>) method of your map view delegate when you want to display the same types of markers used in the Maps app.

The default [displayPriority](mkannotationview/displaypriority.md) for an instance of this class is [MKFeatureDisplayPriorityDefaultLow](mkfeaturedisplaypriority/defaultlow.md).

## Relationships

- **Inherits From**: [MKAnnotationView](mkannotationview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md), [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md), [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md), [NSAppearanceCustomization](../appkit/nsappearancecustomization.md), [NSCoding](../foundation/nscoding.md), [NSDraggingDestination](../appkit/nsdraggingdestination.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearance](../uikit/uiappearance.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UICoordinateSpace](../uikit/uicoordinatespace.md), [UIDynamicItem](../uikit/uidynamicitem.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIFocusItem](../uikit/uifocusitem.md), [UIFocusItemContainer](../uikit/uifocusitemcontainer.md), [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Setting the Marker Color

- [markerTintColor](mkmarkerannotationview/markertintcolor.md) — The background color of the marker balloon.

### Setting the Marker Content

- [glyphText](mkmarkerannotationview/glyphtext.md) — The text to display in the marker balloon.
- [glyphImage](mkmarkerannotationview/glyphimage.md) — An image to display in the marker balloon.
- [glyphTintColor](mkmarkerannotationview/glyphtintcolor.md) — The color to apply to the glyph text or image.
- [selectedGlyphImage](mkmarkerannotationview/selectedglyphimage.md) — An image to display when the user selects the marker.

### Setting the Visibility

- [titleVisibility](mkmarkerannotationview/titlevisibility.md) — The visibility of the title text rendered beneath the marker balloon.
- [subtitleVisibility](mkmarkerannotationview/subtitlevisibility.md) — The visibility of the subtitle text rendered beneath the marker balloon.
- [MKFeatureVisibility](mkfeaturevisibility.md) — Constants that indicate the visibility of different map features.

### Animating the Marker onto the Screen

- [animatesWhenAdded](mkmarkerannotationview/animateswhenadded.md) — A Boolean that indicates whether the marker animates into position onscreen.

## See Also

### Location annotations

- [Annotating a Map with Custom Data](annotating-a-map-with-custom-data.md) — Annotate a map with location-specific data using default and customized annotation views and callouts.
- [MKPointAnnotation](mkpointannotation.md) — A string-based piece of location-specific data that you apply to a specific point on a map.
- [MKMapItemAnnotation](mkmapitemannotation.md) — An annotation that represents a map item
- [MKPinAnnotationView](mkpinannotationview.md) — An annotation view that displays a pin image on the map. _(deprecated)_
