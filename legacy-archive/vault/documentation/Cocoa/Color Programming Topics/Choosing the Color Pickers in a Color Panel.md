---
title: Color Programming Topics
apple_id: 10000082i
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/Tasks/ChoosingColorPickers.html
archived_at: '2026-07-15T07:15:15.071948Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Color Programming Topics](Introduction%20to%20Color%20Programming%20Topics%20for%20Cocoa.md)


[Next](Adding%20Custom%20Color%20Pickers%20to%20a%20Color%20Panel.md)[Previous](Choosing%20Colors%20With%20Color%20Wells%20and%20Color%20Panels.md)

# Choosing the Color Pickers in a Color Panel

The color mask determines which of the color modes are enabled for an [NSColorPanel](https://developer.apple.com/documentation/appkit/nscolorpanel) object. This mask is set before you initialize a new instance of `NSColorPanel`. `NSColorPanelAllModesMask` represents the logical OR of the other color mask constants: It causes the `NSColorPanel` object to display all standard color pickers. When initializing a new instance of `NSColorPanel`, you can logically OR any combination of color mask constants to restrict the available color modes.

| Mode | Color Mask Constant |
| --- | --- |
| Grayscale-Alpha | `NSColorPanelGrayModeMask` |
| Red-Green-Blue | `NSColorPanelRGBModeMask` |
| Cyan-Yellow-Magenta-Black | `NSColorPanelCMYKModeMask` |
| Hue-Saturation-Brightness | `NSColorPanelHSBModeMask` |
| Custom palette | `NSColorPanelCustomPaletteModeMask` |
| Custom color list | `NSColorPanelColorListModeMask` |
| Color wheel | `NSColorPanelWheelModeMask` |
| All of the above | `NSColorPanelAllModesMask` |

The a color panel’s color mode mask is set using the class method [setPickerMask:](https://developer.apple.com/documentation/appkit/nscolorpanel/1534004-setpickermask). The mask must be set before creating an application’s instance of `NSColorPanel`.

When an application’s instance of `NSColorPanel` is masked for more than one color mode, your program can set its active mode by invoking the [setMode:](https://developer.apple.com/documentation/appkit/nscolorpanel/1525410-mode) method with a color mode constant as its argument; the user can set the mode by clicking buttons on the panel. Here are the standard color modes and mode constants:

| Mode | Color Mode Constant |
| --- | --- |
| Grayscale-Alpha | `NSGrayModeColorPanel` |
| Red-Green-Blue | `NSRGBModeColorPanel` |
| Cyan-Yellow-Magenta-Black | `NSCMYKModeColorPanel` |
| Hue-Saturation-Brightness | `NSHSBModeColorPanel` |
| Custom palette | `NSCustomPaletteModeColorPanel` |
| Custom color list | `NSColorListModeColorPanel` |
| Color wheel | `NSWheelModeColorPanel` |

In grayscale-alpha, red-green-blue, cyan-magenta-yellow-black, and hue-saturation-brightness modes, the user adjusts colors by manipulating sliders. In the custom palette mode, the user can load an NSImage file (TIFF or EPS) into the color panel, then select colors from the image. In custom color list mode, the user can create and load lists of named colors. The two custom modes provide pop-up buttons for loading and saving files. Finally, color wheel mode provides a simplified control for selecting colors.

If a color panel has been used, it uses whatever mode it was in last as the default mode when `NSColorPanelAllModesMask` is used to initialize the `NSColorPanel`. Otherwise, it uses color wheel mode.

[Next](Adding%20Custom%20Color%20Pickers%20to%20a%20Color%20Panel.md)[Previous](Choosing%20Colors%20With%20Color%20Wells%20and%20Color%20Panels.md)

