---
title: Desktop Sprites
apple_id: DTS10001036
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Desktop_Sprites/Listings/Completed_Lab_ImageCompressionUtilities_h.html
archived_at: '2026-07-18T03:06:46.843293Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Desktop Sprites](Desktop%20Sprites.md)


[Next](Completed%20Lab-main.c.md)[Previous](Completed%20Lab-ImageCompressionUtilities.c.md)

# Completed Lab/ImageCompressionUtilities.h

```c
#ifndef _IMAGECOMPRESSIONUTILITIES_
#define _IMAGECOMPRESSIONUTILITIES_
#ifndef __MOVIES__
    #include <Movies.h>
#endif
#endif

// _____________________ Image Compression Utilities _____________________ //

//OSErr CompressPictAsTransparentRLE( void );
//OSErr CompressPICTResourcesAsTransparentRLE( Boolean withHitTesting );
//void MakePictTransparent( PicHandle pic, RGBColor *keyColor );

// Given a QuickDraw picture, extract QuickTime compressed image data and description, if any
OSErr ExtractCompressData( PicHandle thePict, Handle *dataOut, ImageDescriptionHandle *idh );


// Utilities for compressing from various types of sources


OSErr RecompressCompressedImageWithTransparency( ImageDescriptionHandle originalDesc, Handle originalImageData,
                                                    RGBColor *keyColor, 
                                                    RgnHandle limitHitTestRegion,
                                                    ImageDescriptionHandle *idh, Handle * imageData );
OSErr RecompressPictureWithTransparency ( PicHandle originalPicture,
                                                    RGBColor *keyColor, 
                                                    RgnHandle limitHitTestRegion,
                                                    ImageDescriptionHandle *idh, Handle * imageData );
OSErr RecompressPictureFileWithTransparency ( FSSpec * spec, 
                                                    RGBColor *keyColor, 
                                                    RgnHandle limitHitTestRegion,
                                                    ImageDescriptionHandle *idh, Handle * imageData );

// Low-level callback procedure based routine to compress with/without transparency & hit-testing

enum {
    kRecoProcInitMsg = 1,                   // message and refcon are valid
    kRecoProcDisposeMsg = 2,                // message and refcon are valid
    kRecoProcGetBoundsMsg = 3,              // message, bounds and refcon are valid. Proc fills in bounds with rectangle to use for compressed image.
    kRecoProcDrawMsg = 4                    // message, bounds, drawingPort, portType and refcon are valid. portType is 'imag' if drawing into
                                            // image GWorld, 'imap' if drawing into hit testing GWorld.
};

enum {
    kRecoProcOriginalImageType =            FOUR_CHAR_CODE('imag'),
    kRecoProcHitTestingImageType =          FOUR_CHAR_CODE('imap')
};

typedef pascal OSErr (*CompressDrawProc)( short message, Rect * bounds, GWorldPtr drawingPort, OSType drawingImageType, void * refcon );

OSErr RecompressWithTransparencyFromProc( CompressDrawProc drawProc, void * drawProcRefcon, 
                                                    Boolean includeHitTesting,
                                                    RGBColor *keyColor, 
                                                    RgnHandle hitTestRegion,
                                                    ImageDescriptionHandle *idh, Handle * imageData );
```

[Next](Completed%20Lab-main.c.md)[Previous](Completed%20Lab-ImageCompressionUtilities.c.md)

