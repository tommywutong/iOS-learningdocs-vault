---
title: UIBackgroundExtensionView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibackgroundextensionview
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundextensionview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundextensionview.json'
content_hash: 'sha256:9a89bca3b4e7d37e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBackgroundExtensionView

<sub>Class</sub>

A view that extends content to fill its own bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UIBackgroundExtensionView
```

## Overview

A background extension view can be laid out to extend outside the safe area, such as under a sidebar or an inspector. By default, the view lays out its content to stay within the safe area, and uses modifications of the content along the edges to fill the container view.

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Instance Properties

- [automaticallyPlacesContentView](uibackgroundextensionview/automaticallyplacescontentview.md) — Controls the automatic safe area placement of the `contentView` within the container.
- [contentView](uibackgroundextensionview/contentview.md) — The content view to extend to fill the `UIBackgroundExtensionView`.

## See Also

### Interacting with adjacent views

- [UIScrollEdgeElementContainerInteraction](uiscrolledgeelementcontainerinteraction.md) — Add this interaction to a container view of views that overlay the edge of a scroll view. Any descendants of this view that should affect the shape of the edge effect, such as labels, images, glass views, and controls, will automatically do so.
