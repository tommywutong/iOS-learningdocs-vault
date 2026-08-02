---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_ScaleAndRotate_c_Step5_txt.html
archived_at: '2026-07-18T03:10:59.195327Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Completed%20Lab-AlphaCompositing.c.md)[Previous](Clippings-ScaleAndRotate.c-Step3.txt.md)

# Clippings/ScaleAndRotate.c/Step5.txt

```
    err = GraphicsImportGetBoundsRect( importer, &scaledBounds );
    SizeWindow( window, scaledBounds.right, scaledBounds.bottom, false );
    err = GraphicsImportDraw( importer );
```

[Next](Completed%20Lab-AlphaCompositing.c.md)[Previous](Clippings-ScaleAndRotate.c-Step3.txt.md)

