---
title: Drawing and Printing Guide for iOS
apple_id: TP40010156
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Graphics & Animation
technology: UIKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/SupportingHiResScreensInViews/SupportingHiResScreensInViews.html
archived_at: '2026-07-15T04:56:16.413739Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Drawing and Printing Guide for iOS](About%20Drawing%20and%20Printing%20in%20iOS.md)


[Next](Loading%20Images.md)[Previous](Improving%20Drawing%20Performance.md)

# Supporting High-Resolution Screens In Views

Apps built against iOS SDK 4.0 and later need to be prepared to run on devices with different screen resolutions. Fortunately, iOS makes supporting multiple screen resolutions easy. Most of the work of handling the different types of screens is done for you by the system frameworks. However, your app still needs to do some work to update raster-based images, and depending on your app you may want to do additional work to take advantage of the extra pixels available to you.

See [Points Versus Pixels](iOS%20Drawing%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjufvjvony) for important background information related to this topic.

To update your apps for devices with high-resolution screens, you need to do the following:

- Provide a high-resolution image for each image resource in your app bundle, as described in [Updating Your Image Resource Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjvfvjvooa).
- Provide high-resolution app and document icons, as described in [Updating Your App’s Icons and Launch Images](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjvfvjvomq).
- For vector-based shapes and content, continue using your custom Core Graphics and UIKit drawing code as before. If you want to add extra detail to your drawn content, see [Points Versus Pixels](iOS%20Drawing%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjufvjvony) for information on how to do so.
- If you use OpenGL ES for drawing, decide whether you want to opt in to high-resolution drawing and set the scale factor of your layer accordingly, as described in [Drawing High-Resolution Content Using OpenGL ES or GLKit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjvfvjvomjr).
- For custom images that you create, modify your image-creation code to take the current scale factor into account, as described in [Drawing to Bitmap Contexts and PDF Contexts](iOS%20Drawing%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjufvjvomrs).
- If your app uses Core Animation, adjust your code as needed to compensate for scale factors, as described in [Accounting for Scale Factors in Core Animation Layers](iOS%20Drawing%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjufvjvomzx).

The drawing technologies in iOS provide a lot of support to help you make your rendered content look good regardless of the resolution of the underlying screen:

- Standard UIKit views (text views, buttons, table views, and so on) automatically render correctly at any resolution.
- Vector-based content ([UIBezierPath](https://developer.apple.com/documentation/uikit/uibezierpath), [CGPathRef](https://developer.apple.com/documentation/coregraphics/cgpath), PDF) automatically takes advantage of any additional pixels to render sharper lines for shapes.
- Text is automatically rendered at higher resolutions.
- UIKit supports the automatic loading of high-resolution variants (`@2x`) of your images.

If your app uses only native drawing technologies for its rendering, the only thing you need to do to support higher-resolution screens is provide high-resolution versions of your images.

Apps running in iOS 4 should now include two separate files for each image resource. One file provides a standard-resolution version of a given image, and the second provides a high-resolution version of the same image. The naming conventions for each pair of image files is as follows:

- Standard: _<ImageName>__<device_modifier>_`.`_<filename_extension>_
- High resolution: _<ImageName>_`@2x`_<device_modifier>_`.`_<filename_extension>_

The _<ImageName>_ and _<filename_extension>_ portions of each name specify the usual name and extension for the file. The _<device_modifier>_ portion is optional and contains either the string `~ipad` or `~iphone`. You include one of these modifiers when you want to specify different versions of an image for iPad and iPhone. The inclusion of the `@2x` modifier for the high-resolution image is new and lets the system know that the image is the high-resolution variant of the standard image.

When creating high-resolution versions of your images, place the new versions in the same location in your app bundle as the original.

The [UIImage](https://developer.apple.com/documentation/uikit/uiimage) class handles all of the work needed to load high-resolution images into your app. When creating new image objects, you use the same name to request both the standard and the high-resolution versions of your image. For example, if you have two image files, named `Button.png` and `Button@2x.png`, you would use the following code to request your button image:

```
UIImage *anImage = [UIImage imageNamed:@"Button"];
```

On devices with high-resolution screens, the [imageNamed:](https://developer.apple.com/documentation/uikit/uiimage/1624146-imagenamed), [imageWithContentsOfFile:](https://developer.apple.com/documentation/uikit/uiimage/1624123-imagewithcontentsoffile), and [initWithContentsOfFile:](https://developer.apple.com/documentation/uikit/uiimage/1624112-init) methods automatically looks for a version of the requested image with the `@2x` modifier in its name. If it finds one, it loads that image instead. If you do not provide a high-resolution version of a given image, the image object still loads a standard-resolution image (if one exists) and scales it during drawing.

When it loads an image, a `UIImage` object automatically sets the [size](https://developer.apple.com/documentation/uikit/uiimage/1624105-size) and [scale](https://developer.apple.com/documentation/uikit/uiimage/1624110-scale) properties to appropriate values based on the suffix of the image file. For standard resolution images, it sets the `scale` property to 1.0 and sets the size of the image to the image’s pixel dimensions. For images with the `@2x` suffix in the filename, it sets the `scale` property to 2.0 and halves the width and height values to compensate for the scale factor. These halved values correlate correctly to the point-based dimensions you need to use in the logical coordinate space to render the image.

A `UIImage` object automatically takes its scale factor into account during drawing. Thus, any code you have for rendering images should work the same as long as you provide the correct image resources in your app bundle.

If your app uses the [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) class to present multiple images for a highlight or animation, all of the images you assign to that view must use the same scale factor. You can use an image view to display a single image or to animate several images, and you can also provide a highlight image. Therefore, if you provide high-resolution versions for one of these images, then all must have high-resolution versions as well.

In addition to updating your app’s custom image resources, you should also provide new high-resolution icons for your app’s icon and launch images. The process for updating these image resources is the same as for all other image resources. Create a new version of the image, add the `@2x` modifier string to the corresponding image filename, and treat the image as you do the original. For example, for app icons, add the high-resolution image filename to the `CFBundleIconFiles` key of your app’s `Info.plist` file.

For information about specifying the icons and launch images for your app, see [App-Related Resources](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Inter-AppCommunication/Inter-AppCommunication.html#//apple_ref/doc/uid/TP40007072-CH6) in _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_.

If your app uses OpenGL ES or GLKit for rendering, your existing drawing code should continue to work without any changes. When drawn on a high-resolution screen, though, your content is scaled accordingly and will appear more blocky. The reason for the blocky appearance is that the default behavior of the [CAEAGLLayer](https://developer.apple.com/documentation/quartzcore/caeagllayer) class, which you use to back your OpenGL ES renderbuffers (directly or indirectly), is the same as other Core Animation layer objects. In other words, its scale factor is set to 1.0 initially, which causes the Core Animation compositor to scale the contents of the layer on high-resolution screens. To avoid this blocky appearance, you need to increase the size of your OpenGL ES renderbuffers to match the size of the screen. (With more pixels, you can then increase the amount of detail you provide for your content.) Because adding more pixels to your renderbuffers has performance implications, though, you must explicitly opt in to support high-resolution screens.

To enable high-resolution drawing, you must change the scale factor of the view you use to present your OpenGL ES or GLKit content. Changing the [contentScaleFactor](https://developer.apple.com/documentation/uikit/uiview/1622657-contentscalefactor) property of your view from 1.0 to 2.0 triggers a matching change to the scale factor of the underlying `CAEAGLLayer` object. The [renderbufferStorage:fromDrawable:](https://developer.apple.com/documentation/opengles/eaglcontext/1622262-renderbufferstorage) method, which you use to bind the layer object to your renderbuffers, calculates the size of the render buffer by multiplying the layer’s bounds by its scale factor. Thus, doubling the scale factor doubles the width and height of the resulting render buffer, giving you more pixels for your content. After that, it is up to you to provide the content for those additional pixels.

Listing B-1 shows the proper way to bind your layer object to your renderbuffers and retrieve the resulting size information. If you used the OpenGL ES app template to create your code, then this step is already done for you, and the only thing you need to do is set the scale factor of your view appropriately. If you did not use the OpenGL ES app template, you should use code similar to this to retrieve the render buffer size. You should never assume that the render buffer size is fixed for a given type of device.

__Listing B-1__  Initializing a render buffer’s storage and retrieving its actual dimensions

```
GLuint colorRenderbuffer;
glGenRenderbuffersOES(1, &colorRenderbuffer);
glBindRenderbufferOES(GL_RENDERBUFFER_OES, colorRenderbuffer);
[myContext renderbufferStorage:GL_RENDERBUFFER_OES fromDrawable:myEAGLLayer];

// Get the renderbuffer size.
GLint width;
GLint height;
glGetRenderbufferParameterivOES(GL_RENDERBUFFER_OES, GL_RENDERBUFFER_WIDTH_OES, &width);
glGetRenderbufferParameterivOES(GL_RENDERBUFFER_OES, GL_RENDERBUFFER_HEIGHT_OES, &height);
```

If you do opt in to high-resolution drawing, you also need to adjust the model and texture assets of your app accordingly. For example, when running on iPad or on a high-resolution device, you might want to choose larger models and more detailed textures to take advantage of the increased number of pixels. Conversely, on a standard-resolution iPhone, you can continue to use smaller models and textures.

An important factor when determining whether to support high-resolution content is performance. The quadrupling of pixels that occurs when you change the scale factor of your layer from 1.0 to 2.0 puts additional pressure on the fragment processor. If your app performs many per-fragment calculations, the increase in pixels may reduce your app’s frame rate. If you find your app runs significantly slower at the higher scale factor, consider one of the following options:

- Optimize your fragment shader’s performance using the performance-tuning guidelines found in _[OpenGL ES Programming Guide](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/About%20OpenGL%20ES.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojt)_.
- Choose a simpler algorithm to implement in your fragment shader. By doing so, you are reducing the quality of each individual pixel to render the overall image at a higher resolution.
- Use a fractional scale factor between 1.0 and 2.0. A scale factor of 1.5 provides better quality than a scale factor of 1.0 but needs to fill fewer pixels than an image scaled to 2.0.
- OpenGL ES in iOS 4 and later offers multisampling as an option. Even though your app can use a smaller scale factor (even 1.0), implement multisampling anyway. An added advantage is that this technique also provides higher quality on devices that do not support high-resolution displays.

The best solution depends on the needs of your OpenGL ES app; you should test more than one of these options and choose the approach that provides the best balance between performance and image quality.

[Next](Loading%20Images.md)[Previous](Improving%20Drawing%20Performance.md)

