---
title: Drawing and Printing Guide for iOS
apple_id: TP40010156
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Graphics & Animation
technology: UIKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/LoadingImages/LoadingImages.html
archived_at: '2026-07-15T04:56:11.562463Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Drawing and Printing Guide for iOS](About%20Drawing%20and%20Printing%20in%20iOS.md)


[Next](Document%20Revision%20History.md)[Previous](Supporting%20High-Resolution%20Screens%20In%20Views.md)

# Loading Images

For both functional and aesthetic reasons, images are a pervasive element of app user interfaces. They can be a key differentiating factor for apps.

Many images used by apps, including launch images and app icons, are stored as files in the app’s main bundle. You can have launch images and icons that are specific to device type (iPad versus iPhone and iPod touch) and that are optimized for high-resolution displays. You can find full descriptions of these bundled image files in [Advanced App Tricks](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/PerformanceTips/PerformanceTips.html#//apple_ref/doc/uid/TP40007072-CH7) and [App-Related Resources](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Inter-AppCommunication/Inter-AppCommunication.html#//apple_ref/doc/uid/TP40007072-CH6) in _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_. [Updating Your Image Resource Files](Supporting%20High-Resolution%20Screens%20In%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjvfvjvooa) discusses adjustments that make your image files compatible with high-resolution screens.

In addition, iOS provides support for loading and displaying images using both the UIKit and Core Graphics [frameworks](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56). How you determine which classes and functions to use to draw images depends on how you intend to use them. Whenever possible, though, it is recommended that you use the classes of UIKit for representing images in your code. Table C-1 lists some of the usage scenarios and the recommended options for handling them.

__Table C-1__  Usage scenarios for images

| Scenario | Recommended usage |
| Display an image as the content of a view | Use the [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) class to display the image. This option assumes that your view’s only content is an image. You can still layer other views on top of the image view to draw additional controls or content. |
| Display an image as an adornment for part of a view | Load and draw the image using the [UIImage](https://developer.apple.com/documentation/uikit/uiimage) class. |
| Save some bitmap data into an image object | You can do this using the UIKit functions or Core Graphics functions described in [Creating New Images Using Bitmap Graphics Contexts](Drawing%20and%20Creating%20Images.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjtfvjvooa). |
| Save an image as a JPEG or PNG file | Create a `UIImage` object from the original image data. Call the [UIImageJPEGRepresentation](https://developer.apple.com/documentation/uikit/1624115-uiimagejpegrepresentation) or [UIImagePNGRepresentation](https://developer.apple.com/documentation/uikit/1624096-uiimagepngrepresentation) function to get an `NSData` object, and use that object’s methods to save the data to a file. |

The UIKit framework as well as the lower-level system frameworks of iOS give you a wide range of possibilities for creating, accessing, drawing, writing, and manipulating images.

The UIKit framework has three classes and one protocol that are related to images in some way:

**[UIImage](https://developer.apple.com/documentation/uikit/uiimage)**
: Objects of this class represent images in the UIKit framework. You can create them from several different sources, including files and Quartz image objects. Methods of the class enable you to draw images to the current graphics context using different blend modes and opacity values.

The `UIImage` class automatically handles any required transformations for you, such as applying the proper scale factor (taking into consideration high-resolution displays) and, when given Quartz images, modifying the coordinate system of the image so that it matches the default coordinate system of UIKit (where the y origin is at the upper left).

**[UIImageView](https://developer.apple.com/documentation/uikit/uiimageview)**
: Objects of this class are views that display either a single image or animate a series of images. If an image is to be the sole content of a view, use the `UIImageView` class instead of drawing the image.

**[UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller) and [UIImagePickerControllerDelegate](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate)**
: This class and protocol give your app a way to obtain images (photos) and movies supplied by the user. The class presents and manages user interfaces for choosing and taking photos and movies. When users pick a photo, it delivers the selected `UIImage` object to the delegate, which must implement the protocol methods.

In addition to these classes, UIKit declares functions that you can call to perform a variety of tasks with images:

- __Drawing into an image-backed graphics context.__ The [UIGraphicsBeginImageContext](https://developer.apple.com/documentation/uikit/1623922-uigraphicsbeginimagecontext) function creates an offscreen bitmap graphics context. You can draw in this graphics context and then extract a `UIImage` object from it. (See [Drawing Images](Drawing%20and%20Creating%20Images.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjtfvjvomjq) for additional information.)
- __Getting or caching image data.__ Each [UIImage](https://developer.apple.com/documentation/uikit/uiimage) object has a backing Core Graphics image object (`CGImageRef`) that you can access directly. You can then pass the Core Graphics object to the Image I/O framework to save the data. You can also convert the image data in a `UIImage` object to either a PNG or JPEG format by calling the [UIImagePNGRepresentation](https://developer.apple.com/documentation/uikit/1624096-uiimagepngrepresentation) or [UIImageJPEGRepresentation](https://developer.apple.com/documentation/uikit/1624115-uiimagejpegrepresentation) functions. You can then access the bytes in the data object and you can write the image data to a file.
- __Writing an image to the Photo Album on a device.__ Call the [UIImageWriteToSavedPhotosAlbum](https://developer.apple.com/documentation/uikit/1619125-uiimagewritetosavedphotosalbum) function, passing in a `UIImage` object, to put that image in the Photo Album on a device.

[Drawing Images](Drawing%20and%20Creating%20Images.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjtfvjvomjq) identifies scenarios when you would use these UIKit classes and functions.

You can use several system frameworks other than UIKit to create, access, modify, and write images. If you find that you cannot accomplish a certain image-related task using a UIKit method or function, a function of one of these lower-level frameworks might be able do what you want. Some of these functions might require a Core Graphics image object ([CGImageRef](https://developer.apple.com/documentation/coregraphics/cgimageref)). You can access the `CGImageRef` object backing a [UIImage](https://developer.apple.com/documentation/uikit/uiimage) object through the [CGImage](https://developer.apple.com/documentation/uikit/uiimage/1624159-cgimage) property.

The Core Graphics framework of Quartz is the most important of the lower-level system frameworks. Several of its functions correspond to UIKit functions and methods; for example, some Core Graphics functions allow you to create and draw to bitmap graphics contexts, while others let you create images from various sources. However, Core Graphics offers more options for handling images. With Core Graphics you can create and apply image masks, create images from portions of existing images, apply color spaces, and access a number of additional image attributes, including bytes per row, bits per pixel, and rendering intent.

The Image I/O framework is closely related to Core Graphics. It allows an app to read and write most image file formats, including the standard web formats, high dynamic range images, and raw camera data. It features fast image encoding and decoding, image metadata, and image caching.

Assets Library is a framework that allows an app to access assets managed by the Photos app. You can get an asset either by representation (for example, PNG or JPEG) or URL. From the representation or URL you can obtain a Core Graphics image object or the raw image data. The framework also lets you write images to the Saved Photos Album.

Table C-2 lists the image formats supported directly by iOS. Of these formats, the PNG format is the one most recommended for use in your apps. Generally, the image formats that UIKit supports are the same formats supported by the Image I/O framework.

__Table C-2__  Supported image formats

| Format | Filename extensions |
| Portable Network Graphic (PNG) | `.png` |
| Tagged Image File Format (TIFF) | `.tiff` or `.tif` |
| Joint Photographic Experts Group (JPEG) | `.jpeg` or `.jpg` |
| Graphic Interchange Format (GIF) | `.gif` |
| Windows Bitmap Format (DIB) | `.bmp` or `.BMPf` |
| Windows Icon Format | `.ico` |
| Windows Cursor | `.cur` |
| XWindow bitmap | `.xbm` |

Providing high-quality images for your user interface should be a priority in your design. Images provide a reasonably efficient way to display complicated graphics and should be used wherever they are appropriate. When creating images for your app, keep the following guidelines in mind:

- __Use the PNG format for images.__ The PNG format provides lossless image content, meaning that saving image data to a PNG format and then reading it back results in the exact same pixel values. PNG also has an optimized storage format designed for faster reading of the image data. It is the preferred image format for iOS.
- __Create images so that they do not need resizing.__ If you plan to use an image at a particular size, be sure to create the corresponding image resource at that size. Do not create a larger image and scale it down to fit, because scaling requires additional CPU cycles and requires interpolation. If you need to present an image at variable sizes, include multiple versions of the image at different sizes and scale down from an image that is relatively close to the target size.
- __Remove alpha channels from opaque PNG files.__ If every pixel of a PNG image is opaque, removing the alpha channel avoids the need to blend the layers containing that image. This simplifies compositing of the image considerably and improves drawing performance.

[Next](Document%20Revision%20History.md)[Previous](Supporting%20High-Resolution%20Screens%20In%20Views.md)

