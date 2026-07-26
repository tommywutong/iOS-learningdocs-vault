---
title: MKPolygonView
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+（13.0 起废弃）, iPadOS 4.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkpolygonview
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolygonview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolygonview.json'
content_hash: 'sha256:ecf9d425b28501b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKPolygonView

<sub>Class</sub>

Provides the visual representation for an [MKPolygon](mkpolygon.md) annotation object.

> [!warning] Deprecated
> Use MKPolygonRenderer

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class MKPolygonView
```

## Overview

This view fills and strokes the area represented by the annotation. You can change the color and other drawing attributes of the polygon by modifying the properties inherited from the [MKOverlayPathView](mkoverlaypathview.md) class. This class is typically used as is and not subclassed.

In iOS 7 and later, use the [MKPolygonRenderer](mkpolygonrenderer.md) class to display polygon overlays instead.

## Relationships

- **Inherits From**: [MKOverlayPathView](mkoverlaypathview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearance](../uikit/uiappearance.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UICoordinateSpace](../uikit/uicoordinatespace.md), [UIDynamicItem](../uikit/uidynamicitem.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIFocusItem](../uikit/uifocusitem.md), [UIFocusItemContainer](../uikit/uifocusitemcontainer.md), [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

### Classes

- [MKCircleView](mkcircleview.md) — Provides the visual representation for an [MKCircle](mkcircle.md) annotation object. _(deprecated)_
- [MKOverlayView](mkoverlayview.md) — Defines the basic behavior associated with all overlay views. _(deprecated)_
- [MKOverlayPathView](mkoverlaypathview.md) — Represents a generic overlay that draws its contents using a Core Graphics path data type. _(deprecated)_
- [MKPolylineView](mkpolylineview.md) — Provides the visual representation for an [MKPolyline](mkpolyline.md) annotation object. _(deprecated)_
- [MKPinAnnotationView](mkpinannotationview.md) — An annotation view that displays a pin image on the map. _(deprecated)_
