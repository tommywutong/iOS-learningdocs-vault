---
title: UICollectionViewListCell
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlistcell
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlistcell'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlistcell.json'
content_hash: 'sha256:699caedfa8bdf218'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewListCell

<sub>Class</sub>

A collection view cell that provides list features and default styling.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UICollectionViewListCell
```

## Overview

A list cell represents an individual item that might appear in a list. List cells provide built-in support for indentation, and the ability to add cell accessories ([UICellAccessory](uicellaccessory-swift.struct.md)) for visual adornment or to support user interactions with the cell.

You can use a list cell in any type of layout. Using a list cell inside a list enables additional list-specific behavior for the cells. For example, in a list section or layout, you can define separator alignment between list cells, and configure swipe actions for each cell’s leading and trailing edges. You create an individual list section using [list(using:layoutEnvironment:)](<nscollectionlayoutsection/list(using_layoutenvironment_).md>), or a full list layout using [list(using:)](<uicollectionviewcompositionallayout/list(using_).md>).

You can use a list cell’s [defaultContentConfiguration()](<uicollectionviewlistcell/defaultcontentconfiguration().md>) (Swift)  or [defaultContentConfiguration](uicollectionviewlistcell/defaultcontentconfiguration.md) (Objective-C) to get a list content configuration that has preconfigured default styling. After you get the default configuration, you assign your content to it, customize any other properties, and assign it to the cell as the current content configuration. For customization options, see [UIListContentConfiguration](uilistcontentconfiguration-swift.struct.md).

**Swift**

```swift
var content = cell.defaultContentConfiguration()

// Configure content.
content.image = UIImage(systemName: "star")
content.text = "Favorites"

// Customize appearance.
content.imageProperties.tintColor = .purple

cell.contentConfiguration = content
```

**Objective-C**

```objc
UIListContentConfiguration *content = [cell defaultContentConfiguration];

// Configure content.
[content setImage:[UIImage systemImageNamed:@"star"]];
[content setText:@"Favorites"];

// Customize appearance.
[content.imageProperties setTintColor:[UIColor purpleColor]];

[cell setContentConfiguration:content];
```

Alternatively, you can set your content through your own custom subviews using the cell’s [contentView](uicollectionviewcell/contentview.md).

## Relationships

- **Inherits From**: [UICollectionViewCell](uicollectionviewcell.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Getting a configuration

- [defaultContentConfiguration()](<uicollectionviewlistcell/defaultcontentconfiguration().md>) — Retrieves a default list content configuration for the cell’s style.

### Managing cell accessories

- [accessories](uicollectionviewlistcell/accessories-8nui4.md) — An array of the accessories that decorate the cell.
- [UICellAccessory](uicellaccessory-swift.struct.md) — An accessory in a collection view list cell.

### Customizing layout

- [indentationLevel](uicollectionviewlistcell/indentationlevel.md) — The level of indentation for the cell.
- [indentationWidth](uicollectionviewlistcell/indentationwidth.md) — The width of an indentation level.
- [indentsAccessories](uicollectionviewlistcell/indentsaccessories.md) — A Boolean value that detemines whether the cell indents accessories on the leading side.
- [separatorLayoutGuide](uicollectionviewlistcell/separatorlayoutguide.md) — A guide for laying out separators in relation to the primary content in the cell.

## See Also

### Cells

- [UICollectionViewCell](uicollectionviewcell.md) — A single data item when that item is within the collection view’s visible bounds.
- [UICollectionReusableView](uicollectionreusableview.md) — A view that defines the behavior for all cells and supplementary views presented by a collection view.
