---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_MultipleImages_clp_SetMatrix_txt.html
archived_at: '2026-07-18T03:10:58.960662Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-ScaleAndRotate.c-Rotate.txt.md)[Previous](Clippings-MultipleImages.clp-SetImageIndex.txt.md)

# Clippings/MultipleImages.clp/SetMatrix.txt

```
        SetIdentityMatrix( &matrix );
        GraphicsImportGetDefaultMatrix( importer, &matrix );
        err = GraphicsImportSetMatrix( importer, &matrix );
```

[Next](Clippings-ScaleAndRotate.c-Rotate.txt.md)[Previous](Clippings-MultipleImages.clp-SetImageIndex.txt.md)

