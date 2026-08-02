---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_AlphaComposite_c_Rotate_txt.html
archived_at: '2026-07-18T03:10:57.165828Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-AlphaComposite.c-SetGraphicsMode.txt.md)[Previous](Clippings-AlphaComposite.c-DrawBackground.txt.md)

# Clippings/AlphaComposite.c/Rotate.txt

```
    err = GraphicsImportGetMatrix( foregroundImporter, &matrix );
    backgroundCenter.x = Long2Fix( backgroundBounds.right - backgroundBounds.left ) / 2;
    backgroundCenter.y = Long2Fix( backgroundBounds.bottom - backgroundBounds.top ) / 2;
    RotateMatrix( &matrix, Long2Fix(30), backgroundCenter.x, backgroundCenter.y );
    err = GraphicsImportSetMatrix( foregroundImporter, &matrix );
    err = GraphicsImportDraw( foregroundImporter );
```

[Next](Clippings-AlphaComposite.c-SetGraphicsMode.txt.md)[Previous](Clippings-AlphaComposite.c-DrawBackground.txt.md)

