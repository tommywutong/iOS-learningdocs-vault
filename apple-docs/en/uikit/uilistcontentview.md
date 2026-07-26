---
title: UIListContentView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentview
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentview.json'
content_hash: 'sha256:084e65b3bc3dceda'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIListContentView

<sub>Class</sub>

A content view for displaying list-based content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIListContentView
```

## Overview

You use a list content view for displaying list-based content in a custom view hierarchy. You can embed a list content view manually in a custom cell or in a container view, like a [UIStackView](uistackview.md). You can use Auto Layout or manual layout techniques to size and position the view, and its height adjusts dynamically according to its width and the space it needs to display its content.

A list content view relies on its list content configuration to supply its styling and content. You create a list content view by passing in a [UIListContentConfiguration](uilistcontentconfiguration-swift.struct.md) to [init(configuration:)](<uilistcontentview/init(configuration_).md>) (Swift) or [initWithConfiguration:](uilistcontentview/initwithconfiguration_.md) (Objective-C). To update the content view, you set a new configuration on it through its [configuration](uilistcontentview/configuration.md) property.

If you’re using a [UICollectionView](uicollectionview.md) or [UITableView](uitableview.md), you don’t need to manually create a list content view to take advantage of the list configuration. Instead, you assign a [UIListContentConfiguration](uilistcontentconfiguration-swift.struct.md) to the [contentConfiguration](uicollectionviewcell/contentconfiguration-1lcqh.md) property of the cells, headers, or footers within those types.

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContentView](uicontentview-5fh3z.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating a list content view

- [init(configuration:)](<uilistcontentview/init(configuration_).md>) — Creates a list content view with the specified content configuration.
- [- initWithCoder:](<uilistcontentview/init(coder_).md>) — Creates a list content view from data in an unarchiver.

### Managing the content layout

- [textLayoutGuide](uilistcontentview/textlayoutguide.md) — A guide for positioning the primary text in the content view.
- [secondaryTextLayoutGuide](uilistcontentview/secondarytextlayoutguide.md) — A guide for positioning the secondary text in the content view.
- [imageLayoutGuide](uilistcontentview/imagelayoutguide.md) — A guide for positioning the image in the content view.

## See Also

### Content configurations

- [UIListContentConfiguration](uilistcontentconfiguration-swift.struct.md) — A content configuration for a list-based content view.
- [UIContentConfiguration](uicontentconfiguration-9eib5.md) — The requirements for an object that provides the configuration for a content view.
- [UIContentView](uicontentview-5fh3z.md) — The requirements for a content view that you create using a configuration.
