---
title: Extracting Portrait Effects matte image data from a photo
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/extracting-portrait-effects-matte-image-data-from-a-photo
source_url: 'https://developer.apple.com/documentation/avfoundation/extracting-portrait-effects-matte-image-data-from-a-photo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/extracting-portrait-effects-matte-image-data-from-a-photo.json'
content_hash: 'sha256:e82a2064b0cfe87b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Photo capture](photo-capture.md) · [AVPortraitEffectsMatte](avportraiteffectsmatte.md)

# Extracting Portrait Effects matte image data from a photo

<sub>Article</sub>

Check for portrait effects matte metadata in existing images.

## Overview

The portrait effects matte is stored in the image file alongside the depth data auxiliary image. You can load, view, and edit the portrait effects matte as a high-level object called an [AVPortraitEffectsMatte](avportraiteffectsmatte.md), analogous to [AVDepthData](avdepthdata.md). This mirrors traditional depth map access using [AVDepthData](avdepthdata.md) in its technique to get the elementary auxiliary image bits out of the file.

![Juxtaposition of the depth map and portrait effects matte of a photo showing a girl holding a flower.](../../../attachments/83298edb81ee6a98d7b6d8df552121ab/media-3030225@2x.png)

### Load and view a matting image from file

Load the portrait effects matte by using [Image I/O](../imageio.md) to extract an auxiliary image of type [kCGImageAuxiliaryDataTypePortraitEffectsMatte](../imageio/kcgimageauxiliarydatatypeportraiteffectsmatte.md). Convert this auxiliary image to an auxiliary information dictionary, which contains the matte as metadata of class [CGImageMetadata](../imageio/cgimagemetadata.md). Generate the portrait effects matte object, [AVPortraitEffectsMatte](avportraiteffectsmatte.md), by passing the dictionary to [+ portraitEffectsMatteFromDictionaryRepresentation:error:](<avportraiteffectsmatte/init(fromdictionaryrepresentation_).md>). From this object, you can generate a [CIImage](../coreimage/ciimage.md) object to bring the image into viewable forms, like [UIImage](../uikit/uiimage.md).

**Swift**

```swift
func portraitEffectsMatteImage(at path: String) -> UIImage? {
    let bundlePath = Bundle.main.bundlePath
    let fileURL = URL(fileURLWithPath: bundlePath).appendingPathComponent(path)
        
    guard let source = CGImageSourceCreateWithURL(fileURL as CFURL, nil),
          let auxiliaryInfoDict = CGImageSourceCopyAuxiliaryDataInfoAtIndex(source, 0, kCGImageAuxiliaryDataTypePortraitEffectsMatte) as? [AnyHashable: Any] else { return nil }
        
    // Create a portrait effects matte from the auxiliary information.
    if let matteData = try? AVPortraitEffectsMatte(fromDictionaryRepresentation: auxiliaryInfoDict),
       let matteCIImage = CIImage(portaitEffectsMatte: matteData) {
        // Return a matte image by using the core image representation.
        return UIImage(ciImage: matteCIImage)
    }
    return nil
}
```

**Objective-C**

```objc
- (UIImage*) portraitEffectsMatteImageAtPath: (NSString*)path
{
    // Convert image path to a file URL:
    NSString* bundlePath = [NSBundle mainBundle].bundlePath;
    NSString* filePath = [bundlePath stringByAppendingPathComponent:path];
    CFURLRef urlRef = CFBridgingRetain([NSURL fileURLWithPath:filePath]);
    
    // Get reference to the image data:
    CGImageSourceRef source = CGImageSourceCreateWithURL(urlRef, nil);
    
    // Query for auxiliary data of specific type:
    CFDictionaryRef auxiliaryInfoDict = CGImageSourceCopyAuxiliaryDataInfoAtIndex(source, 0, kCGImageAuxiliaryDataTypePortraitEffectsMatte);
    
    NSDictionary* auxDataDictionary = (__bridge NSDictionary*)auxiliaryInfoDict;
    if (auxDataDictionary) {
        AVPortraitEffectsMatte* matteData = [AVPortraitEffectsMatte portraitEffectsMatteFromDictionaryRepresentation:auxDataDictionary error:nil];
        
        // Load matte data into Core Image for conversion to UIImage:
        CIImage* matteCIImage = [CIImage imageWithPortaitEffectsMatte:matteData];
        return [UIImage imageWithCIImage:matteCIImage];
    }
    else {
        return nil;
    }
}
```

With this matte image, your app can:

- Access the uncompressed pixels of the portrait effects matte in memory.
- Create rotated or flipped derivative copies of the mask.
- Replace a pixel of the matte with one of your own, reflecting an effect you’re applying to the main image.
- Create a dictionary of elementary PEM parts suitable for writing to a file using Image I/O’s [CGImageDestination](../imageio/cgimagedestination.md).

When decompressed, the matte images are natively L008 ([kCVPixelFormatType_OneComponent8](../corevideo/kcvpixelformattype_onecomponent8.md)), which is an 8-bit one-component format where black is zero. Portrait effects matte images are not gamma corrected. They’re tagged with a linear transfer function, indicating that no color correction should be applied when working with them.

## See Also

### Examining a Portrait Effects matte

- [mattingImage](avportraiteffectsmatte/mattingimage.md) — The portrait effects matte’s internal image, formatted as a pixel buffer.
- [pixelFormatType](avportraiteffectsmatte/pixelformattype.md) — The pixel format type of this portrait effects matte’s internal image.
- [- dictionaryRepresentationForAuxiliaryDataType:](<avportraiteffectsmatte/dictionaryrepresentation(forauxiliarydatatype_).md>) — A dictionary of primitive map information used for writing an image file with a portrait effects matte.
