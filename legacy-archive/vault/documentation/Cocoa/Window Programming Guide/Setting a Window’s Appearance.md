---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/SettingWindowAppearance.html
archived_at: '2026-07-15T07:21:16.597508Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Setting%20a%20Window%E2%80%99s%20Title%20and%20Represented%20File.md)[Previous](Using%20the%20Window%20Menu.md)

# Setting a Window’s Appearance

You usually configure most aspects of a window’s appearance in Interface Builder. Sometimes, however, you may need to create a window programmatically, or alter its appearance after it has been created.

The peripheral elements that a window displays define its style. Though you can’t access and manipulate them directly, you can determine at [initialization](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21) whether a window has them by providing a style mask to the initializer. There are four possible style elements, specifiable by combining their mask values using the C bitwise OR operator:

| Element | Mask Value |
| --- | --- |
| A title bar | [NSTitledWindowMask](https://developer.apple.com/documentation/appkit/nstitledwindowmask) |
| A close button | [NSClosableWindowMask](https://developer.apple.com/documentation/appkit/nsclosablewindowmask) |
| A minimize button | [NSMiniaturizableWindowMask](https://developer.apple.com/documentation/appkit/nsminiaturizablewindowmask) |
| A resize bar, border, or box | [NSResizableWindowMask](https://developer.apple.com/documentation/appkit/nsresizablewindowmask) |

You can also specify [NSBorderlessWindowMask](https://developer.apple.com/documentation/appkit/nsborderlesswindowmask), in which case none of these style elements is used.

Typically, you set a window’s appearance once, when it is first created. Sometimes, however, you want to enable or disable a button in the title bar to reflect changed context. To do this, you first retrieve the button from the window using the [standardWindowButton:](https://developer.apple.com/documentation/appkit/nswindow/1419491-standardwindowbutton) of [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) method and then set its enabled state, as in the following example.

```
NSButton *closeButton = [window standardWindowButton:NSWindowCloseButton];
[closeButton setEnabled:NO];
```

The constants required to access standard title bar widgets are defined in the API reference for [NSWindow](https://developer.apple.com/documentation/appkit/nswindow).

You can set a window’s background color and transparency using the methods [setBackgroundColor:](https://developer.apple.com/documentation/appkit/nswindow/1419751-backgroundcolor) and [setAlphaValue:](https://developer.apple.com/documentation/appkit/nswindow/1419186-alphavalue), respectively.

You can set a window’s background color to a non-opaque color. This does not affect the window’s title bar; it only makes the background itself transparent if the window is not opaque, as illustrated in the following example.

```
[myWindow setOpaque:NO]; // YES by default
NSColor *semiTransparentBlue =
    [NSColor colorWithDeviceRed:0.0 green:0.0 blue:1.0 alpha:0.5];
[myWindow setBackgroundColor:semiTransparentBlue];
```

Views placed on a non-opaque window with a transparent background color retain their own opacity. If you want to make the entire window (including the title bar and views placed on the window) transparent, you should use [setAlphaValue:](https://developer.apple.com/documentation/appkit/nswindow/1419186-alphavalue).

You can set a window’s color space using [setColorSpace:](https://developer.apple.com/documentation/appkit/nswindow/1419569-colorspace) and can retrieve the window’s current color space using [colorSpace](https://developer.apple.com/documentation/appkit/nswindow/1419569-colorspace). [NSColorSpace](https://developer.apple.com/documentation/appkit/nscolorspace) objects for use with `setColorSpace:` may be obtained using the class methods documented in _[NSColorSpace Class Reference](https://developer.apple.com/documentation/appkit/nscolorspace)_.

Beginning in OS X version 10.5, windows automatically have a textured gradient applied to their backgrounds. The area on which the gradient is drawn is determined automatically. At times, however, this may not work correctly. If your window does not look correct with automatic gradient calculation, disable it by calling [setAutorecalculatesContentBorderThickness:forEdge:](https://developer.apple.com/documentation/appkit/nswindow/1419218-setautorecalculatescontentborder) with a value of `NO` and the edge to disable automatic calculation for. The value of this property may be accessed using the method [autorecalculatesContentBorderThicknessForEdge:](https://developer.apple.com/documentation/appkit/nswindow/1419356-autorecalculatescontentborderthi).

You can also set and access the content border thickness manually using [setContentBorderThickness:forEdge:](https://developer.apple.com/documentation/appkit/nswindow/1419541-setcontentborderthickness) and [contentBorderThicknessForEdge:](https://developer.apple.com/documentation/appkit/nswindow/1419775-contentborderthickness), respectively.

[Next](Setting%20a%20Window%E2%80%99s%20Title%20and%20Represented%20File.md)[Previous](Using%20the%20Window%20Menu.md)

