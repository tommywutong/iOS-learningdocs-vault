---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_AlphaComposite_c_CenterForground_txt.html
archived_at: '2026-07-18T03:10:57.098430Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-AlphaComposite.c-DrawBackground.txt.md)[Previous](Graphic%20Import-Export.md)

# Clippings/AlphaComposite.c/CenterForground.txt

```
    err = GraphicsImportGetNaturalBounds( foregroundImporter, &foregroundBounds );
    OffsetRect( &foregroundBounds, 
                (backgroundBounds.right - foregroundBounds.right) / 2,
                (backgroundBounds.bottom - foregroundBounds.bottom) / 2 );
    err = GraphicsImportSetBoundsRect( foregroundImporter,
                                       &foregroundBounds );
```

[Next](Clippings-AlphaComposite.c-DrawBackground.txt.md)[Previous](Graphic%20Import-Export.md)

