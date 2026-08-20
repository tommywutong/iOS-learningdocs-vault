---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_AlphaComposite_c_DrawBackground_txt.html
archived_at: '2026-07-18T03:10:57.129944Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-AlphaComposite.c-Rotate.txt.md)[Previous](Clippings-AlphaComposite.c-CenterForground.txt.md)

# Clippings/AlphaComposite.c/DrawBackground.txt

```
    // set the graphics port for drawing the first image
    err = GraphicsImportSetGWorld( backgroundImporter, GetWindowPort( window ), NULL );

    // draw the background
    err = GraphicsImportDraw( backgroundImporter );
```

[Next](Clippings-AlphaComposite.c-Rotate.txt.md)[Previous](Clippings-AlphaComposite.c-CenterForground.txt.md)

