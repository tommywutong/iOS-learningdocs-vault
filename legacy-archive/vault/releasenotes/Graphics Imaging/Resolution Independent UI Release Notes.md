---
title: Resolution Independent UI Release Notes
apple_id: TP40001374
resource_type: Release Note
platform: macOS
topic: null
technology: null
published: '2005-04-29'
source_url: https://developer.apple.com/library/archive/releasenotes/GraphicsImaging/RN-ResolutionIndependentUI/index.html
archived_at: '2026-07-18T02:58:39.428365Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Resolution Independent UI Release Notes for Mac OS X v10.4

> [!IMPORTANT]
> 

Tiger continues the evolution of resolution independence in Mac OS X, bringing it to the computer user interface by breaking the software assumption that all display output is 72 DPI. From its inception, the Quartz graphics system was designed to be resolution independent across output devices. For example Quartz can take content displayed on-screen at 72 DPI and scale it for output to printers of varying DPI. Now the same is true for the display. Resolution Independent UI uses a combination of technologies across the different application development frameworks to scale the UI for varying output resolution.

Resolution independent UI will have an impact on the way you lay out your user interface. It will also impact the graphics you create for your application. The following sections provide an overview of the changes made in Tiger to support this feature.

#### Contents:

- [Scaling Factor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzufvcg63tujruw422fnrsw2zlooreuixzr)
- [Scaling Modes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzufvcg63tujruw422fnrsw2zlooreuixzs)
- [Cocoa Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzufvcg63tujruw422fnrsw2zlooreuixzw)
- [Carbon Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzufvcg63tujruw422fnrsw2zlooreuixzx)
- [Core Graphics Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzufvcg63tujruw422fnrsw2zlooreuixzy)
- [IconServices Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnzufvcg63tujruw422fnrsw2zlooreuixzz)

### Scaling Factor

Resolution Independent UI can be used to provide the user with either detail (more pixels per point, but fewer points on the screen), or real-estate (fewer pixels per point but more points on the screen). To do so the graphics system and user interface require an additional parameter to govern this preference. We call this additional parameter "scaling factor". In future release of Mac OS X we expect this parameter to be settable by the user the same way a user can today go to the Displays Preferences Panel to change the screen resolution.

> [!NOTE]
> 

Let's assume that on a 1600x1200 pixel display we want to target the basic "look" of our current user interface at 1024x768, which assumes a 72 virtual dpi. To take up the same fraction of the display, the UI would need to be larger by a scaling factor of 1600/1024 = 1.5625. Note that from a distance, this desktop would look identical to today's 1024x768, but upon closer inspection the 1600x1200 display would be much more detailed. If instead, we wanted to make the display look like today's 800x600 displays, we would run our 1600x1200 display at a virtual dpi of 144 with a scaling factor of 2, which would be highly detailed using 4 times as many pixels to represent the user interface.

### Scaling Modes

Tiger provides three possible adoption paths (scaling modes) for application developers: _magnification_, _Framework-scaling_, and _Application-scaling_. Each scaling mode offers a certain amount of support for applying scaling factors to rendered UI. If your application is based on modern technologies such as Cocoa or is Carbon based using HIView and CoreGraphics then much of this support is automatic. But if you use older technologies, such as QuickDraw, you may have to do some work to scale your graphics.

### Framework Scaling (Cocoa and Carbon)

Framework-scaling mode is named for the fact that most scaling is handled automatically by an application framework such as Cocoa or Carbon. Framework-scaling is the preferred mode for most content and is the only mode available to Cocoa applications. If you are writing a Carbon application, you must use HIView and Core Graphics to take advantage of framework-scaling.

In framework-scaling mode, the size of the window buffer is increased to accommodate the actual number of pixels that are going to be drawn on the screen. During drawing, the system frameworks automatically scale controls and other interface elements, such as menus and the window title bar, to the appropriate sizes. The system frameworks also add a scaling transform to the CGContext you use to render content in the window. Any calls you make to Quartz or the Application Kit are thereby scaled automatically.

Framework-scaling mode is not appropriate for applications that use QuickDraw calls. The scaling factors applied to the CGContext may change your QuickDraw content in unintended ways. Carbon applications that use QuickDraw should use the application-scaling mode instead.

> [!NOTE]
> 

### Application Scaling (Carbon only)

Application-scaling mode is so named because the application is responsible for handling all scaling of content. In this mode, the size of the window buffer is increased to accommodate the actual number of pixels that are going to be drawn on the screen. The system continues to scale system-defined controls, including the window title bar and menus, but it does not apply a scaling transform to the window’s graphics context. Instead, your application assumes full responsibility for scaling all of its window content to the correct size.

Application-scaling mode is intended for developers who still use legacy technologies such as QuickDraw or for developers who prefer to handle scaling factors themselves. To use this mode, you must query the system for the current scaling factor and use it to create an appropriate transform, which you can then apply to your content.

### Magnification (Carbon only)

Magnified mode is a compatibility mode to provide basic support for scaling until you can modify your applications to use one of the other modes. In magnified mode, the window server applies the current scaling factor to the window buffer to create a magnified view of the image. Because it is based on the original window buffer, the scaled window does not have any more detail than it had originally. Pixels are simply interpolated to fit the new window size. As a result, windows might look like they had simply been magnified by a lens.

Applications do not have to do anything to use magnified mode. It is used by default if you do not specify any other mode when you create your windows. However, magnified mode is not recommended for general usage.

### Cocoa Support

Resolution Independent UI support in Cocoa is described in the _[AppKit Release Notes for macOS 10.13](../App%20Kit/AppKit%20Release%20Notes%20for%20macOS%2010.13.md)_.

### Carbon Support

Resolution Independent UI support in Carbon is described in the _[High Level Toolbox Release Notes (10.4)](https://developer.apple.com/library/archive/releasenotes/Carbon/RN-HIToolbox/index.html#//apple_ref/doc/uid/TP40001013)_.

### Core Graphics Support

Quartz was designed with resolution independence in mind. Since the beginning, developers have been able to use the same code to render both to a printer or the screen. When it comes to support for resolution independent UI, Quartz in combination with HIView or NSView provides most of the support you need automatically. Both HIView and NSView attach an affine transform matrix to the local drawing context to account for scaling factors. This transform automatically converts coordinates in your views to coordinates in the target device.

Even with all the automatic support, there may still be times when you want to know how to adjust your content in advance. For this, Core Graphics provides a new function to get the affine transform used for mapping between your original 72 dpi coordinate space and the coordinate space used when rendering to the target device. This function is defined as follows:

`CGAffineTransform CGContextGetUserSpaceToDeviceSpaceTransform(CGContextRefc);`

You can use the affine transform returned by this function to make adjustments to the coordinates of points and rectangles. You do this by applying the transform to a coordinate in your user space to get a new value in the coordinate space of the target device (a high-resolution monitor, for example). You can then make any necessary adjustments to the device-space coordinate to ensure a proper appearance. For example, you might round off fractional components of device-space coordinates to make sure elements line up properly. You then apply the inverse transformation to the modified device-space coordinates to get the new coordinates in your user space.

### IconServices Support

Icon Services in Tiger has been extended to support icons that are 256 x 256 pixel in size. To support these larger icons, a new icon type selector has been added for you to use in calls to `SetIconFamilyData` and `GetIconFamilyData`. The selector is `kIconServices256PixelDataARGB` and is defined in `IconStorage.h`.

With `SetIconFamilyData`, a non-premultiplied 256x256 ARGB bitmap should be provided as input and IconServices will compress it before storing it in the ICNS container.

With `GetIconFamilyData` an uncompressed raw 256x256 ARGB bitmap is returned. The only difference is that the returned image contains the alpha channel where for the previously supported icon sizes there are 2 separate selectors: one for the mask and one for the data.
