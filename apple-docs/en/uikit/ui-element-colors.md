---
title: UI element colors
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/ui-element-colors
source_url: 'https://developer.apple.com/documentation/uikit/ui-element-colors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/ui-element-colors.json'
content_hash: 'sha256:6ec99ceea221266e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Drawing](drawing.md) · [UIColor](uicolor.md)

# UI element colors

<sub>API Collection</sub>

Choose colors for UI elements such as labels, text, backgrounds, and links.

## Overview

UIKit provides color objects for the foreground and background colors of your app’s UI elements. The names of these color objects reflect their intended use, rather than specific color values.

Except where noted, the color objects adapt automatically to Dark Mode changes when you use the provided [UIColor](uicolor.md) object. If you retrieve the color values, either directly or using another type such as [CGColor](../coregraphics/cgcolor.md), you must handle Dark Mode changes yourself. For more information about supporting Dark Mode, see [Supporting Dark Mode in your interface](supporting-dark-mode-in-your-interface.md).

## Topics

### Label colors

- [labelColor](uicolor/label.md) — The color for text labels that contain primary content.
- [secondaryLabelColor](uicolor/secondarylabel.md) — The color for text labels that contain secondary content.
- [tertiaryLabelColor](uicolor/tertiarylabel.md) — The color for text labels that contain tertiary content.
- [quaternaryLabelColor](uicolor/quaternarylabel.md) — The color for text labels that contain quaternary content.

### Fill colors

- [systemFillColor](uicolor/systemfill.md) — An overlay fill color for thin and small shapes.
- [secondarySystemFillColor](uicolor/secondarysystemfill.md) — An overlay fill color for medium-size shapes.
- [tertiarySystemFillColor](uicolor/tertiarysystemfill.md) — An overlay fill color for large shapes.
- [quaternarySystemFillColor](uicolor/quaternarysystemfill.md) — An overlay fill color for large areas that contain complex content.

### Text colors

- [placeholderTextColor](uicolor/placeholdertext.md) — The color for placeholder text in controls or text views.

### Tint color

- [tintColor](uicolor/tintcolor.md) — A color value that resolves at runtime based on the current tint color of the app or trait hierarchy.

### Standard content background colors

- [systemBackgroundColor](uicolor/systembackground.md) — The color for the main background of your interface.
- [secondarySystemBackgroundColor](uicolor/secondarysystembackground.md) — The color for content layered on top of the main background.
- [tertiarySystemBackgroundColor](uicolor/tertiarysystembackground.md) — The color for content layered on top of secondary backgrounds.

### Grouped content background colors

- [systemGroupedBackgroundColor](uicolor/systemgroupedbackground.md) — The color for the main background of your grouped interface.
- [secondarySystemGroupedBackgroundColor](uicolor/secondarysystemgroupedbackground.md) — The color for content layered on top of the main background of your grouped interface.
- [tertiarySystemGroupedBackgroundColor](uicolor/tertiarysystemgroupedbackground.md) — The color for content layered on top of secondary backgrounds of your grouped interface.

### Separator colors

- [separatorColor](uicolor/separator.md) — The color for thin borders or divider lines that allows some underlying content to be visible.
- [opaqueSeparatorColor](uicolor/opaqueseparator.md) — The color for borders or divider lines that hides any underlying content.

### Link color

- [linkColor](uicolor/link.md) — The specified color for links.

### Nonadaptable colors

- [darkTextColor](uicolor/darktext.md) — The nonadaptable system color for text on a light background.
- [lightTextColor](uicolor/lighttext.md) — The nonadaptable system color for text on a dark background.

### Deprecated colors

- [groupTableViewBackgroundColor](uicolor/grouptableviewbackground.md) — The system color to use for the background of a grouped table. _(deprecated)_

## See Also

### Getting existing colors

- [Standard colors](standard-colors.md) — Define standard color objects for specific shades, such as red, blue, green, black, white, and more.
- [Color creation](color-creation.md) — Load colors from asset catalogs and create colors from raw component values.
