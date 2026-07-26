---
title: MKPinAnnotationView
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+（16.0 起废弃）, iPadOS 3.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.9+（13.0 起废弃）, tvOS 9.2+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkpinannotationview
source_url: 'https://developer.apple.com/documentation/mapkit/mkpinannotationview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpinannotationview.json'
content_hash: 'sha256:dd7cfbd73918701d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKPinAnnotationView

<sub>Class</sub>

An annotation view that displays a pin image on the map.

> [!warning] Deprecated
> In iOS 16 and macOS 13 and later use an [MKAnnotationView](mkannotationview.md) to create a custom map annotation

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKPinAnnotationView
```

## Overview

Return instances of this class from the [- mapView:viewForAnnotation:](<mkmapviewdelegate/mapview(__viewfor_)-8humz.md>) method of your map view delegate when you want to display a pin for one of your annotations. The pins displayed by this view are the same ones found in the Maps application. You can specify the type of pin you want to display and whether you want the pin to be animated into place.

> [!note] Note
> In iOS 5.1 and earlier, the MapKit framework uses the Google Mobile Maps (GMM) service to provide map data. Use of specific classes of this framework (and their associated interfaces) is subject to the Google Mobile Maps terms of service, found at [http://code.google.com/apis/maps/iphone/terms.html](http://code.google.com/apis/maps/iphone/terms.html).

## Relationships

- **Inherits From**: [MKAnnotationView](mkannotationview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md), [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md), [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md), [NSAppearanceCustomization](../appkit/nsappearancecustomization.md), [NSCoding](../foundation/nscoding.md), [NSDraggingDestination](../appkit/nsdraggingdestination.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearance](../uikit/uiappearance.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UICoordinateSpace](../uikit/uicoordinatespace.md), [UIDynamicItem](../uikit/uidynamicitem.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIFocusItem](../uikit/uifocusitem.md), [UIFocusItemContainer](../uikit/uifocusitemcontainer.md), [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Getting Standard Pin Colors

- [+ redPinColor](<mkpinannotationview/redpincolor().md>) — Returns the standard color for red pins. _(deprecated)_
- [+ greenPinColor](<mkpinannotationview/greenpincolor().md>) — Returns the standard color for green pins. _(deprecated)_
- [+ purplePinColor](<mkpinannotationview/purplepincolor().md>) — Returns the standard color for purple pins. _(deprecated)_
- [MKPinAnnotationColor](mkpinannotationcolor.md) — The supported colors for pin annotations. _(deprecated)_

### Getting and Setting Attributes

- [pinTintColor](mkpinannotationview/pintintcolor.md) — The color of the pin head. _(deprecated)_
- [animatesDrop](mkpinannotationview/animatesdrop.md) — A Boolean value indicating whether the annotation view is animated onto the screen. _(deprecated)_
- [pinColor](mkpinannotationview/pincolor.md) — The color of the pin head. _(deprecated)_

## See Also

### Classes

- [MKCircleView](mkcircleview.md) — Provides the visual representation for an [MKCircle](mkcircle.md) annotation object. _(deprecated)_
- [MKOverlayView](mkoverlayview.md) — Defines the basic behavior associated with all overlay views. _(deprecated)_
- [MKOverlayPathView](mkoverlaypathview.md) — Represents a generic overlay that draws its contents using a Core Graphics path data type. _(deprecated)_
- [MKPolygonView](mkpolygonview.md) — Provides the visual representation for an [MKPolygon](mkpolygon.md) annotation object. _(deprecated)_
- [MKPolylineView](mkpolylineview.md) — Provides the visual representation for an [MKPolyline](mkpolyline.md) annotation object. _(deprecated)_
