---
title: 在不将图像加载到内存的情况下访问图像属性
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/09/accessing-image-properties-without-loading-the-image-into-memory/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8ab0554fc7021779'
translated: true
---

> 原文：[Accessing Image Properties Without Loading the Image Into Memory](https://oleb.net/blog/2011/09/accessing-image-properties-without-loading-the-image-into-memory/)　·　Ole Begemann

# 在不将图像加载到内存的情况下访问图像属性

有时你可能希望从图像文件中检索某些属性，例如图像的尺寸或其他元数据，而无需在屏幕上实际显示全尺寸图像。在 iOS 上实现这一点的最简单方法是使用 [`UIImage`](http://developer.apple.com/library/ios/#DOCUMENTATION/UIKit/Reference/UIImage_Class/Reference/Reference.html) 类：

```
UIImage *image = [UIImage imageWithContentsOfFile:...];
CGSize imageSize = image.size;
...
```

这种方法的问题在于，整个图像会被加载到内存中。而且由于像素数据在内存中以未压缩的形式存储，即使是一个小小的 512 × 512 图像（它填不满 iPhone 4 屏幕的一半）也会占用 1 MB 的内存。

# CGImageSource

从 iOS 4 开始，SDK 以 [`CGImageSource...`](http://developer.apple.com/library/ios/#documentation/GraphicsImaging/Reference/CGImageSource/Reference/reference.html) 函数集的形式提供了一个更好的解决方案，这些函数在 Mac 上已经可用很久了。这些函数允许你访问某些图像元数据，而无需将实际像素数据加载到内存中。例如，获取像素尺寸的方法如下（确保在你的 target 中包含了 ImageIO.framework）：

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

# 你梦寐以求的所有元数据

`CGImageSourceCopyPropertiesAtIndex()` 返回的字典包含的远不止图像尺寸。如果存在，它将包含完整的 [EXIF](https://en.wikipedia.org/wiki/Exif) 和 [IPTC](https://en.wikipedia.org/wiki/IPTC_Information_Interchange_Model) 元数据，以及 TIFF、GIF、JPEG、PNG 和 Raw 文件（以及其他格式）的各种文件格式特定信息。

作为示例，让我们读取照片的拍摄日期、相机型号名称以及存储在元数据中的 GPS 坐标：

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

这在我的示例图像上产生以下输出：

```
Date Taken: 2011:03:27 11:30:30
Camera Model: Canon EOS 20D
GPS Coordinates: 8.374788 E / 54.89472 N
```

一个 `NSLog(@"Image properties: %@", (NSDictionary *)imageProperties);` 将快速向你展示特定图像的所有可用元数据。用不同的文件进行实验很有趣。文档在 [CGImageProperties Reference](https://developer.apple.com/reference/imageio/1666330-cgimageproperties) 中列出了所有可用的元数据键。
