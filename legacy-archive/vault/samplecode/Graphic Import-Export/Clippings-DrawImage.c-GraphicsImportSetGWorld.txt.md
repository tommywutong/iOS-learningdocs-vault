---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_DrawImage_c_GraphicsImportSetGWorld_txt.html
archived_at: '2026-07-18T03:10:57.440358Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-FilterExport.c-DoExport.txt.md)[Previous](Clippings-DrawImage.c-GraphicsImportDraw.txt.md)

# Clippings/DrawImage.c/GraphicsImportSetGWorld.txt

```
    err = GraphicsImportSetGWorld( importer,                // importer instance
                                   GetWindowPort( window ), // destination graphics port or GWorld
                                   NULL );                  // destination GDevice, set to NULL uses GWorlds device
```

[Next](Clippings-FilterExport.c-DoExport.txt.md)[Previous](Clippings-DrawImage.c-GraphicsImportDraw.txt.md)

