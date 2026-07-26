---
title: Using Cocoa to Convert Images From RGB to CMYK
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/05/using-cocoa-to-convert-images-from-rgb-to-cmyk/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:fc9b76f7cfb8ce5c'
translated: false
---

> 原文：[Using Cocoa to Convert Images From RGB to CMYK](https://oleb.net/blog/2011/05/using-cocoa-to-convert-images-from-rgb-to-cmyk/)　·　Ole Begemann

# Using Cocoa to Convert Images From RGB to CMYK

Today in the office, someone needed to convert a bunch of images from [RGB](https://en.wikipedia.org/wiki/RGB_color_model) to [CMYK](https://en.wikipedia.org/wiki/Cmyk). Not many programs beside Photoshop can deal with CMYK. [ImageMagick](http://www.imagemagick.org/) can also do it and is easy to use in a scripted environment, but I would have to spend hours in the man pages to make ImageMagick do what I want.

So why not do it in Cocoa? Turns out it only takes a few lines. This is the basic algorithm:

```
NSImage *sourceImage = [[[NSImage alloc] initWithContentsOfFile:sourceFilename] autorelease];
NSBitmapImageRep *sourceImageRep = [[sourceImage representations] objectAtIndex:0];

NSColorSpace *targetColorSpace = [NSColorSpace genericCMYKColorSpace];
NSBitmapImageRep *targetImageRep = [sourceImageRep bitmapImageRepByConvertingToColorSpace:targetColorSpace
    renderingIntent:NSColorRenderingIntentPerceptual];
return targetImageRep;
```

We simply load an `NSImage`, ask it for its bitmap representation and then send it a `bitmapImageRepByConvertingToColorSpace:renderingIntent:` message with the CMYK color space as the first argument. You can play with different values for the `renderingIntent` argument to specify how to handle color that are not present in the target color space. See [the documentation](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSGraphicsContext_Class/Reference/Reference.html#//apple_ref/doc/uid/20000336-SW3) for possible values.

You can get [the code for the full command line app from GitHub](https://github.com/ole/RGBtoCMYK). To use it, simply pass the names of the files you want to convert on the command line.

One nice touch: I use Apple’s block-based enumeration method to loop through the command line arguments. This lets me process the images concurrently so the app should scale quite well without any effort on my part. Simply pass `NSEnumerationConcurrent` to the enumeration method to enable concurrent execution:

```
[commandLineArguments enumerateObjectsWithOptions:NSEnumerationConcurrent
    usingBlock:^(id filename, NSUInteger idx, BOOL *stop) {
    ...
}];
```
