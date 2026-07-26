---
title: Standard colors
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/standard-colors
source_url: 'https://developer.apple.com/documentation/uikit/standard-colors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/standard-colors.json'
content_hash: 'sha256:e5a33fabcca54f06'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Drawing](drawing.md) · [UIColor](uicolor.md)

# Standard colors

<sub>API Collection</sub>

Define standard color objects for specific shades, such as red, blue, green, black, white, and more.

## Overview

Use the standard color objects when you want to use a specific color shade in your UI. To view swatches of these colors, see [System Colors](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/color/#system-colors).

The system color objects adapt automatically to Dark Mode changes when you use the provided [UIColor](uicolor.md) object, but the fixed-shade colors don’t adapt. If you retrieve the color values, either directly or using another type such as [CGColor](../coregraphics/cgcolor.md), you must handle Dark Mode changes yourself. For more information about supporting Dark Mode, see [Supporting Dark Mode in your interface](supporting-dark-mode-in-your-interface.md).

## Topics

### Adaptable colors

- [systemBlueColor](uicolor/systemblue.md) — A blue color that automatically adapts to the current trait environment.
- [systemBrownColor](uicolor/systembrown.md) — A brown color that automatically adapts to the current trait environment.
- [systemCyanColor](uicolor/systemcyan.md) — A cyan color that automatically adapts to the current trait environment.
- [systemGreenColor](uicolor/systemgreen.md) — A green color that automatically adapts to the current trait environment.
- [systemIndigoColor](uicolor/systemindigo.md) — An indigo color that automatically adapts to the current trait environment.
- [systemMintColor](uicolor/systemmint.md) — A mint color that automatically adapts to the current trait environment.
- [systemOrangeColor](uicolor/systemorange.md) — An orange color that automatically adapts to the current trait environment.
- [systemPinkColor](uicolor/systempink.md) — A pink color that automatically adapts to the current trait environment.
- [systemPurpleColor](uicolor/systempurple.md) — A purple color that automatically adapts to the current trait environment.
- [systemRedColor](uicolor/systemred.md) — A red color that automatically adapts to the current trait environment.
- [systemTealColor](uicolor/systemteal.md) — A teal color that automatically adapts to the current trait environment.
- [systemYellowColor](uicolor/systemyellow.md) — A yellow color that automatically adapts to the current trait environment.

### Adaptable gray colors

- [systemGrayColor](uicolor/systemgray.md) — The standard base gray color that adapts to the environment.
- [systemGray2Color](uicolor/systemgray2.md) — A second-level shade of gray that adapts to the environment.
- [systemGray3Color](uicolor/systemgray3.md) — A third-level shade of gray that adapts to the environment.
- [systemGray4Color](uicolor/systemgray4.md) — A fourth-level shade of gray that adapts to the environment.
- [systemGray5Color](uicolor/systemgray5.md) — A fifth-level shade of gray that adapts to the environment.
- [systemGray6Color](uicolor/systemgray6.md) — A sixth-level shade of gray that adapts to the environment.

### Transparent color

- [clearColor](uicolor/clear.md) — A color object with grayscale and alpha values that are both `0.0`.

### Fixed colors

- [blackColor](uicolor/black.md) — A color object in the sRGB color space with a grayscale value of `0.0` and an alpha value of `1.0`.
- [blueColor](uicolor/blue.md) — A color object with RGB values of `0.0`, `0.0`, and `1.0`, and an alpha value of `1.0`.
- [brownColor](uicolor/brown.md) — A color object with RGB values of `0.6`, `0.4`, and `0.2`, and an alpha value of `1.0`.
- [cyanColor](uicolor/cyan.md) — A color object with RGB values of `0.0`, `1.0`, and `1.0`, and an alpha value of `1.0`.
- [darkGrayColor](uicolor/darkgray.md) — A color object with a grayscale value of 1/3 and an alpha value of `1.0`.
- [grayColor](uicolor/gray.md) — A color object with a grayscale value of `0.5` and an alpha value of `1.0`.
- [greenColor](uicolor/green.md) — A color object with RGB values of `0.0`, `1.0`, and `0.0`, and an alpha value of `1.0`.
- [lightGrayColor](uicolor/lightgray.md) — A color object with a grayscale value of 2/3 and an alpha value of `1.0`.
- [magentaColor](uicolor/magenta.md) — A color object with RGB values of `1.0`, `0.0`, and `1.0`, and an alpha value of `1.0`.
- [orangeColor](uicolor/orange.md) — A color object with RGB values of `1.0`, `0.5`, and `0.0`, and an alpha value of `1.0`.
- [purpleColor](uicolor/purple.md) — A color object with RGB values of `0.5`, `0.0`, and `0.5`, and an alpha value of `1.0`.
- [redColor](uicolor/red.md) — A color object with RGB values of `1.0`, `0.0`, and `0.0`, and an alpha value of `1.0`.
- [whiteColor](uicolor/white.md) — A color object with a grayscale value of `1.0` and an alpha value of `1.0`.
- [yellowColor](uicolor/yellow.md) — A color object with RGB values of `1.0`, `1.0`, and `0.0`, and an alpha value of `1.0`.

## See Also

### Getting existing colors

- [UI element colors](ui-element-colors.md) — Choose colors for UI elements such as labels, text, backgrounds, and links.
- [Color creation](color-creation.md) — Load colors from asset catalogs and create colors from raw component values.
