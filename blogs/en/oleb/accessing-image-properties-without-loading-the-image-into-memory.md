---
title: Accessing Image Properties Without Loading the Image Into Memory
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/09/accessing-image-properties-without-loading-the-image-into-memory/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8ab0554fc7021779'
translated: false
---

> 原文：[Accessing Image Properties Without Loading the Image Into Memory](https://oleb.net/blog/2011/09/accessing-image-properties-without-loading-the-image-into-memory/)　·　Ole Begemann

# Accessing Image Properties Without Loading the Image Into Memory

Sometimes you might want to retrieve certain properties from an image file, such as the image’s dimensions or other metadata, without actually displaying the full-size image on screen. The simplest way to do that on iOS is using the [`UIImage`](http://developer.apple.com/library/ios/#DOCUMENTATION/UIKit/Reference/UIImage_Class/Reference/Reference.html) class:

```
UIImage *image = [UIImage imageWithContentsOfFile:...];
CGSize imageSize = image.size;
...
```

The problem with this approach is that the entire image gets loaded into memory. And since the pixel data is stored uncompressed in memory, even a small 512 × 512 image (that fills less than half of an iPhone 4’s screen) will take up 1 MB of memory.

# CGImageSource

As of iOS 4, the SDK includes a better solution in the form of the [`CGImageSource...`](http://developer.apple.com/library/ios/#documentation/GraphicsImaging/Reference/CGImageSource/Reference/reference.html) set of functions, which have been available on the Mac since forever. These functions allow you to access certain image metadata without having to load the actual pixel data into memory. For example, getting the pixel dimensions works like this (make sure to include the ImageIO.framework in your target):

```
#import <ImageIO/ImageIO.h>

NSURL *imageFileURL = [NSURL fileURLWithPath:...];
CGImageSourceRef imageSource = CGImageSourceCreateWithURL((CFURLRef)imageFileURL, NULL);
if (imageSource == NULL) {
    // Error loading image
    ...
    return;
}

NSDictionary *options = [NSDictionary dictionaryWithObjectsAndKeys:
                         [NSNumber numberWithBool:NO], (NSString *)kCGImageSourceShouldCache,
                         nil];
CFDictionaryRef imageProperties = CGImageSourceCopyPropertiesAtIndex(imageSource, 0, (CFDictionaryRef)options);
if (imageProperties) {
    NSNumber *width = (NSNumber *)CFDictionaryGetValue(imageProperties, kCGImagePropertyPixelWidth);
    NSNumber *height = (NSNumber *)CFDictionaryGetValue(imageProperties, kCGImagePropertyPixelHeight);
    NSLog(@"Image dimensions: %@ x %@ px", width, height);
    CFRelease(imageProperties);
}
CFRelease(imageSource);
```

# All the Metadata You Dreamed Of

The dictionary returned by `CGImageSourceCopyPropertiesAtIndex()` contains a lot more than just the image dimensions. If present, it includes the complete [EXIF](https://en.wikipedia.org/wiki/Exif) and [IPTC](https://en.wikipedia.org/wiki/IPTC_Information_Interchange_Model) metadata and also various file-format-specific information for TIFF, GIF, JPEG, PNG and Raw files (among others).

As an example, let’s read out the date a photo was taken, the model name of the camera and the GPS coordinates stored in the metadata:

```
CFDictionaryRef exif = CFDictionaryGetValue(imageProperties, kCGImagePropertyExifDictionary);
if (exif) {
  NSString *dateTakenString = (NSString *)CFDictionaryGetValue(exif, kCGImagePropertyExifDateTimeOriginal);
  NSLog(@"Date Taken: %@", dateTakenString);
}

CFDictionaryRef tiff = CFDictionaryGetValue(imageProperties, kCGImagePropertyTIFFDictionary);
if (tiff) {
    NSString *cameraModel = (NSString *)CFDictionaryGetValue(tiff, kCGImagePropertyTIFFModel);
    NSLog(@"Camera Model: %@", cameraModel);
}

CFDictionaryRef gps = CFDictionaryGetValue(imageProperties, kCGImagePropertyGPSDictionary);
if (gps) {
    NSString *latitudeString = (NSString *)CFDictionaryGetValue(gps, kCGImagePropertyGPSLatitude);
    NSString *latitudeRef = (NSString *)CFDictionaryGetValue(gps, kCGImagePropertyGPSLatitudeRef);
    NSString *longitudeString = (NSString *)CFDictionaryGetValue(gps, kCGImagePropertyGPSLongitude);
    NSString *longitudeRef = (NSString *)CFDictionaryGetValue(gps, kCGImagePropertyGPSLongitudeRef);
    NSLog(@"GPS Coordinates: %@ %@ / %@ %@", longitudeString, longitudeRef, latitudeString, latitudeRef);
}
```

This produces the following output on my sample image:

```
Date Taken: 2011:03:27 11:30:30
Camera Model: Canon EOS 20D
GPS Coordinates: 8.374788 E / 54.89472 N
```

An `NSLog(@"Image properties: %@", (NSDictionary *)imageProperties);` will quickly show you all the available metadata for a particular image. It’s fun to experiment with different files. The documentation lists all available metadata keys at [CGImageProperties Reference](https://developer.apple.com/reference/imageio/1666330-cgimageproperties).
