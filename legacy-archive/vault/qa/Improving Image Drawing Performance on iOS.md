---
title: Improving Image Drawing Performance on iOS
apple_id: DTS40010245
resource_type: QA
platform: iOS
topic: Graphics & Animation
technology: CoreGraphics
published: '2010-08-18'
source_url: https://developer.apple.com/library/archive/qa/qa1708/_index.html
archived_at: '2026-07-18T02:34:16.713963Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1708

# Improving Image Drawing Performance on iOS

## Q:  What can I do to improve my image drawing performance (`CGContextDrawImage`, `UIImage/-drawInRect:`, etc)?

A: What can I do to improve my image drawing performance (`CGContextDrawImage`, `UIImage/-drawInRect:`, etc)?

In general, no matter what iOS you're targeting, you should avoid having frequent calls to `-drawRect:`. This is particularly crucial for improving your application performance on iPhone 4, because you have four times the number of pixels to fill on iPhone 4 compared with other iPhone models.

If you're hitting image drawing performance issues, then it is likely that you are drawing the images in your view's `-drawRect:` method using `CGContextDrawImage` or `UIImage/-drawInRect:`, and are invalidating and redrawing the view rapidly or even every frame. Note that, because of the way that iPhone/iPod touch/iPad updates its screen, the entire view will be redrawn if you call `-setNeedsDisplayInRect:` or `-setNeedsDisplay:`.

Every `UIView` is backed with a `CALayer` and images as layer contents remain in memory as long as the `CALayer` stays in the hierarchy. This means that most of the operations you see in an application, including movement, rotation, and scaling of the view/layer, do not require a redraw. The best way for animating (moving, rotating or scaling) images is therefore to create views or layers for the images and then use Core Animation to do any animation. This way you can avoid entirely calls to `-drawRect:` and thus calls to `CGContextDrawImage` or `UIImage/-drawInRect:`.

To illustrate it with a simple example, let's say you want to draw a sprite rotating about its `z` axis perpendicular to the screen. One way to do it would be applying a rotation transform to the Current Transform Matrix (`CGContextRotateCTM`) and redrawing the image (`CGContextDrawImage`) in the `UIView`'s `-drawRect:` method at every animation step. However, a much more efficient way is to set the image as the `contents` property of the backing `CALayer`, and then animate the layer's `transform` property to achieve the rotating animation. In the following, Listing 1 demonstrates how to set a `UIImage` as layer contents in a `UIImageView`, and Listing 2 demonstrates an example of animating the view/layer's transform. For more information on programming with Core Animation, see [Core Animation Programming Guide](https://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004627-SW1).

If you have separate moving components within an image, then you should break it down to separate views or layers and animate them individually. For instance, if you're drawing a draggable handle over the image, rather than invalidating the entire image view when the handle is moving, you should put it in an individual layer and move that layer around.

There are some use cases (not the majority) for which the `CALayer` and Core Animation approach will not work. For those cases, keep in mind that `CGContextDrawImage` and `UIImage/-drawInRect:` could spend a lot of time in decompressing or resampling the images as necessary because the images will not be cached in the layer tree. If you can, adjust your resource art so that the image size (in pixels) is the same as its displayed size (in pixels), meaning you would provide different image sets for iPhone/iPod touch (`image.png`), iPhone 4 (`image@2x.png`), and iPad (`image-iPad.png`). Further, you could cache the images yourself by drawing into a bitmap context and caching the image you create from the context. Listing 3 demonstrates how to create your own `UIImage` copy with the target width and height. You can then cache the resulting image in an image array.

Even if the contents of the view or layer are changing in such a way that you cannot eliminate `-drawRect:` entirely, by dividing the contents into separate views or layers, you can reduce the amount that you need to redraw. When your view logically consists of multiple independent parts, it's recommended that you break it down into a view containing subviews or sublayers with your contents in them. This will allow you to work with them in a more natural way and isolate your drawing updates for each subsection of the view instead of having to take the penalty of updating the entire view.

__Listing 1__  Setting a UIImage as layer contents in a UIImageView

```
// This also sets the view's contentScaleFactor to the image's scale factor imageView.image = image;
```


__Listing 2__  Animating the z rotation of a view

```objc
- (void)rotateView:(UIView *)view toAngle:(float)angle {     [UIView beginAnimations:nil context:nil];     [view setTransform:CGAffineTransformMakeRotation(angle)];     [UIView commitAnimations]; }
```


__Listing 3__  Resizing a UIImage. The result can be cached in an image array.

```objc
- (UIImage*)resizeImage:(UIImage*)image toWidth:(NSInteger)width height:(NSInteger)height {     // Create a graphics context with the target size     // On iOS 4 and later, use UIGraphicsBeginImageContextWithOptions to take the scale into consideration     // On iOS prior to 4, fall back to use UIGraphicsBeginImageContext     CGSize size = CGSizeMake(width, height);     if (NULL != UIGraphicsBeginImageContextWithOptions)         UIGraphicsBeginImageContextWithOptions(size, NO, 0);     else         UIGraphicsBeginImageContext(size);      CGContextRef context = UIGraphicsGetCurrentContext();      // Flip the context because UIKit coordinate system is upside down to Quartz coordinate system     CGContextTranslateCTM(context, 0.0, height);     CGContextScaleCTM(context, 1.0, -1.0);      // Draw the original image to the context     CGContextSetBlendMode(context, kCGBlendModeCopy);     CGContextDrawImage(context, CGRectMake(0.0, 0.0, width, height), image.CGImage);      // Retrieve the UIImage from the current context     UIImage *imageOut = UIGraphicsGetImageFromCurrentImageContext();      UIGraphicsEndImageContext();      return imageOut; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-08-18 | New document that discusses how to improve CGContextDrawImage and UIImage/drawInRect: performance on iOS. |

