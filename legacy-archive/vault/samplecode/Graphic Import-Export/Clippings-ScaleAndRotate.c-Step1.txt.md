---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_ScaleAndRotate_c_Step1_txt.html
archived_at: '2026-07-18T03:10:59.099628Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-ScaleAndRotate.c-Step3.txt.md)[Previous](Clippings-ScaleAndRotate.c-SetBoundsRect.txt.md)

# Clippings/ScaleAndRotate.c/Step1.txt

```
    // locate and open a graphics importer component
    err = GetGraphicsImporterForFile( &theFSSpec, &importer );

    // get the native size of the image associated with the importer
    err = GraphicsImportGetNaturalBounds( importer, &naturalBounds );

    windowBounds = naturalBounds;
    OffsetRect( &windowBounds, 10, 45 );
    window = NewCWindow( NULL, &windowBounds, "\pScale and Rotate ", true, documentProc, (WindowPtr)-1, true, 0);

    // set the graphics port for drawing
    err = GraphicsImportSetGWorld( importer, GetWindowPort( window ), NULL );

    // draw the image
    err = GraphicsImportDraw( importer );
```

[Next](Clippings-ScaleAndRotate.c-Step3.txt.md)[Previous](Clippings-ScaleAndRotate.c-SetBoundsRect.txt.md)

