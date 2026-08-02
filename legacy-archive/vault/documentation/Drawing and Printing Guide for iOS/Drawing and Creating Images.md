---
title: Drawing and Printing Guide for iOS
apple_id: TP40010156
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Graphics & Animation
technology: UIKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/HandlingImages/Images.html
archived_at: '2026-07-15T04:56:11.536135Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Drawing and Printing Guide for iOS](About%20Drawing%20and%20Printing%20in%20iOS.md)


[Next](Generating%20PDF%20Content.md)[Previous](Drawing%20Shapes%20Using%20B%C3%A9zier%20Paths.md)

# Drawing and Creating Images

Most of the time, it is fairly straightforward to display images using standard views. However, there are two situations in which you may need to do additional work:

- If you want to display images as part of a custom view, you must draw the images yourself in your view’s [drawRect:](https://developer.apple.com/documentation/uikit/uiview/1622529-draw) method. [Drawing Images](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjtfvjvomjq) explains how.
- If you want to render images offscreen (to draw later, or to save into a file), you must create a bitmap image context. To learn more, read [Creating New Images Using Bitmap Graphics Contexts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjtfvjvooa).

For maximum performance, if your image drawing needs can be met using the `UIImageView` class, you should use this image object to initialize a `UIImageView` object. However, if you need to draw an image explicitly, you can store the image and use it later in your view’s `drawRect:` method.

The following example shows how to load an image from your app’s [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4).

```
NSString *imagePath = [[NSBundle mainBundle] pathForResource:@"myImage" ofType:@"png"];
UIImage *myImageObj = [[UIImage alloc] initWithContentsOfFile:imagePath];

// Store the image into a property of type UIImage *
// for use later in the class's drawRect: method.
self.anImage = myImageObj;
```

To draw the resulting image explicitly in your view’s `drawRect:` method, you can use any of the drawing methods available in `UIImage`. These methods let you specify where in your view you want to draw the image and therefore do not require you to create and apply a separate transform prior to drawing.

The following snippet draws the image loaded above at the point (10, 10) in the view.

```objc
- (void)drawRect:(CGRect)rect
{
    ...

    // Draw the image.
    [self.anImage drawAtPoint:CGPointMake(10, 10)];
}
```


Most of the time, when drawing, your goal is to show something onscreen. However, it is sometimes useful to draw something to an offscreen buffer. For example, you might want to create a thumbnail of an existing image, draw into a buffer so that you can save it to a file, and so on. To support those needs, you can create a bitmap image context, use UIKit framework or Core Graphics functions to draw to it, and then obtain an image object from the context.

In UIKit, the procedure is as follows:

1. Call [UIGraphicsBeginImageContextWithOptions](https://developer.apple.com/documentation/uikit/1623912-uigraphicsbeginimagecontextwitho) to create a bitmap context and push it onto the graphics stack.

   For the first parameter (`size`), pass a [CGSize](https://developer.apple.com/documentation/coregraphics/cgsize) value to specify the dimensions of the bitmap context (in points).

   For the second parameter (`opaque`), if your image contains transparency (an alpha channel), pass `NO`. Otherwise, pass `YES` to maximize performance.

   For the final parameter (`scale`), pass `0.0` for a bitmap that is scaled appropriately for the main screen of the device, or pass the scale factor of your choice.

   For example, the following code snippet creates a bitmap that is 200 x 200 pixels. (The number of pixels is determined by multiplying the size of the image by the scale factor.)

```
UIGraphicsBeginImageContextWithOptions(CGSizeMake(100.0,100.0), NO, 2.0);
```
2. Use UIKit or Core Graphics routines to draw the content of the image into the newly created graphics context.
3. Call the [UIGraphicsGetImageFromCurrentImageContext](https://developer.apple.com/documentation/uikit/1623924-uigraphicsgetimagefromcurrentima) function to generate and return a [UIImage](https://developer.apple.com/documentation/uikit/uiimage) object based on what you drew. If desired, you can continue drawing and call this method again to generate additional images.
4. Call [UIGraphicsEndImageContext](https://developer.apple.com/documentation/uikit/1623933-uigraphicsendimagecontext) to pop the context from the graphics stack.

The method in Listing 3-1 gets an image downloaded over the Internet and draws it into an image-based context, scaled down to the size of an app icon. It then obtains a `UIImage` object created from the bitmap data and assigns it to an instance variable. Note that the size of the bitmap (the first parameter of [UIGraphicsBeginImageContextWithOptions](https://developer.apple.com/documentation/uikit/1623912-uigraphicsbeginimagecontextwitho)) and the size of the drawn content (the size of `imageRect`) should match. If the content is larger than the bitmap, a portion of the content will be clipped and not appear in the resulting image.

__Listing 3-1__  Drawing a scaled-down image to a bitmap context and obtaining the resulting image

```objc
- (void)connectionDidFinishLoading:(NSURLConnection *)connection {
    UIImage *image = [[UIImage alloc] initWithData:self.activeDownload];
    if (image != nil && image.size.width != kAppIconHeight && image.size.height != kAppIconHeight) {
        CGRect imageRect = CGRectMake(0.0, 0.0, kAppIconHeight, kAppIconHeight);
        UIGraphicsBeginImageContextWithOptions(itemSize, NO, [UIScreen mainScreen].scale);
        [image drawInRect:imageRect];
        self.appRecord.appIcon = UIGraphicsGetImageFromCurrentImageContext();  // UIImage returned.
        UIGraphicsEndImageContext();
    } else {
        self.appRecord.appIcon = image;
    }
    self.activeDownload = nil;
    [image release];
    self.imageConnection = nil;
    [delegate appImageDidLoad:self.indexPathInTableView];
}
```

You can also call Core Graphics functions to draw the contents of the generated bitmap image; the code fragment in Listing 3-2, which draws a scaled-down image of a PDF page, gives an example of this. Note that the code flips the graphics context prior to calling [CGContextDrawPDFPage](https://developer.apple.com/documentation/coregraphics/cgcontext/1456255-drawpdfpage) to align the drawn image with default coordinate system of UIKit.

__Listing 3-2__  Drawing to a bitmap context using Core Graphics functions

```
// Other code precedes...

CGRect pageRect = CGPDFPageGetBoxRect(page, kCGPDFMediaBox);
pdfScale = self.frame.size.width/pageRect.size.width;
pageRect.size = CGSizeMake(pageRect.size.width * pdfScale, pageRect.size.height * pdfScale);
UIGraphicsBeginImageContextWithOptions(pageRect.size, YES, pdfScale);
CGContextRef context = UIGraphicsGetCurrentContext();

// First fill the background with white.
CGContextSetRGBFillColor(context, 1.0,1.0,1.0,1.0);
CGContextFillRect(context,pageRect);
CGContextSaveGState(context);

// Flip the context so that the PDF page is rendered right side up
CGContextTranslateCTM(context, 0.0, pageRect.size.height);
CGContextScaleCTM(context, 1.0, -1.0);

// Scale the context so that the PDF page is rendered at the
// correct size for the zoom level.
CGContextScaleCTM(context, pdfScale,pdfScale);
CGContextDrawPDFPage(context, page);
CGContextRestoreGState(context);
UIImage *backgroundImage = UIGraphicsGetImageFromCurrentImageContext();
UIGraphicsEndImageContext();
backgroundImageView = [[UIImageView alloc] initWithImage:backgroundImage];

// Other code follows...
```

If you prefer using Core Graphics entirely for drawing in a bitmap graphics context, you can use the [CGBitmapContextCreate](https://developer.apple.com/documentation/coregraphics/cgcontext/1455939-init) function to create the context and draw your image contents into it. When you finish drawing, call the [CGBitmapContextCreateImage](https://developer.apple.com/documentation/coregraphics/cgcontext/1454225-makeimage) function to obtain a `CGImageRef` object from the bitmap context. You can draw the Core Graphics image directly or use this it to initialize a `UIImage` object. When finished, call the [CGContextRelease](https://developer.apple.com/documentation/coregraphics/1586509-cgcontextrelease) function on the graphics context.

[Next](Generating%20PDF%20Content.md)[Previous](Drawing%20Shapes%20Using%20B%C3%A9zier%20Paths.md)

