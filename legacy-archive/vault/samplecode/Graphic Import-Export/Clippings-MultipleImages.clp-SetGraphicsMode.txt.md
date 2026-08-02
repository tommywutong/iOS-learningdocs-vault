---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_MultipleImages_clp_SetGraphicsMode_txt.html
archived_at: '2026-07-18T03:10:58.878090Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-MultipleImages.clp-SetImageIndex.txt.md)[Previous](Clippings-MultipleImages.clp-GetImageCount.txt.md)

# Clippings/MultipleImages.clp/SetGraphicsMode.txt

```swift
        err = GraphicsImportGetImageDescription( importer, &desc );
        if( (*desc)->depth == 32 )
            err = GraphicsImportSetGraphicsMode( importer, graphicsModeStraightAlpha, NULL );
        else
            err = GraphicsImportSetGraphicsMode( importer, ditherCopy, NULL );
```

[Next](Clippings-MultipleImages.clp-SetImageIndex.txt.md)[Previous](Clippings-MultipleImages.clp-GetImageCount.txt.md)

