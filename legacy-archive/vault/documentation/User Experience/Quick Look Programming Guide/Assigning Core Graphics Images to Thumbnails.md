---
title: Quick Look Programming Guide
apple_id: TP40005020
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickLook
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Quicklook_Programming_Guide/Articles/QLAssignThumbnailImages.html
archived_at: '2026-07-18T02:12:34.624867Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quick Look Programming Guide](Introduction%20to%20Quick%20Look%20Programming%20Guide.md)


[Next](Canceling%20Previews%20and%20Thumbnails.md)[Previous](Saving%20Previews%20and%20Thumbnails%20in%20the%20Document.md)

# Assigning Core Graphics Images to Thumbnails

In some cases the simplest course for generating a thumbnail is to create a Core Graphics image rather than creating an image compatible with the I/O framework or drawing the image in a graphics context. For example, your generator might be using a framework that can directly provide a serialized version of the thumbnail image as a `CGImage` object. For this cases, you can create the Core Graphics image and then communicate that image to Quick Look by calling the [QLThumbnailRequestSetImage](https://developer.apple.com/documentation/quicklook/1402699-qlthumbnailrequestsetimage) function. The main difference between this function and [QLThumbnailRequestSetImageWithData](https://developer.apple.com/documentation/quicklook/1402655-qlthumbnailrequestsetimagewithda) is that the latter function requires the image data to be in a format that is supported by the I/O framework.

Listing 8-1 illustrates approach, using methods of the QT Kit framework to get the poster frame of a movie as a Core Graphics image and setting that as the thumbnail for a movie file.

__Listing 8-1__  Creating and assigning a Core Graphics image

```
OSStatus GenerateThumbnailForURL(void *thisInterface, QLThumbnailRequestRef thumbnail, CFURLRef url, CFStringRef contentTypeUTI, CFDictionaryRef options, CGSize maxSize)
{
    NSError *theErr;
    QTMovie *theMovie = [QTMovie movieWithURL:(__bridge NSURL *)url error:&theErr];
    if (theMovie == nil) {
        if (theErr != nil) {
            NSLog(@"Couldn't load movie URL, error = %@", theErr);
        }
        return noErr;
    }
    [theMovie gotoPosterTime];
    QTTime mTime = [theMovie currentTime];
    NSDictionary *imgProp = [NSDictionary dictionaryWithObject:QTMovieFrameImageTypeCGImageRef forKey:QTMovieFrameImageType];
    CGImageRef theImage = (__bridge CGImageRef)[theMovie frameImageAtTime:mTime withAttributes:imgProp error:&theErr];

    if (theImage == nil) {
        if (theErr != nil) {
            NSLog(@"Couldn't create CGImageRef, error = %@", theErr);
        }
        return noErr;
    }
    QLThumbnailRequestSetImage(thumbnail, theImage, NULL);
    return noErr;
}
```

[Next](Canceling%20Previews%20and%20Thumbnails.md)[Previous](Saving%20Previews%20and%20Thumbnails%20in%20the%20Document.md)

