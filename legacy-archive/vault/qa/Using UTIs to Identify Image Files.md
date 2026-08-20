---
title: Using UTIs to Identify Image Files
apple_id: DTS10004242
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: CoreServices
published: '2007-05-11'
source_url: https://developer.apple.com/library/archive/qa/qa1518/_index.html
archived_at: '2026-07-18T02:32:05.050460Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1518

# Using UTIs to Identify Image Files

## Q:  How can I use Uniform Type Identifiers (UTIs) to determine if a given file path is an image file?

A: You can determine if a given file, based on its file path, is an image file by comparing its UTI through the Launch Services framework with the supported UTIs from the Image I/O framework.

__Listing 1__  Determining if a file path is an image file.

```objc
- (BOOL)isImageFile:(NSString*)filePath
{
    BOOL isImageFile = NO;
    FSRef fileRef;
    Boolean isDirectory;

    if (FSPathMakeRef((const UInt8 *)[filePath fileSystemRepresentation], &fileRef, &isDirectory) == noErr)
    {
        // get the content type (UTI) of this file
        CFDictionaryRef values = NULL;
        CFStringRef attrs[1] = { kLSItemContentType };
        CFArrayRef attrNames = CFArrayCreate(NULL, (const void **)attrs, 1, NULL);

        if (LSCopyItemAttributes(&fileRef, kLSRolesViewer, attrNames, &values) == noErr)
        {
            // verify that this is a file that the Image I/O framework supports
            if (values != NULL)
            {
                CFTypeRef uti = CFDictionaryGetValue(values, kLSItemContentType);
                if (uti != NULL)
                {
                    CFArrayRef supportedTypes = CGImageSourceCopyTypeIdentifiers();
                    CFIndex i, typeCount = CFArrayGetCount(supportedTypes);

                    for (i = 0; i < typeCount; i++)
                    {
                        CFStringRef supportedUTI = CFArrayGetValueAtIndex(supportedTypes, i);

                        // make sure the supported UTI conforms only to "public.image" (this will skip PDF)
                        if (UTTypeConformsTo(supportedUTI, CFSTR("public.image")))
                        {
                            if (UTTypeConformsTo(uti, supportedUTI))
                            {
                                isImageFile = YES;
                                break;
                            }
                        }
                    }

                    CFRelease(supportedTypes);
                }

                CFRelease(values);
            }
        }

        CFRelease(attrNames);
    }

    return isImageFile;
}
```

If you require other UTIs not related to image files or ImageIO, in place of `CGImageSourceCopyTypeIdentifiers()` you may use the following -

`CFArrayRef UTICreateAllIdentifiersForTag(CFStringRef inTagClass, CFStringRef inTag, CFStringRef inConfirmingToUTI);`

- [Cocoa Drawing Guide - Supported Image File Formats](https://developer.apple.com/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Images/chapter_7_section_3.html)
- [Uniform Type Identifiers Overview](https://developer.apple.com/documentation/Carbon/Conceptual/understanding_utis/understand_utis_intro/chapter_1_section_1.html)
- [An Overview of UTI Functions](https://developer.apple.com/documentation/Carbon/Conceptual/understanding_utis/understand_utis.tasks/chapter_3_section_3.html)
- [Using the Image I/O Framework with Mac OS X 10.4 Tiger](https://developer.apple.com/graphicsimaging/workingwithimageio.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-05-11 | New document that explains how to use Uniform Type Identifiers to identify what files can be opened at images. |

