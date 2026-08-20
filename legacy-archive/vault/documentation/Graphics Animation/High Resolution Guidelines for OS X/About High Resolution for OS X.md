---
title: High Resolution Guidelines for OS X
apple_id: TP40012302
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/HighResolutionOSX/Introduction/Introduction.html
archived_at: '2026-07-15T07:35:05.945065Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](High%20Resolution%20Explained-%20Features%20and%20Benefits.md)

# About High Resolution for OS X

High-resolution displays provide a rich visual experience, allowing users to see sharper text and more details in photos than on standard-resolution displays. The high-resolution model for OS X is based on Quartz. Introduced in OS X v10.0, Quartz allows developers to draw into an abstract coordinate space—_user space_—without regard for the characteristics of the final drawing destination: printer, screen, bitmap, PDF. The OS X implementation of high resolution extends this flexible imaging model throughout the system, to the level of the display.

When you run a high-resolution-savvy app on a high-resolution device, the text, vector drawing, and UI controls are sharp. This is due to the increased pixel density—pixels are smaller and there are more of them per unit area. Each _point_ in user space is backed by four pixels. The increase in pixel density results in higher details for drawing and text rendering. As shown in Figure I-1, a standard-resolution display has fewer pixels available to approximate the shape of a curve, resulting in a jagged look when magnified. But a high-resolution display has quadruple the pixels available to approximate the curve, resulting in a much smoother-looking curve. Magnified or not, when you look at the same shape on a standard-resolution display and a high-resolution one, the difference is obvious immediately.

__Figure I-1__  Drawing is sharper in high resolution

!

The guidelines in this document describe how to optimize your app for high resolution. At the core of most guidelines in this document is that you should think in points most of the time, but understand the exceptions when you must be aware of pixels. You’ll need to free your code from relying on device coordinates, except in perhaps the most extreme edge cases. You’ll also need to increase the resolution of all the graphics resources your app uses.

### Get Your App Ready for High Resolution

OS X does much of the work required to handle the different resolutions, but there are some tasks you must perform, such as providing specially named high-resolution images and updating icon assets. You’ll also need to update your code to use the most recent APIs, especially in cases where you are currently using deprecated APIs.

### Tune Advanced Technologies for High Resolution

If your app uses pixel-based technologies (such as OpenGL, Quartz image patterns), needs low-level access to display information, must examine pixels directly, or supports other specialized tasks or technologies, you’ll need to perform some work to ensure your app works well in high resolution. At the very least, scan through the list of advanced techniques to see which ones, if any, apply to your app.

### Make Sure Your App Works After Optimizing for High Resolution

You don’t need a high-resolution display to start optimizing your app and testing the code. Quartz Debug has features you can use to make sure your app is working as expected. When things don’t work as expected, the troubleshooting section can help you figure out the issue.

### Understand the User Experience If You Don’t Optimize Right Away

If you aren’t able to update your app immediately for high resolution, it’s important to understand how users will experience your app as they wait for you to release the optimized version.

These documents provide additional details for using many of the technologies referred to in this document:

- _OS X Human Interface Guidelines_ provides advice on designing high-resolution artwork for app icons.
- _[Cocoa Drawing Guide](../../Cocoa/Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_ provides important conceptual information for understanding drawing and image handling. It also contains numerous examples that show how to use AppKit drawing technologies.
[Next](High%20Resolution%20Explained-%20Features%20and%20Benefits.md)

