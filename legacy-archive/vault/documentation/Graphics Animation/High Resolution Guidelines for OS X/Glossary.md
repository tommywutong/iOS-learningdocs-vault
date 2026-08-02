---
title: High Resolution Guidelines for OS X
apple_id: TP40012302
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/HighResolutionOSX/Glossary/Glossary.html
archived_at: '2026-07-15T07:35:05.933967Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [High Resolution Guidelines for OS X](About%20High%20Resolution%20for%20OS%20X.md)


[Next](Document%20Revision%20History.md)[Previous](Testing%20and%20Troubleshooting%20High-Resolution%20Content.md)

# Glossary

- __backing scale factor__

  The relationship between points in a virtual object (view, window, or screen) and the pixels that represent that object onscreen. In OS X this value is either 1.0 or 2.0, depending on the resolution of the underlying device.

- __backing store__

  An offscreen buffer used for drawing operations.

- __base space__

  The default coordinate system for a graphics context.

- __current transformation matrix__

  An affine transform that the system uses to map points from one coordinate space to another for the current graphics context.

- __device space__

  A fixed coordinate system that corresponds to individual pixels on a physical device, such as a display or printer. One unit in device space equals one pixel.

- __framework-scaled mode__

  The way the application framework automatically adjusts Cocoa app content onscreen to ensure sharp graphics whether the display is standard or high resolution. Application frameworks draw all standard user interface elements—such as buttons, menus, and the window title bar—to the correct size for the resolution.

- __magnified mode__

  An accommodation OS X makes to allow apps that aren’t high resolution to run acceptably on a high-resolution display. The system magnifies the contents of the backing store to fill the display.

- __pixel__

  The smallest picture unit on a display device.

- __point__

  One unit in user space, prior to any transformations on the space. The term point has its origin in the print industry, which defines 72 points as equal to 1 inch in physical space. When used in reference to high resolution in OS X, points in user space do not have any relation to measurements in the physical world.

- __user size__

  The size, in points, of an object onscreen.

- __user space__

  A device-independent coordinate system that an application draws into. One unit in user space equals one point. You can transform user space by applying scaling, rotation, and translation. The mapping from user space to device space depends on: (1) The mapping between default user space and device space; (2) The coordinate transformations applied to user space either by the system API or your own API.

[Next](Document%20Revision%20History.md)[Previous](Testing%20and%20Troubleshooting%20High-Resolution%20Content.md)

