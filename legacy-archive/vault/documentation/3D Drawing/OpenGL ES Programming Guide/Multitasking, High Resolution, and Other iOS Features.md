---
title: OpenGL ES Programming Guide
apple_id: TP40008793
resource_type: Guide
platform: tvOS|iOS
topic: Graphics & Animation
technology: OpenGLES
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/ImplementingaMultitasking-awareOpenGLESApplication/ImplementingaMultitasking-awareOpenGLESApplication.html
archived_at: '2026-07-15T04:56:18.226519Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL ES Programming Guide](About%20OpenGL%20ES.md)


[Next](OpenGL%20ES%20Design%20Guidelines.md)[Previous](Drawing%20to%20Other%20Rendering%20Destinations.md)

# Multitasking, High Resolution, and Other iOS Features

Many aspects of working with OpenGL ES are platform neutral, but some details of working with OpenGL ES on iOS bear special consideration. In particular, an iOS app using OpenGL ES must handle multitasking correctly or risk being terminated when it moves to the background. You should also consider display resolution and other device features when developing OpenGL ES content for iOS devices.

Your app can continue to run when a user switches to another app. For an overall discussion of multitasking on iOS, see [App States and Multitasking](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html#//apple_ref/doc/uid/TP40007072-CH4).

An OpenGL ES app must perform additional work when it is moved into the background. If an app handles these tasks improperly, it may be terminated by iOS instead. Also, an app may want to free OpenGL ES resources so that those resources are made available to the foreground app.

An OpenGL ES app is terminated if it attempts to execute OpenGL ES commands on the graphics hardware. iOS prevents background apps from accessing the graphics processor so that the frontmost app is always able to present a great experience to the user. Your app can be terminated not only if it makes OpenGL ES calls while in the background but also if previously submitted commands are flushed to the GPU while in the background. Your app must ensure that all previously submitted commands have finished executing before moving into the background.

If you use a GLKit view and view controller, and only submit OpenGL ES commands during your drawing method, your app automatically behaves correctly when it moves to the background. The [GLKViewController](https://developer.apple.com/documentation/glkit/glkviewcontroller) class, by default, pauses its animation timer when your app becomes inactive, ensuring that your drawing method is not called.

If you do not use GLKit views or view controllers or if you submit OpenGL ES commands outside a [GLKView](https://developer.apple.com/documentation/glkit/glkview) drawing method, you must take the following steps to ensure that your app is not terminated in the background:

1. In your app delegate’s [applicationWillResignActive:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622950-applicationwillresignactive) method, your app should stop its animation timer (if any), place itself into a known good state, and then call the `glFinish` function.
2. In your app delegate’s [applicationDidEnterBackground:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622997-applicationdidenterbackground) method, your app may want to delete some of its OpenGL ES objects to make memory and resources available to the foreground app. Call the `glFinish` function to ensure that the resources are removed immediately.
3. After your app exits its [applicationDidEnterBackground:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622997-applicationdidenterbackground) method, it must not make any new OpenGL ES calls. If it makes an OpenGL ES call, it is terminated by iOS.
4. In your app’s [applicationWillEnterForeground:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623076-applicationwillenterforeground) method, re-create any objects and restart your animation timer.

To summarize, your app needs to call the `glFinish` function to ensure that all previously submitted commands are drained from the command buffer and are executed by OpenGL ES. After it moves into the background, you must avoid all use of OpenGL ES until it moves back into the foreground.

Your app is never required to free up OpenGL ES objects when it moves into the background. Usually, your app should avoid disposing of its content. Consider two scenarios:

- A user is playing your game and exits it briefly to check their calendar. When the player returns to your game, the game’s resources are still in memory, and the game can resume immediately.
- Your OpenGL ES app is in the background when the user launches another OpenGL ES app. If that app needs more memory than is available on the device, the system silently and automatically terminates your app without requiring it to perform any additional work.

Your goal should be to design your app to be a good citizen: This means keeping the time it takes to move to the foreground as short as possible while also reducing its memory footprint while it is in the background.

Here’s how you should handle the two scenarios:

- Your app should keep textures, models and other assets in memory; resources that take a long time to re-create should never be disposed of when your app moves into the background.
- Your app should dispose of objects that can be quickly and easily re-created. Look for objects that consume large amounts of memory.

Easy targets are the framebuffers your app allocates to hold rendering results. When your app is in the background, it is not visible to the user and may not render any new content using OpenGL ES. That means the memory consumed by your app’s framebuffers is allocated, but is not useful. Also, the contents of the framebuffers are _transitory_; most app re-create the contents of the framebuffer every time they render a new frame. This makes renderbuffers a memory-intensive resource that can be easily re-created, becoming a good candidate for an object that can be disposed of when moving into the background.

If you use a GLKit view and view controller, the [GLKViewController](https://developer.apple.com/documentation/glkit/glkviewcontroller) class automatically disposes of its associated view’s framebuffers when your app moves into the background. If you manually create framebuffers for other uses, you should dispose of them when your app moves to the background. In either case, you should also consider what other transitory resources your app can dispose of at that time.

By default, the value of a GLKit view’s [contentScaleFactor](https://developer.apple.com/documentation/uikit/uiview/1622657-contentscalefactor) property matches the scale of the screen that contains it, so its associated framebuffer is configured for rendering at the full resolution of the display. For more information on how high-resolution displays are supported in UIKit, see [Supporting High-Resolution Screens In Views](https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/SupportingHiResScreensInViews/SupportingHiResScreensInViews.html#//apple_ref/doc/uid/TP40010156-CH15).

If you present OpenGL ES content using a Core Animation layer, its scale factor is set to `1.0` by default. To draw at the full resolution of a Retina display, you should change the scale factor of the [CAEAGLLayer](https://developer.apple.com/documentation/quartzcore/caeagllayer) object to match the screen’s scale factor.

When supporting devices with high resolution displays, you should adjust the model and texture assets of your app accordingly. When running on a high-resolution device, you might want to choose more detailed models and textures to render a better image. Conversely, on a standard-resolution device, you can use smaller models and textures.

An important factor when determining how to support high-resolution displays is performance. The doubling of scale factor on a Retina display quadruples the number of pixels, causing the GPU to process four times as many fragments. If your app performs many per-fragment calculations, the increase in pixels may reduce the frame rate. If you find that your app runs significantly slower at a higher scale factor, consider one of the following options:

- Optimize your fragment shader’s performance using the performance-tuning guidelines found in this document.
- Implement a simpler algorithm in your fragment shader. By doing so, you are reducing the quality of individual pixels to render the overall image at a higher resolution.
- Use a fractional scale factor between 1.0 and and the screen’s scale factor. A scale factor of 1.5 provides better quality than a scale factor of 1.0 but needs to fill fewer pixels than an image scaled to 2.0.
- Use lower-precision formats for your `GLKView` object’s [drawableColorFormat](https://developer.apple.com/documentation/glkit/glkview/1615587-drawablecolorformat) and [drawableDepthFormat](https://developer.apple.com/documentation/glkit/glkview/1615583-drawabledepthformat) properties. By doing this, you reduce the memory bandwidth required to operate on the underlying renderbuffers.
- Use a lower scale factor and enable multisampling. An added advantage is that multisampling also provides higher quality on devices that do not support high-resolution displays.

  To enable multisampling for a `GLKView` object, change the value of its [drawableMultisample](https://developer.apple.com/documentation/glkit/glkview/1615601-drawablemultisample) property. If you are not rendering to a GLKit view, you must manually set up multisampling buffers and resolve them before presenting a final image (see [Using Multisampling to Improve Image Quality](Drawing%20to%20Other%20Rendering%20Destinations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojtfvbuqmjqgmwvgvzu)).

  Multisampling is not free; additional memory is required to store the additional samples, and resolving the samples into the resolve framebuffer takes time. If you add multisampling to your app, always test your app’s performance to ensure that it remains acceptable.

Like any app, an OpenGL ES app should support the user interface orientations appropriate to its content. You declare the supported interface orientations for your app in its information property list, or for the view controller hosting your OpenGL ES content using its [supportedInterfaceOrientations](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621435-supportedinterfaceorientations) method. (See _[View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)_ for details.)

By default, the [GLKViewController](https://developer.apple.com/documentation/glkit/glkviewcontroller) and `GLKView` classes handle orientation changes automatically: When the user rotates the device to a supported orientation, the system animates the orientation change and changes the size of the view controller’s view. When its size changes, a `GLKView` object adjusts the size of its framebuffer and viewport accordingly. If you need to respond to this change, implement the [viewWillLayoutSubviews](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621437-viewwilllayoutsubviews) or [viewDidLayoutSubviews](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621398-viewdidlayoutsubviews) method in your `GLKViewController` subclass, or implement the [layoutSubviews](https://developer.apple.com/documentation/uikit/uiview/1622482-layoutsubviews) method if you’re using a custom `GLKView` subclass.

If you draw OpenGL ES content using a Core Animation layer, your app should still include a view controller to manage user interface orientation.

An iOS device can be attached to an external display. The resolution of an external display and its content scale factor may differ from the resolution and scale factor of the main screen; your code that renders a frame should adjust to match.

The procedure for drawing on an external display is almost identical to that running on the main screen.

1. Create a window on the external display by following the steps in _[Multiple Display Programming Guide for iOS](../../Windows%20Views/Multiple%20Display%20Programming%20Guide%20for%20iOS/Using%20Windows%20to%20Present%20Content%20on%20Multiple%20Displays.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdknjv)_.
2. Add to the window the appropriate view or view controller objects for your rendering strategy.

   - If rendering with GLKit, set up instances of [GLKViewController](https://developer.apple.com/documentation/glkit/glkviewcontroller) and [GLKView](https://developer.apple.com/documentation/glkit/glkview) (or your custom subclasses) and add them to the window using its [rootViewController](https://developer.apple.com/documentation/uikit/uiwindow/1621581-rootviewcontroller) property.
   - If rendering to a Core Animation layer, add the view containing your layer as a subview of the window. To use an animation loop for rendering, create a display link object optimized for the external display by retrieving the [screen](https://developer.apple.com/documentation/uikit/uiwindow/1621597-screen) property of the window and calling its [displayLinkWithTarget:selector:](https://developer.apple.com/documentation/uikit/uiscreen/1617820-displaylink) method.

[Next](OpenGL%20ES%20Design%20Guidelines.md)[Previous](Drawing%20to%20Other%20Rendering%20Destinations.md)

