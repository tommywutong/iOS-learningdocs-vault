---
title: Modifying Image Metadata Without Recompressing Image
apple_id: DTS40016579
resource_type: QA
platform: iOS|macOS
topic: null
technology: ImageIO
published: '2015-09-08'
source_url: https://developer.apple.com/library/archive/qa/qa1895/_index.html
archived_at: '2026-07-18T02:35:33.270149Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1895

# Modifying Image Metadata Without Recompressing Image

## Q:  How can I modify the metadata associated with an image without having to save or recompress an image?

A: Starting in Mac OS X 10.8 and iOS 7.0, the Image I/O framework APIs can be used to modify EXIF and other image metadata in JPEG, PNG, PSD, and TIFF files without recompressing the image data. In order to take advantage of this functionality, you must must use the following API when calling the Image I/O framework:


```
bool CGImageDestinationCopyImageSource(CGImageDestinationRef idst, CGImageSourceRef isrc, CFDictionaryRef options, CFErrorRef * err);
```

Here is an example showing how you would normally use this call in sequence with other Image I/O APIs when updating a file:


```
 /* get the file type */
    CFStringRef UTI = CGImageSourceGetType(imageSource);
    if ( NULL == UTI ) { /* Handle Error Retrieving File Type Accordingly */ }

    /* create an image destination for saving the file */
   CGImageDestinationRef destination = CGImageDestinationCreateWithData(finalImageData, UTI, 1, NULL);
    if ( nil == destination ) {/* Handle Error Creating CGImageDestinationRef Accordingly */}

    /* create an CFDictionaryRef with the modified metadata */
    CFDictionaryRef options_dict = ...

    /* add an image to the destination */
    CFErrorRef errorRef = nil;
    if ( ! CGImageDestinationCopyImageSource(destination, imageSource, options_dict, &errorRef) ) {
        CFStringRef error_description = CFErrorCopyDescription(errorRef);

        CFRelease(error_description);
    }
```

At the time of writing this Technical Q&A, the `CGImageDestinationCopyImageSource` API supports the following image formats: JPEG, PNG, PSD, TIFF.

`CGImageDestinationCopyImageSource` will return false if an error occurs while writing out the metadata. This is also true If an unsupported image format is passed to `CGImageDestinationCopyImageSource`. In both cases, developers should handle errors accordingly.

The `CGImageDestinationCopyImageSource` API will copy the contents of the image source to the image destination without modifying the image data. It also allows the image metadata to be modified by adding the keys and values defined in CGImageDestination.h to the options parameter.

For more information including the available options to pass in see CGImageDestination.h.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-09-08 | New document that image I/O provides an API that allows for modifying image metadata without having to resave or recompress the image. |

