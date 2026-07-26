---
title: MKCompassButton
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkcompassbutton
source_url: 'https://developer.apple.com/documentation/mapkit/mkcompassbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcompassbutton.json'
content_hash: 'sha256:9d68c1bf9bebeeff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKCompassButton

<sub>Class</sub>

A specialized view that displays the compass heading for its associated map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class MKCompassButton
```

## Overview

Use this class when you want to incorporate a standard compass button into your own view hierarchy. A compass button reflects the current orientation of its associated map view. Tapping the compass button reorients the map so that due north is at the top of the map view.

## Relationships

- **Inherits From**: [NSView](../appkit/nsview.md), [UIView](../uikit/uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md), [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md), [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md), [NSAppearanceCustomization](../appkit/nsappearancecustomization.md), [NSCoding](../foundation/nscoding.md), [NSDraggingDestination](../appkit/nsdraggingdestination.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearance](../uikit/uiappearance.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UICoordinateSpace](../uikit/uicoordinatespace.md), [UIDynamicItem](../uikit/uidynamicitem.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIFocusItem](../uikit/uifocusitem.md), [UIFocusItemContainer](../uikit/uifocusitemcontainer.md), [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Creating a compass button

- [+ compassButtonWithMapView:](<mkcompassbutton/init(mapview_).md>) — Creates a compass button and associates it with the specified map view.

### Getting the compass attributes

- [mapView](mkcompassbutton/mapview.md) — The map view that provides the heading information for the compass button.
- [compassVisibility](mkcompassbutton/compassvisibility.md) — The visibility of the compass button.
- [MKFeatureVisibility](mkfeaturevisibility.md) — Constants that indicate the visibility of different map features.

## See Also

### Map customization

- [MKMapCamera](mkmapcamera.md) — A virtual camera for defining the appearance of the map.
- [MKScaleView](mkscaleview.md) — A specialized view that displays the scale information for its associated map.
- [MKZoomControl](mkzoomcontrol.md) — A specialized view that displays and controls the zoom level of the map view.
- [MKPitchControl](mkpitchcontrol.md) — A specialized view that displays and controls the pitch angle of the map view.
- [MKUserTrackingButton](mkusertrackingbutton.md) — A specialized button that allows the user to toggle whether the map tracks to the heading the user is facing.
- [MKUserTrackingBarButtonItem](mkusertrackingbarbuttonitem.md) — A specialized bar button item that allows the user to toggle whether the map tracks to the heading the user is facing.
