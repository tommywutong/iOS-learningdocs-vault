---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_FilterExport_c_QTGetEffectsList_txt.html
archived_at: '2026-07-18T03:10:57.721884Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-FilterExport.c-QTInsertChild.txt.md)[Previous](Clippings-FilterExport.c-QTFindChildByIndex.txt.md)

# Clippings/FilterExport.c/QTGetEffectsList.txt

```
    err = QTGetEffectsList( &videoFilterList,   // QTAtomContainer holding a list
                            1,                  // min number of sources that an effect must have to be added to the list
                            1,                  // max number of sources that an effect can have to be added to the list
                            0 );                // getOptions 0 for all effects except 'none' effect
```

[Next](Clippings-FilterExport.c-QTInsertChild.txt.md)[Previous](Clippings-FilterExport.c-QTFindChildByIndex.txt.md)

