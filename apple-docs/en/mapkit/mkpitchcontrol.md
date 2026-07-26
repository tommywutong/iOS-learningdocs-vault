---
title: MKPitchControl
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 14.0+, macOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkpitchcontrol
source_url: 'https://developer.apple.com/documentation/mapkit/mkpitchcontrol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpitchcontrol.json'
content_hash: 'sha256:d18a4f0948fc00f2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKPitchControl

<sub>Class</sub>

A specialized view that displays and controls the pitch angle of the map view.

<sub>Mac Catalyst, macOS</sub>

```swift
class MKPitchControl
```

## Overview

Use this class when you want to incorporate a standard, fixed-size pitch control into your own view hierarchy. A pitch control allows the user to change the pitch angle of its associated map view.

## Relationships

- **Inherits From**: [NSView](../appkit/nsview.md), [UIView](../uikit/uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md), [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md), [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md), [NSAppearanceCustomization](../appkit/nsappearancecustomization.md), [NSCoding](../foundation/nscoding.md), [NSDraggingDestination](../appkit/nsdraggingdestination.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearance](../uikit/uiappearance.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UICoordinateSpace](../uikit/uicoordinatespace.md), [UIDynamicItem](../uikit/uidynamicitem.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIFocusItem](../uikit/uifocusitem.md), [UIFocusItemContainer](../uikit/uifocusitemcontainer.md), [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Creating a pitch control

- [+ pitchControlWithMapView:](<mkpitchcontrol/init(mapview_).md>) — Creates a pitch control and associates it with the specified map view.

### Accessing the map view

- [mapView](mkpitchcontrol/mapview.md) — The map view associated with this control.

## See Also

### Map customization

- [MKMapCamera](mkmapcamera.md) — A virtual camera for defining the appearance of the map.
- [MKCompassButton](mkcompassbutton.md) — A specialized view that displays the compass heading for its associated map.
- [MKScaleView](mkscaleview.md) — A specialized view that displays the scale information for its associated map.
- [MKZoomControl](mkzoomcontrol.md) — A specialized view that displays and controls the zoom level of the map view.
- [MKUserTrackingButton](mkusertrackingbutton.md) — A specialized button that allows the user to toggle whether the map tracks to the heading the user is facing.
- [MKUserTrackingBarButtonItem](mkusertrackingbarbuttonitem.md) — A specialized bar button item that allows the user to toggle whether the map tracks to the heading the user is facing.
