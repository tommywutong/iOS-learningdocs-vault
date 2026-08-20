---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_FilterExport_c_Step1_txt.html
archived_at: '2026-07-18T03:10:58.028870Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-FilterExport.c-Step8.txt.md)[Previous](Clippings-FilterExport.c-StandardParameterDialog.txt.md)

# Clippings/FilterExport.c/Step1.txt

```
    // create the offscreen
    err = QTNewGWorld( &sourceGWorld,           // returned GWorld
                       k32ARGBPixelFormat,      // pixel format 
                       &naturalBounds,          // bounds 
                       NULL,                    // cTable   
                       NULL,                    // GDevice
                       kICMTempThenAppMemory ); // flags
    LockPixels( GetGWorldPixMap( sourceGWorld ) );

    // set the graphics port for drawing
    err = GraphicsImportSetGWorld( importer, sourceGWorld, NULL );

    // draw the image to the offscreen
    err = GraphicsImportDraw( importer );

    // blit the offscreen to the window
    CopyBits(GetPortBitMapForCopyBits(sourceGWorld),
             GetPortBitMapForCopyBits(GetWindowPort(window)),
             &naturalBounds,
             &naturalBounds,
             ditherCopy,
             NULL);
```

[Next](Clippings-FilterExport.c-Step8.txt.md)[Previous](Clippings-FilterExport.c-StandardParameterDialog.txt.md)

