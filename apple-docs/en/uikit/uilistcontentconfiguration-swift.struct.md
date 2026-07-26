---
title: UIListContentConfiguration
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct.json'
content_hash: 'sha256:331f9306133191f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIListContentConfiguration

<sub>Structure</sub>

A content configuration for a list-based content view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIListContentConfiguration
```

## Overview

A list content configuration describes the styling and content for an individual element that might appear in a list, like a cell, header, or footer. Using a list content configuration, you can obtain system default styling for a variety of different view states. You fill the configuration with your content, and then assign it directly to cells, headers, and footers in [UICollectionView](uicollectionview.md) and [UITableView](uitableview.md), or to your own custom list content view ([UIListContentView](uilistcontentview.md)).

For views like cells, headers, and footers, use their [defaultContentConfiguration()](<uicollectionviewlistcell/defaultcontentconfiguration().md>) to get a list content configuration that has preconfigured default styling. Alternatively, you can create a list content configuration from one of the system default styles. After you get the configuration, you assign your content to it, customize any other properties, and assign it to your view as the current content configuration.

```swift
var content = cell.defaultContentConfiguration()

// Configure content.
content.image = UIImage(systemName: "star")
content.text = "Favorites"

// Customize appearance.
content.imageProperties.tintColor = .purple

cell.contentConfiguration = content
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [UIContentConfiguration](uicontentconfiguration-9eib5.md)

## Topics

### Creating default cell configurations

- [cell()](<uilistcontentconfiguration-swift.struct/cell().md>) — Creates the default configuration you use to style a cell in a list.
- [subtitleCell()](<uilistcontentconfiguration-swift.struct/subtitlecell().md>) — Creates the default configuration you use to style a cell that’s in a list and contains subtitle text.
- [valueCell()](<uilistcontentconfiguration-swift.struct/valuecell().md>) — Creates the default configuration you use to style a cell that’s in a list and contains side-by-side value text.
- [sidebarCell()](<uilistcontentconfiguration-swift.struct/sidebarcell().md>) — Creates the default configuration you use to style a cell in a sidebar list.
- [sidebarSubtitleCell()](<uilistcontentconfiguration-swift.struct/sidebarsubtitlecell().md>) — Creates the default configuration you use to style a cell that’s in a sidebar list and contains subtitle text.
- [accompaniedSidebarCell()](<uilistcontentconfiguration-swift.struct/accompaniedsidebarcell().md>) — Creates the default configuration you use to style a cell in an accompanied sidebar list.
- [accompaniedSidebarSubtitleCell()](<uilistcontentconfiguration-swift.struct/accompaniedsidebarsubtitlecell().md>) — Creates the default configuration you use to style a cell that’s in an accompanied sidebar list and contains subtitle text.

### Creating header and footer configurations

- [plainHeader()](<uilistcontentconfiguration-swift.struct/plainheader().md>) — Creates the default configuration you use to style a header in a plain list.
- [plainFooter()](<uilistcontentconfiguration-swift.struct/plainfooter().md>) — Creates the default configuration you use to style a footer in a plain list.
- [groupedHeader()](<uilistcontentconfiguration-swift.struct/groupedheader().md>) — Creates the default configuration you use to style a header in a grouped list.
- [groupedFooter()](<uilistcontentconfiguration-swift.struct/groupedfooter().md>) — Creates the default configuration you use to style a footer in a grouped list.
- [prominentInsetGroupedHeader()](<uilistcontentconfiguration-swift.struct/prominentinsetgroupedheader().md>) — Creates the default configuration you use to style a prominent header in an inset grouped list.
- [extraProminentInsetGroupedHeader()](<uilistcontentconfiguration-swift.struct/extraprominentinsetgroupedheader().md>) — Creates the default configuration you use to style an extra prominent header in an inset grouped list.
- [sidebarHeader()](<uilistcontentconfiguration-swift.struct/sidebarheader().md>) — Creates the default configuration you use to style a header in a sidebar list.

### Customizing content

- [image](uilistcontentconfiguration-swift.struct/image.md) — The image to display.
- [text](uilistcontentconfiguration-swift.struct/text.md) — The primary text.
- [attributedText](uilistcontentconfiguration-swift.struct/attributedtext.md) — An attributed variant of the primary text.
- [secondaryText](uilistcontentconfiguration-swift.struct/secondarytext.md) — The secondary text.
- [secondaryAttributedText](uilistcontentconfiguration-swift.struct/secondaryattributedtext.md) — An attributed variant of the secondary text.

### Customizing appearance

- [imageProperties](uilistcontentconfiguration-swift.struct/imageproperties-swift.property.md) — Properties for configuring the image.
- [textProperties](uilistcontentconfiguration-swift.struct/textproperties-swift.property.md) — Properties for configuring the primary text.
- [secondaryTextProperties](uilistcontentconfiguration-swift.struct/secondarytextproperties.md) — Properties for configuring the secondary text.
- [ImageProperties](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct.md) — Properties that affect the list content configuration’s image.
- [TextProperties](uilistcontentconfiguration-swift.struct/textproperties-swift.struct.md) — Properties that affect the list content configuration’s text.

### Customizing layout

- [axesPreservingSuperviewLayoutMargins](uilistcontentconfiguration-swift.struct/axespreservingsuperviewlayoutmargins.md) — A Boolean value that determines whether the content view preserves the layout margins that it inherits from its superview on the horizontal or vertical axes.
- [directionalLayoutMargins](uilistcontentconfiguration-swift.struct/directionallayoutmargins.md) — The margins between the content and the edges of the content view.
- [prefersSideBySideTextAndSecondaryText](uilistcontentconfiguration-swift.struct/preferssidebysidetextandsecondarytext.md) — A Boolean value that determines whether the configuration positions the text and secondary text side by side.
- [imageToTextPadding](uilistcontentconfiguration-swift.struct/imagetotextpadding.md) — The padding between the image and text.
- [textToSecondaryTextHorizontalPadding](uilistcontentconfiguration-swift.struct/texttosecondarytexthorizontalpadding.md) — The minimum horizontal padding between the text and secondary text.
- [textToSecondaryTextVerticalPadding](uilistcontentconfiguration-swift.struct/texttosecondarytextverticalpadding.md) — The vertical padding between the text and secondary text.

### Instance Properties

- [alpha](uilistcontentconfiguration-swift.struct/alpha.md)

### Type Methods

- [footer()](<uilistcontentconfiguration-swift.struct/footer().md>)
- [header()](<uilistcontentconfiguration-swift.struct/header().md>)

## See Also

### Content configurations

- [UIListContentView](uilistcontentview.md) — A content view for displaying list-based content.
- [UIContentConfiguration](uicontentconfiguration-9eib5.md) — The requirements for an object that provides the configuration for a content view.
- [UIContentView](uicontentview-5fh3z.md) — The requirements for a content view that you create using a configuration.
