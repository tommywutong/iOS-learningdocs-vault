---
title: Quick Look Programming Guide
apple_id: TP40005020
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickLook
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Quicklook_Programming_Guide/Articles/QLDrawGraphContext.html
archived_at: '2026-07-18T02:12:36.058935Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quick Look Programming Guide](Introduction%20to%20Quick%20Look%20Programming%20Guide.md)


[Next](Dynamically%20Generating%20Previews.md)[Previous](Overview%20of%20Generator%20Implementation.md)

# Drawing Thumbnails and Previews In a Graphics Context

For previews or thumbnails of documents that consist primarily or solely of graphics and images, the best approach a generator can take is to draw the image of that document in a graphics context provided by Quick Look. The generator draws the document images directly in the client—the graphics context acts as a kind of window onto a surface of the client application. By doing this, you can avoid the overhead of creating and compressing an image into a native type and then requiring the client to decompress and load it on their end. Three graphics contexts are available, each for a different kind of document:

- A graphics context for drawing one or more bitmap images that fit on one page
- A graphics context for drawing one or more vector images that fit on one page
- A graphics context for drawing multiple pages of vector images

[Drawing Document Images in a Graphics Context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqobnknlte) describes how to draw a thumbnail or preview for the first two situations. [Drawing Previews in a PDF Context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqobnknltc) discusses the third kind of graphics context and explains how to use it.

The strategy for drawing single-page previews and thumbnails in a graphics context is the same. Implement the appropriate callback function—`GenerateThumbnailForURL` or `GeneratePreviewForURL`—to read the given document (located by the [CFURLRef](https://developer.apple.com/documentation/corefoundation/cfurl) parameter) into memory. Then get the Quick Look graphics context with a call to [QLThumbnailRequestCreateContext](https://developer.apple.com/documentation/quicklook/1402694-qlthumbnailrequestcreatecontext) or [QLPreviewRequestCreateContext](https://developer.apple.com/documentation/quicklook/1402613-qlpreviewrequestcreatecontext) and draw the thumbnail or preview image in the provided context. Listing 5-1 shows the code for generating a preview of a Sketch document.

__Listing 5-1__  Drawing a Sketch preview in a Quick Look graphics context

```
OSStatus GeneratePreviewForURL(void *thisInterface, QLPreviewRequestRef preview, CFURLRef url, CFStringRef contentTypeUTI, CFDictionaryRef options)
{
    @autoreleasepool{
        // Create and read the document file
        SKTDrawDocument* document = [[SKTDrawDocument alloc] init];

        if (![document readFromURL:(NSURL *)url ofType:(NSString *)contentTypeUTI]) {
            return noErr;
        }

        NSSize canvasSize = [document canvasSize];

        // Preview will be drawn in a vectorized context
        CGContextRef cgContext = QLPreviewRequestCreateContext(preview, *(CGSize *)&canvasSize, false, NULL);
        if(cgContext) {
            NSGraphicsContext* context = [NSGraphicsContext graphicsContextWithGraphicsPort:(void *)cgContext flipped:YES];
            if(context) {
                [document drawDocumentInContext:context];
            }
            QLPreviewRequestFlushContext(preview, cgContext);
            CFRelease(cgContext);
        }
    }
    return noErr;
}
```

Before you draw the preview or thumbnail in the provided graphics context, make sure you save the current context and then restore that context when you’re finished drawing. You should then flush the context with [QLPreviewRequestFlushContext](https://developer.apple.com/documentation/quicklook/1402697-qlpreviewrequestflushcontext) or [QLThumbnailRequestFlushContext](https://developer.apple.com/documentation/quicklook/1402761-qlthumbnailrequestflushcontext) and release it as shown in the above example.

The `QLPreviewRequestCreateContext` and `QLThumbnailRequestCreateContext` functions have identical sets of parameters. The first parameter identifies the preview request or thumbnail request object passed into the callback. The other parameters have a more direct bearing on the created graphics context.

- The second parameter (parameter named _size_ in the function declaration) is the size of the image to be drawn in either pixels or points depending on whether the graphics context is bitmap or vector, respectively.
- The third parameter (_isBitmap_) tells Quick Look whether the returned graphics context should be suited for bitmap or vector graphics; in the example above, a vector-optimized graphics context is requested with a `false` value.
- The fourth and final parameter is a dictionary of properties that you can pass back to Quick Look as hints for handling the drawn image; see _QLPreviewRequest Reference_ and _QLThumbnailRequest Reference_ for details.

A generator implementing the `GenerateThumbnailForURL` callback might be passed in the _options_ directory a floating-point value that specifies how much Quick Look is scaling the thumbnail image. (You can access this value using the [kQLThumbnailOptionScaleFactorKey](https://developer.apple.com/documentation/quicklook/kqlthumbnailoptionscalefactorkey) key.). If you a drawing a vector image for a thumbnail using the graphics context returned from `QLThumbnailRequestCreateContext`, you don’t have to worry about scaling the image; just draw it normally in the the given size, which is in points. Quick Look creates a context with the specified size multiplied by the scale factor in pixels but also applies the appropriate affine transform so that the drawing context appears to the generator to be of the stated size.

If your application has documents that (potentially) have more than one page of vector graphics, you should consider using the [QLPreviewRequestCreatePDFContext](https://developer.apple.com/documentation/quicklook/1402759-qlpreviewrequestcreatepdfcontext) function to create the graphics context for drawing the preview in. This function returns a graphics context suited for PDF content. The procedure is similar to the one described in [Drawing Document Images in a Graphics Context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqobnknlte). However, there are some important differences:

- Some parameters of the `QLPreviewRequestCreatePDFContext` are different from those of [QLPreviewRequestCreateContext](https://developer.apple.com/documentation/quicklook/1402613-qlpreviewrequestcreatecontext):

  - The second parameter (_mediaBox_) is a pointer to a rectangle that defines the location and size of the PDF page.
  - The third parameter (_auxiliaryInfo_) is a dictionary containing auxiliary PDF information.
- You must precede the drawing of each page by calling [CGPDFContextBeginPage](https://developer.apple.com/documentation/coregraphics/cgcontext/1456578-beginpdfpage) and call [CGPDFContextEndPage](https://developer.apple.com/documentation/coregraphics/cgcontext/1456122-endpdfpage) when you have finished drawing a page.

As with `QLPreviewRequestCreateContext`, when you have finished drawing the preview, be sure to call [QLPreviewRequestFlushContext](https://developer.apple.com/documentation/quicklook/1402697-qlpreviewrequestflushcontext).

[Next](Dynamically%20Generating%20Previews.md)[Previous](Overview%20of%20Generator%20Implementation.md)

