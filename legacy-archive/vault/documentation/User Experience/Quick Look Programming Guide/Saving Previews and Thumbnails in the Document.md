---
title: Quick Look Programming Guide
apple_id: TP40005020
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickLook
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Quicklook_Programming_Guide/Articles/QLSaveInDocument.html
archived_at: '2026-07-18T02:12:37.932422Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quick Look Programming Guide](Introduction%20to%20Quick%20Look%20Programming%20Guide.md)


[Next](Assigning%20Core%20Graphics%20Images%20to%20Thumbnails.md)[Previous](Dynamically%20Generating%20Previews.md)

# Saving Previews and Thumbnails in the Document

As one approach for providing thumbnail and preview data to Quick Look, the application can store that data as part of the document data. The generator can then access it and return it to Quick Look in a call to [QLThumbnailRequestSetImageWithData](https://developer.apple.com/documentation/quicklook/1402655-qlthumbnailrequestsetimagewithda) or [QLPreviewRequestSetDataRepresentation](https://developer.apple.com/documentation/quicklook/1402661-qlpreviewrequestsetdatarepresent). This approach permits a quick response time for the generator, but at the expense of a larger document file.

To illustrate how your generator might provide previews and thumbnails using this approach, the following listings show modifications to the code for the Sketch application that writes a thumbnail image as part of the document data. Listing 7-1 shows how you might define a property of the [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) subclass to hold the image data.

__Listing 7-1__  Sketch example project: adding a thumbnail property

```objc
@interface SKTDrawDocument : NSDocument {
    @private
    NSMutableArray *_graphics;
    // ...other instance variables here...
    NSData *_thumbnail;
}
// ...existing methods here...
- (NSData *)thumbnail;
```

Implement the `thumbnail` accessor method to return the thumbnail image. To the the `NSDocument` method that prepares the document data for writing out to a file ([dataOfType:error:](https://developer.apple.com/documentation/appkit/nsdocument/1515205-data)) are added the lines of code in Listing 7-2 indicated by the “new” labels.

__Listing 7-2__  Sketch example project: including the thumbnail with the document data

```objc
static NSString *SKTThumbnailImageKey = @"SketchThumbnail";                   // new

- (NSData *)dataOfType:(NSString *)typeName error:(NSError **)outError {
    NSData *data,;
    NSArray *graphics = [self graphics];
    NSPrintInfo *printInfo = [self printInfo];
    NSWorkspace *workspace = [NSWorkspace sharedWorkspace];
    BOOL useTypeConformance = [workspace respondsToSelector:@selector(type:conformsToType:)];

    if ((useTypeConformance && [workspace type:SKTDrawDocumentNewTypeName conformsToType:typeName])
        || [typeName isEqualToString:SKTDrawDocumentOldTypeName]) {
        NSData *tiffRep;                                                     // new
        NSMutableDictionary *properties = [NSMutableDictionary dictionary];

        [properties setObject:[NSNumber numberWithInt:SKTDrawDocumentCurrentVersion] forKey:SKTDrawDocumentVersionKey];
        [properties setObject:[SKTGraphic propertiesWithGraphics:graphics] forKey:SKTDrawDocumentGraphicsKey];
        [properties setObject:[NSArchiver archivedDataWithRootObject:printInfo] forKey:SKTDrawDocumentPrintInfoKey];
        tiffRep = [self TIFFDataWithGraphics:graphics error:outError];        // new
        [properties setObject:tiffRep forKey:SKTThumbnailImageKey];           // new
        data = [NSPropertyListSerialization dataFromPropertyList:properties
                                                          format:NSPropertyListBinaryFormat_v1_0
                                                errorDescription:NULL];
    } else if ((useTypeConformance && [workspace type:(__bridge NSString *)kUTTypePDF conformsToType:typeName])
               || [typeName isEqualToString:NSPDFPboardType]) {
        data = [SKTRenderingView pdfDataWithGraphics:graphics];
    } else {
        NSParameterAssert((useTypeConformance && [workspace type:(__bridge NSString *)kUTTypeTIFF conformsToType:typeName])
                          || [typeName isEqualToString:NSTIFFPboardType]);
        data = [SKTRenderingView tiffDataWithGraphics:graphics error:outError];
    }
    return data;
}
```

In the corresponding `NSDocument` method for reading document data back in ([readFromData:ofType:error:](https://developer.apple.com/documentation/appkit/nsdocument/1515198-readfromdata)) “unpack” the thumbnail from the dictionary of document properties:

```
_thumbnail = [properties objectForKey:SKTThumbnailImageKey];
```

Now implementing the generator for Sketch is a simple matter of accessing the thumbnail image data and passing it to Quick Look in a call to [QLThumbnailRequestSetImageWithData](https://developer.apple.com/documentation/quicklook/1402655-qlthumbnailrequestsetimagewithda), as shown in Listing 7-3. (For previews, the corresponding function is [QLPreviewRequestSetDataRepresentation](https://developer.apple.com/documentation/quicklook/1402661-qlpreviewrequestsetdatarepresent).)

__Listing 7-3__  Returning the stored thumbnail image to Quick Look

```
OSStatus GenerateThumbnailForURL(void *thisInterface, QLThumbnailRequestRef thumbnail, CFURLRef url, CFStringRef contentTypeUTI, CFDictionaryRef options, CGSize maxSize)
{
    @autoreleasepool {
        SKTDrawDocument* document = [[SKTDrawDocument alloc] init];
        if (![document readFromURL:(__bridge NSURL *)url
                            ofType:(__bridge NSString *)contentTypeUTI]) {
            return noErr;
        }
        if ([document respondsToSelector:@selector(thumbnail)]) {  // runtime verification
            NSData *tiffData = [document thumbnail];
            if (tiffData != nil) {
                NSDictionary *props = [NSDictionary dictionaryWithObject:@"public.tiff" forKey:(__bridge NSString *)kCGImageSourceTypeIdentifierHint];
                QLThumbnailRequestSetImageWithData(thumbnail, (__bridge CFDataRef)tiffData, (__bridge CFDictionaryRef)props);
                return noErr;
            }
        }
        NSSize canvasSize = [document canvasSize];
        CGContextRef cgContext = QLThumbnailRequestCreateContext(thumbnail, *(CGSize *)&canvasSize, false, NULL);
        if (cgContext) {
            NSGraphicsContext* context = [NSGraphicsContext graphicsContextWithGraphicsPort:(void *)cgContext flipped:YES];
            if (context) {
                [document drawDocumentInContext:context];
            }
            QLThumbnailRequestFlushContext(thumbnail, cgContext);
            CFRelease(cgContext);
        }
    }
    return noErr;
}
```

In the call to `QLThumbnailRequestSetImageWithData`, the generator indicates the image format to Quick Look with the [kCGImageSourceTypeIdentifierHint](https://developer.apple.com/documentation/imageio/kcgimagesourcetypeidentifierhint) property. Note that this example checks whether the class of the document object implements the `thumbnail` accessor method (to exclude prior versions of the application) and, if so, it checks whether thumbnail data is returned. If it isn’t, it draws the thumbnail image in a Quick Look–provided graphics context.

[Next](Assigning%20Core%20Graphics%20Images%20to%20Thumbnails.md)[Previous](Dynamically%20Generating%20Previews.md)

