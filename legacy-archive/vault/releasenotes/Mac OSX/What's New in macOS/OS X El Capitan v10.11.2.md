---
title: What's New in macOS
apple_id: TP40001812
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/WhatsNewInOSX/Articles/MacOSX10_11_2.html
archived_at: '2026-07-18T02:58:48.536220Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [What's New in macOS](Introduction.md)


[Next](OS%20X%20El%20Capitan%20v10.11.md)[Previous](macOS%20Sierra%2010.12.md)

# OS X El Capitan v10.11.2

This article summarizes the key technology changes and improvements in OS X v10.11.2. The information about these changes is organized into sections by technology area.

Please file any bug reports about this release or this documentation at [http://bugreport.apple.com/](http://bugreport.apple.com/).

OS X v10.11.2 contains several enhancements to the OS X display pipeline. The following sections highlight new features of particular importance for professional and high-end graphics apps.

30-Bit Color is now supported on the Mac Pro (Late 2013), iMac (Retina 5K, 27-inch, Late 2014), and iMac (Retina 5K, 27-inch, Late 2015). The frame buffer of these Macs has a depth of 10 bits per color component, allowing apps to display graphics and imagery with more than 256 color gradations per component. To take advantage of deep color output in your Metal or OpenGL graphics pipeline, assign a half-float pixel format to your displayable render target. In a Metal app, use the [MTLPixelFormatRGBA16Float](https://developer.apple.com/documentation/metal/mtlpixelformat/rgba16float) pixel format; in an OpenGL app, use the `GL_RGB16` or `GL_RGBA16` pixel format.

The displays on the new iMac (Retina 4K, 21.5-inch, Late 2015) and iMac (Retina 5K, 27-inch, Late 2015) are based on the P3 color gamut. This wider color gamut allows a broader range of colors to be reproduced, as compared to sRGB. Two new color space constants are now available in the latest OS X SDK:

- Display P3 ([kCGColorSpaceDisplayP3](https://developer.apple.com/documentation/coregraphics/kcgcolorspacedisplayp3))

  The Display P3 color space uses the standard DCI-P3 primaries, a D65 white point, and the same gamma curve as the sRGB IEC61966-2.1 color space. It is a canonicalization of the new iMac display profiles that is useful for tagging wide color gamut content during export.
- DCI-P3 ([kCGColorSpaceDCIP3](https://developer.apple.com/documentation/coregraphics/kcgcolorspacedcip3))

  The standard DCI-P3 color space is provided for compatibility with content developed for digital cinema and post-production workflows.

OS X is built on top of several color-managed frameworks that automatically handle the wider color gamut. However, if your Metal or OpenGL app implements its own color management pipeline, or if your app performs complex color management operations, then you should account for the new color space constants. For more information on color management, see _[Best Practices for Color Management in OS X and iOS](https://developer.apple.com/library/archive/technotes/tn2313/_index.html#//apple_ref/doc/uid/DTS40014694)_.

Additional levels of display brightness are now accessible to apps on the iMac (Retina 5K, 27-inch, Late 2014) and iMac (Retina 5K, 27-inch, Late 2015). This Extended Dynamic Range (EDR) allows for content to be rendered with a brightness level that extends beyond the typical 1.0 maximum value, depending on ambient lighting conditions. To take advantage of EDR output in your Metal or OpenGL graphics pipeline, subscribe to the [NSApplicationDidChangeScreenParametersNotification](https://developer.apple.com/documentation/appkit/nsapplicationdidchangescreenparametersnotification) notification; a new maximum value will then be posted to the [maximumExtendedDynamicRangeColorComponentValue](https://developer.apple.com/documentation/appkit/nsscreen/1388362-maximumextendeddynamicrangecolor) property which you can use as an input to your graphics shader algorithms (e.g. tone mapping). In a Metal app, use the [wantsExtendedDynamicRangeContent](https://developer.apple.com/documentation/quartzcore/cametallayer/1478161-wantsextendeddynamicrangecontent) property to enable the notification; in an OpenGL app, use the [wantsExtendedDynamicRangeOpenGLSurface](https://developer.apple.com/documentation/appkit/nsopenglview/1807226-wantsextendeddynamicrangeopengls) property to enable the notification.

[Next](OS%20X%20El%20Capitan%20v10.11.md)[Previous](macOS%20Sierra%2010.12.md)

