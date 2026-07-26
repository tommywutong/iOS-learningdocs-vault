---
title: MKZoomControl
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 14.0+, macOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkzoomcontrol
source_url: 'https://developer.apple.com/documentation/mapkit/mkzoomcontrol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkzoomcontrol.json'
content_hash: 'sha256:bdc046aadb702e8f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKZoomControl

<sub>Class</sub>

A specialized view that displays and controls the zoom level of the map view.

<sub>Mac Catalyst, macOS</sub>

```swift
class MKZoomControl
```

## Overview

Use this class when you want to incorporate a standard, fixed-size zoom control into your own view hierarchy. A zoom control enables the user to change the zoom level of its associated map view.

## Relationships

- **Inherits From**: [NSView](../appkit/nsview.md), [UIView](../uikit/uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md), [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md), [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md), [NSAppearanceCustomization](../appkit/nsappearancecustomization.md), [NSCoding](../foundation/nscoding.md), [NSDraggingDestination](../appkit/nsdraggingdestination.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearance](../uikit/uiappearance.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UICoordinateSpace](../uikit/uicoordinatespace.md), [UIDynamicItem](../uikit/uidynamicitem.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIFocusItem](../uikit/uifocusitem.md), [UIFocusItemContainer](../uikit/uifocusitemcontainer.md), [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Creating a zoom control

- [+ zoomControlWithMapView:](<mkzoomcontrol/init(mapview_).md>) — Creates a zoom control and associates it with the specified map view.

### Accessing the map view

- [mapView](mkzoomcontrol/mapview.md) — The map view associated with this control.

## See Also

### Map customization

- [MKMapCamera](mkmapcamera.md) — A virtual camera for defining the appearance of the map.
- [MKCompassButton](mkcompassbutton.md) — A specialized view that displays the compass heading for its associated map.
- [MKScaleView](mkscaleview.md) — A specialized view that displays the scale information for its associated map.
- [MKPitchControl](mkpitchcontrol.md) — A specialized view that displays and controls the pitch angle of the map view.
- [MKUserTrackingButton](mkusertrackingbutton.md) — A specialized button that allows the user to toggle whether the map tracks to the heading the user is facing.
- [MKUserTrackingBarButtonItem](mkusertrackingbarbuttonitem.md) — A specialized bar button item that allows the user to toggle whether the map tracks to the heading the user is facing.
