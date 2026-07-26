---
title: UIListContentConfiguration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-c.class
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-c.class.json'
content_hash: 'sha256:9f6c9b4af27651e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIListContentConfiguration

<sub>Class</sub>

A content configuration for a list-based content view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIListContentConfiguration : NSObject
```

## Overview

A list content configuration describes the styling and content for an individual element that might appear in a list, like a cell, header, or footer. Using a list content configuration, you can obtain system default styling for a variety of different view states. You fill the configuration with your content, and then assign it directly to cells, headers, and footers in [UICollectionView](uicollectionview.md) and [UITableView](uitableview.md), or to your own custom list content view ([UIListContentView](uilistcontentview.md)).

For views like cells, headers, and footers, use their [defaultContentConfiguration](uicollectionviewlistcell/defaultcontentconfiguration.md) to get a list content configuration that has preconfigured default styling. Alternatively, you can create a list content configuration from one of the system default styles. After you get the configuration, you assign your content to it, customize any other properties, and assign it to your view as the current content configuration.

```objc
UIListContentConfiguration *content = [cell defaultContentConfiguration];

// Configure content.
[content setImage:[UIImage systemImageNamed:@"star"]];
[content setText:@"Favorites"];

// Customize appearance.
[content.imageProperties setTintColor:[UIColor purpleColor]];

[cell setContentConfiguration:content];
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSSecureCoding](../foundation/nssecurecoding.md), [UIContentConfiguration](uicontentconfiguration-2raci.md)

## Topics

### Creating default cell configurations

- [cellConfiguration](uilistcontentconfiguration-c.class/cellconfiguration.md) — Creates the default configuration you use to style a cell in a list.
- [subtitleCellConfiguration](uilistcontentconfiguration-c.class/subtitlecellconfiguration.md) — Creates the default configuration you use to style a cell that’s in a list and contains subtitle text.
- [valueCellConfiguration](uilistcontentconfiguration-c.class/valuecellconfiguration.md) — Creates the default configuration you use to style a cell that’s in a list and contains side-by-side value text.
- [sidebarCellConfiguration](uilistcontentconfiguration-c.class/sidebarcellconfiguration.md) — Creates the default configuration you use to style a cell in a sidebar list. _(deprecated)_
- [sidebarSubtitleCellConfiguration](uilistcontentconfiguration-c.class/sidebarsubtitlecellconfiguration.md) — Creates the default configuration you use to style a cell that’s in a sidebar list and contains subtitle text. _(deprecated)_
- [accompaniedSidebarCellConfiguration](uilistcontentconfiguration-c.class/accompaniedsidebarcellconfiguration.md) — Creates the default configuration you use to style a cell in an accompanied sidebar list.
- [accompaniedSidebarSubtitleCellConfiguration](uilistcontentconfiguration-c.class/accompaniedsidebarsubtitlecellconfiguration.md) — Creates the default configuration you use to style a cell that’s in an accompanied sidebar list and contains subtitle text.

### Creating header and footer configurations

- [plainHeaderConfiguration](uilistcontentconfiguration-c.class/plainheaderconfiguration.md) — Creates the default configuration you use to style a header in a plain list. _(deprecated)_
- [plainFooterConfiguration](uilistcontentconfiguration-c.class/plainfooterconfiguration.md) — Creates the default configuration you use to style a footer in a plain list. _(deprecated)_
- [groupedHeaderConfiguration](uilistcontentconfiguration-c.class/groupedheaderconfiguration.md) — Creates the default configuration you use to style a header in a grouped list. _(deprecated)_
- [groupedFooterConfiguration](uilistcontentconfiguration-c.class/groupedfooterconfiguration.md) — Creates the default configuration you use to style a footer in a grouped list. _(deprecated)_
- [prominentInsetGroupedHeaderConfiguration](uilistcontentconfiguration-c.class/prominentinsetgroupedheaderconfiguration.md) — Creates the default configuration you use to style a prominent header in an inset grouped list.
- [extraProminentInsetGroupedHeaderConfiguration](uilistcontentconfiguration-c.class/extraprominentinsetgroupedheaderconfiguration.md) — Creates the default configuration you use to style an extra prominent header in an inset grouped list.
- [sidebarHeaderConfiguration](uilistcontentconfiguration-c.class/sidebarheaderconfiguration.md) — Creates the default configuration you use to style a header in a sidebar list. _(deprecated)_

### Customizing content

- [image](uilistcontentconfiguration-c.class/image.md) — The image to display.
- [text](uilistcontentconfiguration-c.class/text.md) — The primary text.
- [attributedText](uilistcontentconfiguration-c.class/attributedtext.md) — An attributed variant of the primary text.
- [secondaryText](uilistcontentconfiguration-c.class/secondarytext.md) — The secondary text.
- [secondaryAttributedText](uilistcontentconfiguration-c.class/secondaryattributedtext.md) — An attributed variant of the secondary text.

### Customizing appearance

- [imageProperties](uilistcontentconfiguration-c.class/imageproperties.md) — Properties for configuring the image.
- [textProperties](uilistcontentconfiguration-c.class/textproperties.md) — Properties for configuring the primary text.
- [secondaryTextProperties](uilistcontentconfiguration-c.class/secondarytextproperties.md) — Properties for configuring the secondary text.
- [UIListContentImageProperties](uilistcontentimageproperties.md) — Properties that affect the list content configuration’s image.
- [UIListContentTextProperties](uilistcontenttextproperties.md) — Properties that affect the list content configuration’s text.

### Customizing layout

- [axesPreservingSuperviewLayoutMargins](uilistcontentconfiguration-c.class/axespreservingsuperviewlayoutmargins.md) — A Boolean value that detemines whether the content view preserves the layout margins that it inherits from its superview on the horizontal or vertical axes.
- [directionalLayoutMargins](uilistcontentconfiguration-c.class/directionallayoutmargins.md) — The margins between the content and the edges of the content view.
- [prefersSideBySideTextAndSecondaryText](uilistcontentconfiguration-c.class/preferssidebysidetextandsecondarytext.md) — A Boolean value that determines whether the configuration positions the text and secondary text side by side.
- [imageToTextPadding](uilistcontentconfiguration-c.class/imagetotextpadding.md) — The padding between the image and text.
- [textToSecondaryTextHorizontalPadding](uilistcontentconfiguration-c.class/texttosecondarytexthorizontalpadding.md) — The minimum horizontal padding between the text and secondary text.
- [textToSecondaryTextVerticalPadding](uilistcontentconfiguration-c.class/texttosecondarytextverticalpadding.md) — The vertical padding between the text and secondary text.

### Instance Properties

- [alpha](uilistcontentconfiguration-c.class/alpha.md) — The alpha to apply to the entire content view. Defaults to 1.0.

### Type Methods

- [footerConfiguration](uilistcontentconfiguration-c.class/footerconfiguration.md) — Represents a generic footer configuration that automatically adopts the style of a containing list when updating for a new configuration state, by reading the `listEnvironment` trait from the state’s trait collection. Defaults to the footer configuration for a plain-style list.
- [headerConfiguration](uilistcontentconfiguration-c.class/headerconfiguration.md) — Represents a generic header configuration that automatically adopts the style of a containing list when updating for a new configuration state, by reading the `listEnvironment` trait from the state’s trait collection. Defaults to the header configuration for a plain-style list.

## See Also

### Content configurations

- [UIListContentView](uilistcontentview.md) — A content view for displaying list-based content.
- [UIContentConfiguration](uicontentconfiguration-2raci.md) — The requirements for an object that provides the configuration for a content view.
- [UIContentView](uicontentview-3zu2k.md) — The requirements for a content view that you create using a configuration.
