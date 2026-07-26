---
title: 'cropping(to:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgimage/cropping(to:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimage/cropping(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimage/cropping%28to%3A%29.json'
content_hash: 'sha256:b9d5d09620b39dad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGImage](../cgimage.md)

# cropping(to:)

<sub>Instance Method</sub>

Creates a bitmap image using the data contained within a subregion of an existing bitmap image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cropping(to rect: CGRect) -> CGImage?
```

## Parameters

- `rect` — A rectangle specifying the portion of the image to keep.

## Return Value

A [CGImage](../cgimage.md) object that specifies a subimage of the image. If the `rect` parameter defines an area that is not in the image, returns `NULL`.

## Discussion

Cropping removes content around the designated rectangle; it cuts out the desired area of the input image and returns an image of the cropped size.

![Butterfly photo with background cropped out](../../../../attachments/44e39ae57f70286b7a3ea4d5a6491b8b/media-2951298@2x.png)

[CGImageCreateWithImageInRect](<cropping(to_).md>) performs the following tasks to create the subimage:

- It calls the [CGRectIntegral](<../cgrectintegral(__).md>) function to adjust the `rect` parameter to integral bounds.
- It intersects the `rect` with a rectangle whose origin is `(0,0)` and size is equal to the size of the image specified by the `image` parameter.
- It reads the pixels within the resulting rectangle, treating the first pixel within as the origin of the subimage.

If `W` and `H` are the width and height of image, respectively, then the point `(0,0)` corresponds to the first pixel of the image data. The point `(W–1, 0)` is the last pixel of the first row of the image data, while `(0, H–1)` is the first pixel of the last row of the image data and `(W–1, H–1)` is the last pixel of the last row of the image data.

> [!important] Important
> Be sure to specify the subrectangle’s coordinates relative to the original image’s full size, even if the [UIImageView](../../uikit/uiimageview.md) shows only a scaled version.

The resulting image retains a reference to the original image, which means you may release the original image after calling this function.  In Swift, you do not need to release the original image reference explicitly.

**Swift**

```swift
    func cropImage(_ inputImage: UIImage, toRect cropRect: CGRect, viewWidth: CGFloat, viewHeight: CGFloat) -> UIImage? 
{    
    let imageViewScale = max(inputImage.size.width / viewWidth,
                             inputImage.size.height / viewHeight)

    // Scale cropRect to handle images larger than shown-on-screen size
    let cropZone = CGRect(x:cropRect.origin.x * imageViewScale,
                          y:cropRect.origin.y * imageViewScale,
                          width:cropRect.size.width * imageViewScale,
                          height:cropRect.size.height * imageViewScale)

    // Perform cropping in Core Graphics
    guard let cutImageRef: CGImage = inputImage.cgImage?.cropping(to:cropZone)
    else {
        return nil
    }

    // Return image to UIImage
    let croppedImage: UIImage = UIImage(cgImage: cutImageRef)
    return croppedImage
}
```

**Objective-C**

```objc
- (UIImage*) cropImage:(UIImage*)inputImage
                toRect:(CGRect)cropRect
             viewWidth:(CGFloat)viewWidth
            viewHeight:(CGFloat)viewHeight
{
    // viewWidth, viewHeight are dimensions of imageView
    const CGFloat imageViewScale = MAX(inputImage.size.width/_viewWidth, inputImage.size.height/_viewHeight);

    // Scale cropRect to handle images larger than shown-on-screen size
    cropRect.origin.x *= imageViewScale;
    cropRect.origin.y *= imageViewScale;
    cropRect.size.width *= imageViewScale;
    cropRect.size.height *= imageViewScale;
    
    // Perform cropping in Core Graphics
    CGImageRef cutImageRef = CGImageCreateWithImageInRect(inputImage.CGImage, cropRect);
    
    // Convert back to UIImage
    UIImage* croppedImage = [UIImage imageWithCGImage:cutImageRef];
    
    // Clean up reference pointers
    CGImageRelease(cutImageRef);
    
    return croppedImage;
}
```

If you already use [CIImage](../../coreimage/ciimage.md), or if you are post-processing images as [CIImage](../../coreimage/ciimage.md) data in Core Image, such as chaining together multiple filters to the cropped result, it may be more efficient to crop [CIImage](../../coreimage/ciimage.md) directly in the Core Image framework using the `CICrop` filter; in this case, use the convenience function [cropped(to:)](<../../coreimage/ciimage/cropped(to_).md>).

## See Also

### Creating images by modifying an image

- [CGImageCreateWithMask](<masking(__).md>) — Creates a bitmap image from an existing image and an image mask.
- [copy(maskingColorComponents:)](<copy(maskingcolorcomponents_).md>)
