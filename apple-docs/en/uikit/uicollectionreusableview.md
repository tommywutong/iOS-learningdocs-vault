---
title: UICollectionReusableView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionreusableview
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionreusableview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionreusableview.json'
content_hash: 'sha256:0ce9ec7ebc60d816'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionReusableView

<sub>Class</sub>

A view that defines the behavior for all cells and supplementary views presented by a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UICollectionReusableView
```

## Overview

Reusable views are so named because the collection view places them on a reuse queue rather than deleting them when they’re scrolled out of the visible bounds. Such a view can then be retrieved and repurposed for a different set of content.

### Subclassing notes

This class is intended to be subclassed. Most methods defined by this class have minimal or no implementations. You aren’t required to override any of the methods but can do so in cases where you want to respond to changes in the view’s usage or layout.

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Inherited By**: [UICollectionViewCell](uicollectionviewcell.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Reusing cells

- [reuseIdentifier](uicollectionreusableview/reuseidentifier.md) — A string that identifies the purpose of the view.
- [- prepareForReuse](<uicollectionreusableview/prepareforreuse().md>) — Performs any clean up necessary to prepare the view for use again.

### Managing layout changes

- [- preferredLayoutAttributesFittingAttributes:](<uicollectionreusableview/preferredlayoutattributesfitting(__).md>) — Gives the cell a chance to modify the attributes provided by the layout object.
- [- applyLayoutAttributes:](<uicollectionreusableview/apply(__).md>) — Applies the specified layout attributes to the view.
- [- willTransitionFromLayout:toLayout:](<uicollectionreusableview/willtransition(from_to_).md>) — Tells your view that the layout object of the collection view is about to change.
- [- didTransitionFromLayout:toLayout:](<uicollectionreusableview/didtransition(from_to_).md>) — Tells your view that the layout object of the collection view changed.

## See Also

### Cells

- [UICollectionViewCell](uicollectionviewcell.md) — A single data item when that item is within the collection view’s visible bounds.
- [UICollectionViewListCell](uicollectionviewlistcell.md) — A collection view cell that provides list features and default styling.
